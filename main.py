from flask import Flask, request
from flask_restful import Api

from loadApi import loadApi

app = Flask(__name__)
api = Api(app)

loadApi(
	app=app,
	api_prefix='/test',
	endpoints_dir='endpoints'
)

if __name__ == '__main__':
	app.run('10.1.13.136', port=8001)