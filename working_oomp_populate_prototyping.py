
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = kwargs.get("options", [])
    
    
    colors = ["white", "transparent"]
    for color in colors:
        if True:
            option = {}
            #taxonomy_3 wire
            option["taxonomy_2"] = f"prototyping"
            #4 prototyping
            option["taxonomy_3"] = f"breadboard"
            option["taxonomy_4"] = f"800_point"
            option["taxonomy_5"] = f"{color}_color"
            options.append(copy.deepcopy(option))
        #40 pint breadboard
        if True:
            option = {}
            #taxonomy_3 wire
            option["taxonomy_2"] = f"prototyping"
            #4 prototyping
            option["taxonomy_3"] = f"breadboard"
            option["taxonomy_4"] = f"400_point"
            option["taxonomy_5"] = f"{color}_color"
            options.append(copy.deepcopy(option))
    #170 point breadboard
    if True:
        option = {}
        #taxonomy_3 wire
        option["taxonomy_2"] = f"prototyping"
        #4 prototyping
        option["taxonomy_3"] = f"breadboard"
        option["taxonomy_4"] = f"170_point"
        option["taxonomy_5"] = f"white_color"
        options.append(copy.deepcopy(option))
    


# Call main automatically
if __name__ == "__main__":
    main()
