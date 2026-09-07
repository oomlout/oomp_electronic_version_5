import yaml, os, glob

files = glob.glob(r'C:\gh\oomp_electronic_version_5\parts\oomp_project_*\data\generated_data\unmatched_parts.yaml')
totals = []
for f in files:
    data = yaml.safe_load(open(f, encoding='utf-8')) or {}
    project = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(f))))
    count = len(data.get('components', []))
    totals.append((project, count))

for project, count in sorted(totals, key=lambda x: -x[1])[:20]:
    print(f"{count:4d}  {project}")

print(f"\nTotal projects with unmatched: {sum(1 for _, c in totals if c > 0)}")
print(f"Total unmatched components: {sum(c for _, c in totals)}")
