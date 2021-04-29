from ..common import *

@routedTo(['/some_example_endpoint'], 'some_example_endpoint')
class root(Resource):
	def get(self):
		return Response(status=200)