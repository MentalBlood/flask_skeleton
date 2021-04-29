from ..common import *

@routedTo(['/add_message'], 'add_message')
class root(Resource):
	def get(self):
		return Response(status=200)