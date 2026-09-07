import copy
import working_scad

def main(**kwargs):
    filter = ["hanqaqa_easyduino_raspberry_pi_pico_2040_current"]
    kwargs["filter"] = filter
    kwargs["run_oomp_populate"] = True

    kwargs["run_oomp"] = True

    kwargs["run_action"] = True
    #kwargs["run_action"] = False

    kwargs["run_scad"] = False

    kwargs["generate_stl"] = False

    import working
    working.run(**kwargs)

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)