from ..common import *

@routedTo(['/'], '')
class root(Resource):
	def get(self):
		return Response(status=200)