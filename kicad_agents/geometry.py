"""Geometry helpers shared by schematic and PCB extraction."""

import math


def empty_bbox():
    return None


def add_point(bbox, point):
    x_value, y_value = point
    if bbox is None:
        return [x_value, y_value, x_value, y_value]
    bbox[0] = min(bbox[0], x_value)
    bbox[1] = min(bbox[1], y_value)
    bbox[2] = max(bbox[2], x_value)
    bbox[3] = max(bbox[3], y_value)
    return bbox


def add_points(bbox, points):
    for point in points:
        bbox = add_point(bbox, point)
    return bbox


def merge_bbox(first, second):
    if first is None:
        return None if second is None else list(second)
    if second is None:
        return list(first)
    return [
        min(first[0], second[0]),
        min(first[1], second[1]),
        max(first[2], second[2]),
        max(first[3], second[3]),
    ]


def expand_bbox(bbox, amount):
    if bbox is None:
        return None
    return [bbox[0] - amount, bbox[1] - amount, bbox[2] + amount, bbox[3] + amount]


def bbox_corners(bbox):
    if bbox is None:
        return []
    return [
        (bbox[0], bbox[1]),
        (bbox[2], bbox[1]),
        (bbox[2], bbox[3]),
        (bbox[0], bbox[3]),
    ]


def bbox_record(bbox, measurement, units="mm"):
    if bbox is None:
        return {
            "measurement": measurement,
            "units": units,
            "available": False,
            "min": None,
            "max": None,
            "width": None,
            "height": None,
            "center": None,
        }
    return {
        "measurement": measurement,
        "units": units,
        "available": True,
        "min": {"x": round(bbox[0], 6), "y": round(bbox[1], 6)},
        "max": {"x": round(bbox[2], 6), "y": round(bbox[3], 6)},
        "width": round(bbox[2] - bbox[0], 6),
        "height": round(bbox[3] - bbox[1], 6),
        "center": {
            "x": round((bbox[0] + bbox[2]) / 2, 6),
            "y": round((bbox[1] + bbox[3]) / 2, 6),
        },
    }


def rotate_point(point, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    cosine = math.cos(angle_radians)
    sine = math.sin(angle_radians)
    x_value, y_value = point
    return (
        x_value * cosine - y_value * sine,
        x_value * sine + y_value * cosine,
    )


def transform_point(point, origin=(0.0, 0.0), angle_degrees=0.0, mirror=""):
    x_value, y_value = point
    if mirror == "x":
        y_value = -y_value
    elif mirror == "y":
        x_value = -x_value
    rotated_x, rotated_y = rotate_point((x_value, y_value), angle_degrees)
    return origin[0] + rotated_x, origin[1] + rotated_y


def transform_bbox(bbox, origin=(0.0, 0.0), angle_degrees=0.0, mirror=""):
    transformed = empty_bbox()
    for point in bbox_corners(bbox):
        transformed = add_point(
            transformed,
            transform_point(point, origin=origin, angle_degrees=angle_degrees, mirror=mirror),
        )
    return transformed


def rotated_rectangle_bbox(center, size, angle_degrees=0.0):
    half_width = size[0] / 2
    half_height = size[1] / 2
    corners = [
        (-half_width, -half_height),
        (half_width, -half_height),
        (half_width, half_height),
        (-half_width, half_height),
    ]
    bbox = empty_bbox()
    for corner in corners:
        rotated = rotate_point(corner, angle_degrees)
        bbox = add_point(bbox, (center[0] + rotated[0], center[1] + rotated[1]))
    return bbox


def _circle_from_three_points(start, middle, end):
    x1, y1 = start
    x2, y2 = middle
    x3, y3 = end
    denominator = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if abs(denominator) < 1e-12:
        return None
    center_x = (
        (x1 * x1 + y1 * y1) * (y2 - y3)
        + (x2 * x2 + y2 * y2) * (y3 - y1)
        + (x3 * x3 + y3 * y3) * (y1 - y2)
    ) / denominator
    center_y = (
        (x1 * x1 + y1 * y1) * (x3 - x2)
        + (x2 * x2 + y2 * y2) * (x1 - x3)
        + (x3 * x3 + y3 * y3) * (x2 - x1)
    ) / denominator
    radius = math.hypot(x1 - center_x, y1 - center_y)
    return (center_x, center_y), radius


def _normalized_angle(angle):
    return angle % (2 * math.pi)


def _ccw_distance(start, end):
    return (_normalized_angle(end) - _normalized_angle(start)) % (2 * math.pi)


def arc_bbox(start, middle, end):
    circle = _circle_from_three_points(start, middle, end)
    if circle is None:
        return add_points(empty_bbox(), [start, middle, end])

    center, radius = circle
    start_angle = math.atan2(start[1] - center[1], start[0] - center[0])
    middle_angle = math.atan2(middle[1] - center[1], middle[0] - center[0])
    end_angle = math.atan2(end[1] - center[1], end[0] - center[0])
    counter_clockwise = _ccw_distance(start_angle, middle_angle) <= _ccw_distance(start_angle, end_angle)

    candidate_angles = [start_angle, end_angle]
    for angle in [0, math.pi / 2, math.pi, 3 * math.pi / 2]:
        if counter_clockwise:
            on_arc = _ccw_distance(start_angle, angle) <= _ccw_distance(start_angle, end_angle) + 1e-10
        else:
            on_arc = _ccw_distance(end_angle, angle) <= _ccw_distance(end_angle, start_angle) + 1e-10
        if on_arc:
            candidate_angles.append(angle)

    points = [
        (center[0] + radius * math.cos(angle), center[1] + radius * math.sin(angle))
        for angle in candidate_angles
    ]
    return add_points(empty_bbox(), points)


def point_on_segment(point, start, end, tolerance=0.0002):
    point_x, point_y = point
    start_x, start_y = start
    end_x, end_y = end
    cross_product = (point_y - start_y) * (end_x - start_x) - (point_x - start_x) * (end_y - start_y)
    segment_length = math.hypot(end_x - start_x, end_y - start_y)
    if segment_length == 0:
        return math.hypot(point_x - start_x, point_y - start_y) <= tolerance
    if abs(cross_product) > tolerance * segment_length:
        return False
    dot_product = (point_x - start_x) * (end_x - start_x) + (point_y - start_y) * (end_y - start_y)
    if dot_product < -tolerance:
        return False
    squared_length = (end_x - start_x) ** 2 + (end_y - start_y) ** 2
    return dot_product <= squared_length + tolerance

