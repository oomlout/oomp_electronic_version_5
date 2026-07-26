
import copy
import itertools

from requests import options

from oomp_populate_helper import build_oomp_id, write_extras


def main(**kwargs):
    
    options = kwargs.get("options", [])
    
    

    if True:
        option = {}
        #taxonomy_3 wire
        option["taxonomy_2"] = f"display"
        #lcd
        option["taxonomy_3"] = f"lcd"
        #character
        option["taxonomy_4"] = f"character"
        #16_by_2
        option["taxonomy_5"] = f"16_by_2"
        #backlight_yellow
        option["taxonomy_6"] = f"backlight_yellow"
        options.append(option)

    


# Call main automatically
if __name__ == "__main__":
    main()
