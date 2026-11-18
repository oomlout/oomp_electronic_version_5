import copy
import traceback
from datetime import datetime, timezone
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent
RUN_ERROR_LOG = REPOSITORY_ROOT / "report" / "errors_during_run.txt"


def _log_run_error(stage, error):
    RUN_ERROR_LOG.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    entry = [
        f"[{timestamp}] {stage}",
        f"Error type: {type(error).__name__}",
        f"Error message: {error}",
        "Traceback:",
        traceback.format_exc(),
        "",
    ]
    with RUN_ERROR_LOG.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(entry))

def main(**kwargs):
    run_oomp_populate = kwargs.get("run_oomp_populate", True)
    #run_oomp_populate = False
    kwargs["run_oomp_populate"] = run_oomp_populate

    run_oomp = kwargs.get("run_oomp", True)
    #run_oomp = False
    kwargs["run_oomp"] = run_oomp

    run_scad = kwargs.get("run_scad", True)
    #run_scad = False
    kwargs["run_scad"] = run_scad

    run_action = kwargs.get("run_action", True)
    #run_action = False
    kwargs["run_action"] = run_action

    generate_stl = kwargs.get("generate_stl", False)
    #generate_stl = True
    kwargs["generate_stl"] = generate_stl

    run(**kwargs)

def run(**kwargs):


    kwargs_2 = copy.deepcopy(kwargs)
    #pop run and generate variables from kwargs
    pop_values = ["run_oomp_populate", "run_oomp", "run_scad", "run_action", "generate_stl", "run_svg"]
    for key in pop_values:
        kwargs_2.pop(key, None)


    if kwargs.get("run_oomp_populate", False):
        try:
            import working_oomp_populate
            working_oomp_populate.main(**kwargs_2)
        except Exception as error:
            _log_run_error("working_oomp_populate", error)
            raise

    if kwargs.get("run_oomp", False):
        try:
            import working_oomp
            working_oomp.main(**kwargs_2)
        except Exception as error:
            _log_run_error("working_oomp", error)
            raise

    if kwargs.get("run_scad", False):        
        try:
            kwargs2 = copy.deepcopy(kwargs_2)
            if kwargs.get("generate_stl", False):
                kwargs2["typ"] = "all"
            import working_scad
            working_scad.main(**kwargs2)
        except Exception as error:
            _log_run_error("working_scad", error)
            raise

    #add run_svg
    if kwargs.get("run_svg", False):        
        try:
            import working_svg
            working_svg.main(**kwargs_2)
        except Exception as error:
            _log_run_error("working_svg", error)
            raise


    if kwargs.get("run_action", False):
        try:
            import working_action
            working_action.main(**kwargs_2)
        except Exception as error:
            _log_run_error("working_action", error)
            raise




if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)