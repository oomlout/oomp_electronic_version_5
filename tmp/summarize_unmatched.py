import yaml
from collections import Counter

d = yaml.safe_load(open(r'C:/gh/oomp_electronic_version_5/report/unmatched_components.yaml'))
print(f"Total unmatched: {d['summary']['total_unmatched_components']}")
print(f"Projects with unmatched: {d['summary']['projects_with_unmatched']}")

reasons = Counter()
projects = Counter()
values = Counter()
footprints = Counter()
families = Counter()

for r in d['unmatched_components']:
    reasons.update(r['reasons'])
    projects.update([r['project_oomp_id']])
    values.update([r['value']])
    footprints.update([r['footprint']])
    families.update([r['footprint'].split(':')[0]])

print("\n--- Top reasons ---")
for k, v in reasons.most_common(20):
    print(f"  {k}: {v}")

print("\n--- Top projects ---")
for k, v in projects.most_common(20):
    print(f"  {k}: {v}")

print("\n--- Top values ---")
for k, v in values.most_common(40):
    print(f"  {k}: {v}")

print("\n--- Top footprints ---")
for k, v in footprints.most_common(40):
    print(f"  {k}: {v}")

print("\n--- Top families ---")
for k, v in families.most_common(40):
    print(f"  {k}: {v}")
