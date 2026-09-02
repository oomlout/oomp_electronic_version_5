
import copy
import itertools

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = []
    
    kwargs["options"] = options

    import working_oomp_populate_display
    working_oomp_populate_display.main(**kwargs)
    import working_oomp_populate_wire
    working_oomp_populate_wire.main(**kwargs)
    import working_oomp_populate_prototyping
    working_oomp_populate_prototyping.main(**kwargs)
    import working_oomp_populate_led
    working_oomp_populate_led.main(**kwargs)
    import working_oomp_populate_resistor
    working_oomp_populate_resistor.main(**kwargs)
    import working_oomp_populate_resistor_array
    working_oomp_populate_resistor_array.main(**kwargs)
    import working_oomp_populate_capacitor
    working_oomp_populate_capacitor.main(**kwargs)
    import working_oomp_populate_crystal
    working_oomp_populate_crystal.main(**kwargs)
    import working_oomp_populate_ferrite_bead
    working_oomp_populate_ferrite_bead.main(**kwargs)
    import working_oomp_populate_connector
    working_oomp_populate_connector.main(**kwargs)
    import working_oomp_populate_diode
    working_oomp_populate_diode.main(**kwargs)
    import working_oomp_populate_transistor
    working_oomp_populate_transistor.main(**kwargs)
    import working_oomp_populate_ic
    working_oomp_populate_ic.main(**kwargs)
    import working_oomp_populate_project
    working_oomp_populate_project.main(**kwargs)
    import working_oomp_populate_mounting_hole
    working_oomp_populate_mounting_hole.main(**kwargs)


    ###### populate taxonomy details and oobb details
    if True:
        import working_oomp_populate_svg
        for option in options:       
            if option.get("taxonomy_1", "") == "":
                option["taxonomy_1"] = "electronic"
            if option.get("taxonomy_1", "") == "electronic":
                working_oomp_populate_svg.add_svg_details(option)
            #option["taxonomy_2"] = f"electronic"             
            #value_name = "code"
            #value = option.get(value_name, None)
            #option["taxonomy_3"] = f"{value}_{value_name}"
            #oobb details
            if False:
                pass
                oobb_details = {}
                #taxonomy_4 hole_cover
                oobb_details["oobb_name"] = option_type
                oobb_details["diameter"] = option.get("diameter", None)            
                oobb_details["depth"] = option.get("depth", None)
                option["oobb_details"] = oobb_details
            #svg details
            if False:
                pass
                svg_details = {}
                svg_details["svg_name"] = option_type
                svg_details["svg_width"] = option.get("width", None)            
                svg_details["svg_height"] = option.get("height", None)
                option["svg_details"] = svg_details

    #load the options into full list
    extras = []
    for option in options:
        extra = {}
        extra.update(option)
        extras.append(extra)

    
    ######### add notes from an id string
    import working_oomp_populate_extra_detail
    working_oomp_populate_extra_detail.main(extras=extras)


    write_extras(extras)



# Call main automatically
if __name__ == "__main__":
    main()
