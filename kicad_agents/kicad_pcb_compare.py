"""Run with KiCad's Python. Read/normalise copies only; never save the source PCB."""

import json
import sys

import pcbnew


def formatted(item):
    output = pcbnew.STRING_FORMATTER()
    writer = pcbnew.PCB_IO_KICAD_SEXPR()
    writer.SetOutputFormatter(output)
    writer.Format(item)
    return output.GetString()


def normalised(footprint):
    copy = pcbnew.Cast_to_FOOTPRINT(footprint.Duplicate(False))
    if copy.IsFlipped():
        copy.Flip(copy.GetPosition(), pcbnew.FLIP_DIRECTION_LEFT_RIGHT)
    copy.SetOrientationDegrees(0)
    copy.SetPosition(pcbnew.VECTOR2I(0, 0))
    # KiCad normalises equivalent rect/poly representations in memory.
    copy.NormalizeForCompare()
    return formatted(copy)


def placed_mark(footprint, mark, mark_y):
    copy = pcbnew.Cast_to_FOOTPRINT(footprint.Duplicate(False))
    position = copy.GetPosition()
    flipped = copy.IsFlipped()
    if flipped:
        copy.Flip(position, pcbnew.FLIP_DIRECTION_LEFT_RIGHT)
    orientation = copy.GetOrientationDegrees()
    copy.SetOrientationDegrees(0)
    copy.SetPosition(pcbnew.VECTOR2I(0, 0))
    text = pcbnew.PCB_TEXT(copy)
    text.SetText(mark)
    text.SetLayer(pcbnew.F_SilkS)
    text.SetTextSize(pcbnew.VECTOR2I(pcbnew.FromMM(0.8), pcbnew.FromMM(0.8)))
    text.SetTextThickness(pcbnew.FromMM(0.12))
    text.SetPosition(pcbnew.VECTOR2I(0, pcbnew.FromMM(mark_y)))
    copy.Add(text)
    copy.SetPosition(position)
    copy.SetOrientationDegrees(orientation)
    if flipped:
        copy.Flip(position, pcbnew.FLIP_DIRECTION_LEFT_RIGHT)
    return formatted(text)


def run(request):
    board = pcbnew.LoadBoard(request['board'])
    master_records = {}
    for library_id, path in request['masters'].items():
        from pathlib import Path
        path = Path(path)
        master = pcbnew.FootprintLoad(str(path.parent), path.stem)
        if master is None:
            raise ValueError(f'KiCad could not load master: {path}')
        master_records[library_id] = normalised(master)
    footprints = {}
    for footprint in board.GetFootprints():
        uuid = footprint.m_Uuid.AsString()
        record = {'normalised': normalised(footprint), 'reference': footprint.GetReference()}
        mark = request.get('marks', {}).get(uuid)
        if mark:
            record['mark'] = placed_mark(footprint, mark['text'], mark['y'])
        footprints[uuid] = record
    return {'kicad_version': pcbnew.Version(), 'masters': master_records, 'footprints': footprints}


if __name__ == '__main__':
    print(json.dumps(run(json.load(sys.stdin))))
