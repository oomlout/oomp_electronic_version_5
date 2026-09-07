import yaml, sys
for path in sys.argv[1:]:
    d = yaml.safe_load(open(path))
    print(path.split('/')[-2])
    print(d.get('package_drawing', 'NOT FOUND'))
    print('---')
