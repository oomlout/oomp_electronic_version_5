import yaml, collections

data = yaml.safe_load(open('report/unmatched_components.yaml'))
counts = collections.Counter()
reasons = collections.Counter()
types = collections.Counter()
footprints = collections.Counter()
libs = collections.Counter()

for u in data['unmatched_components']:
    counts[u['project_oomp_id']] += 1
    reasons[tuple(u['reasons'])] += 1
    types[u['value']] += 1
    footprints[u['footprint']] += 1
    libs[u['library_id']] += 1

print("=== BY PROJECT ===")
for k, v in counts.most_common(20):
    print(f"  {k}: {v}")

print("\n=== BY REASON ===")
for k, v in reasons.most_common(10):
    print(f"  {k}: {v}")

print("\n=== BY VALUE (top 40) ===")
for k, v in types.most_common(40):
    print(f"  {k}: {v}")

print("\n=== BY FOOTPRINT (top 40) ===")
for k, v in footprints.most_common(40):
    print(f"  {k}: {v}")

print("\n=== BY LIBRARY (top 40) ===")
for k, v in libs.most_common(40):
    print(f"  {k}: {v}")
