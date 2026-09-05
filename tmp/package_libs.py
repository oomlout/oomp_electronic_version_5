import sys
sys.path.insert(0, r'C:\gh\oomlout_roboclick')
sys.path.insert(0, r'C:\gh\oomlout_oomp_version_5')
sys.path.insert(0, r'C:\gh\oomp_electronic_version_5')

from kicad_agents.kicad_library_agent import package_libraries
r = package_libraries('parts', 'kicad_libraries')
print(r)
