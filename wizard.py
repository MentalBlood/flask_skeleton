import argparse
import os

parser = argparse.ArgumentParser(description='Script to help create endpoints')
parser.add_argument('endpoint_name', type=str, nargs='+',
					help='Use name "root" to create "/" endpoint')
args = parser.parse_args()

for name in args.endpoints_names:
	if os.path.exists(f'endpoints/{name}'):
		print(f'directory for endpoint "{name}" already exists, skiping')
		continue
	os.mkdir(f'endpoints/{name}')
	with open(f'endpoints/{name}/main.py', 'w', encoding='utf8') as f:
		f.write('from ..common import *\n')
		f.write('\n')
		f.write(f'class {name}(Resource):\n')
		f.write(f'\tdef get(self):\n')
		f.write(f'\t\treturn Response(status=200)')