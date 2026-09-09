import copy

import argparse
#process
#  locations set in working_parts.odsis 
#  export to working_parts.csvhe best letrence_ doside of the board
#  run this script

def main(**kwargs):
    import oomlout_roboclick
    import working_oomp

    kwargs.setdefault("threaded_workers", 6)
    

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

    # Load every real Roboclick mode before starting the worker pool.  The
    # legacy "ai" name is historical: this repository's normal actions are
    # deterministic Python, image-resize, file-copy, and Jinja jobs.
    if True:
        run_kwargs = copy.deepcopy(kwargs)
        run_kwargs["directory"] = "parts"
        run_kwargs["mode"] = "all"
        run_kwargs["recursive_threaded"] = True
        run_kwargs["threaded_subprocess_actions"] = True
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
