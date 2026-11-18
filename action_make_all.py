import copy
#import working_scad

def main(**kwargs):

    if False:
        import action_delete_generated_files
        action_delete_generated_files.main(**kwargs)

    kwargs["run_oomp_populate"] = True

    kwargs["run_oomp"] = True

    kwargs["run_action"] = True
    #kwargs["run_action"] = False

    kwargs["run_scad"] = True

    kwargs["run_svg"] = True

    kwargs["generate_stl"] = True

    import working
    working.run(**kwargs)

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)