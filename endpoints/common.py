from flask_restful import Resource

def routedTo(urls, endpoint):
	def decorator(someClass):
		someClass.urls = urls
		someClass.endpoint = endpoint
		return someClass
	return decorator