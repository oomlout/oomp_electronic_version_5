import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')

from pathlib import Path
from kicad_agents.kicad_library_agent import package_libraries

repo_root = Path(r'C:\gh\oomp_electronic_version_5')
package_libraries(repo_root / "parts", repo_root / "kicad_libraries")
print("KiCad libraries packaged")
