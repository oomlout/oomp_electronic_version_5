import copy

import argparse
#process
#  locations set in working_parts.odsis 
#  export to working_parts.csvhe best letrence_ doside of the board
#  run this script

def main(**kwargs):
    import oomlout_roboclick
    import working_oomp

    #delete options
    run_delete = False
    run_delete = True
    filter_part_name = ""

    #run delete
    if run_delete:
        kwargs2 = copy.deepcopy(kwargs)
        filter_part_name = filter_part_name
        filters_to_run = []
        if True:
            pass
            #filters_to_run.append("all")
            #filters_to_run.append("regenerate_ai")
            filters_to_run.append("regenerate_corel")

        filters_within_directory = {}
        if True:        
            filters_within_directory["regenerate_ai"] = ["initial_generated.png", "initial_generated_trace.png"]
            filters_within_directory["regenerate_corel"] = ["label.png"]
        
        kwargs2["filters_to_run"] = filters_to_run
        kwargs2["filters_within_directory"] = filters_within_directory
        kwargs2["filter_part_name"] = filter_part_name
        import working_delete
        working_delete.main(**kwargs2)

    #run oomp creation
    if True:
        working_oomp.main(**kwargs)

    # Run the repository actions in deterministic directory order by default.
    # Callers can still opt into Roboclick's threaded runner explicitly.
    if True:
        run_kwargs = copy.deepcopy(kwargs)
        run_kwargs["directory"] = "parts"
        run_kwargs["mode"] = "all"
        run_kwargs.setdefault("recursive_threaded", False)
        run_kwargs.setdefault("threaded_subprocess_actions", False)
        oomlout_roboclick.run_folder_recursive(**run_kwargs)

    

if __name__ == '__main__':
    # parse arguments
    argparser = argparse.ArgumentParser(description='project description')
    #--file_input -fi
    argparser.add_argument('--file_input', '-fi', type=str, default='', help='file_input')    
    args = argparser.parse_args()
    kwargs = {}
    # update kwargs with args
    kwargs.update(vars(args))

    
    
    
    
    main(**kwargs)
