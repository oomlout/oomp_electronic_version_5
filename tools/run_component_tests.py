"""Run component regressions while blocking access to the project checkout."""
from pathlib import Path
import os,sys
root=Path(__file__).resolve().parents[1]
forbidden=root.parent/'oomp_electronic_project_version_5'
sys.path.insert(0,str(root))
os.environ['PYTEST_DISABLE_PLUGIN_AUTOLOAD']='1'
def audit(event,args):
    if event in ('open','os.listdir','os.scandir') and args and isinstance(args[0],(str,bytes,os.PathLike)):
        path=Path(os.fsdecode(args[0])).resolve()
        if path.is_relative_to(forbidden):
            raise RuntimeError('Project checkout access forbidden: '+str(path))
sys.addaudithook(audit)
import pytest
raise SystemExit(pytest.main(sys.argv[1:] or ['-q','kicad_agents/tests']))
