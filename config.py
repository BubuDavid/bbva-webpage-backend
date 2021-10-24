from flask import Flask
from decouple import config

def create_app():
	app = Flask(__name__)

	app.secret_key = config('SECRET_KEY')

	return app