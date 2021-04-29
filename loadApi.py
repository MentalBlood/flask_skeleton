import os
import inspect
from flask_restful import Api

def getClasses(pathAsList):
	pathString = '.'.join(pathAsList)
	module = __import__(pathString)
	moduleItself = module
	for submodule in pathAsList[1:]:
		moduleItself = getattr(moduleItself, submodule)
	return [m[1] for m in inspect.getmembers(moduleItself, inspect.isclass) if m[1].__module__ == pathString]

def loadApi(app, api_prefix, endpoints_dir):
	api = Api(app, prefix=api_prefix)
	endpoints_dirs = os.listdir(endpoints_dir)
	for ep_d in endpoints_dirs:
		ep_d_full_path = endpoints_dir + '/' + ep_d
		if (not os.path.isdir(ep_d_full_path)) or (ep_d == '__pycache__'):
			continue
		endpoint_real_name = api_prefix + '/' + ('' if ep_d == 'root' else ep_d)
		module_path_as_list = [endpoints_dir, ep_d, 'main']
		resources = getClasses(module_path_as_list)
		for r in resources:
			api.add_resource(r, *r.urls, endpoint=endpoint_real_name)