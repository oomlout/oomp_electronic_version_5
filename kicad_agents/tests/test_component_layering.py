import svg_help

def test_assembly_artwork_lifts_pads_above_body_with_labels_on_top():
    thing = {'svg_components': [{'shape': 'rect', 'css_class': 'pad', 'style_name': 'component.pad'},
                               {'shape': 'text', 'style_name': 'component.label'},
                               {'shape': 'rounded_rectangle', 'style_name': 'component.body'},
                               {'shape': 'circle', 'style_name': 'component.pin_one'}]}
    svg_help._lift_pads_above_body(thing)
    order = [(component['shape'], component.get('css_class')) for component in thing['svg_components']]
    assert order == [('rounded_rectangle', None), ('rect', 'pad'), ('text', None), ('circle', None)]
    without_pads = {'svg_components': [{'shape': 'rect'}]}
    svg_help._lift_pads_above_body(without_pads)
    assert len(without_pads['svg_components']) == 1
