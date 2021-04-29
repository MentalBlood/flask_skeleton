from ..common import *

class root(Resource):
	def get(self):
		return Response(status=200)