from ..common import *

class some_example_endpoint(Resource):
	def get(self):
		return Response(status=200)