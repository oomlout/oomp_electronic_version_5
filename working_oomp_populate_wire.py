
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = kwargs.get("options", [])
    
    

    if True:
        option = {}
        #taxonomy_3 wire
        option["taxonomy_2"] = f"wire"
        #4 prototyping
        option["taxonomy_3"] = f"prototyping"
        option["taxonomy_4"] = f"jumper"
        option["taxonomy_5"] = f"aligator_clip"
        #to_aligator_clip
        option["taxonomy_6"] = f"to_aligator_clip"
        #300_mm_length
        option["taxonomy_7"] = f"300_mm_length"
        #bundle of 7
        option["taxonomy_8"] = f"bundle_of_7"

        options.append(copy.deepcopy(option))
    if True:
        option = {}
        #taxonomy_3 wire
        option["taxonomy_2"] = f"wire"
        #4 prototyping
        option["taxonomy_3"] = f"prototyping"
        option["taxonomy_4"] = f"jumper"
        option["taxonomy_5"] = f"dupont_plug"
        #to_aligator_clip
        option["taxonomy_6"] = f"to_dupont_socket"
        #300_mm_length
        option["taxonomy_7"] = f"150_mm_length"
        #bundle of 7
        option["taxonomy_8"] = f"ribbon_cable_rainbow_40"
        options.append(copy.deepcopy(option))
    if True:
        option = {}
        #taxonomy_3 wire
        option["taxonomy_2"] = f"wire"
        #4 prototyping
        option["taxonomy_3"] = f"prototyping"
        option["taxonomy_4"] = f"jumper"
        option["taxonomy_5"] = f"breadboard_plug"
        #to_aligator_clip
        option["taxonomy_6"] = f"to_breadboard_plug"
        #300_mm_length
        option["taxonomy_7"] = f"mixed_length"
        #bundle of 7
        option["taxonomy_8"] = f"bundle_rainbow_75_pieces"
        options.append(copy.deepcopy(option))
    


# Call main automatically
if __name__ == "__main__":
    main()
