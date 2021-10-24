from api_functions import consume_api
from flask_cors import CORS

from config import create_app

from flask import render_template

app = create_app()
CORS(app)


countries = {
	"spain": {
		"display_name":"España",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1ea-1f1f8.png",
		"name":"spain"
	},
	"mexico": {
		"display_name":"México",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1f2-1f1fd.png",
		"name":"mexico"
	},
	"peru": {
		"display_name":"Perú",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1f5-1f1ea.png",
		"name":"peru"
	},
	"argentina":{
		"display_name":"Argentina",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1e6-1f1f7.png",
		"name":"argentina"
	},
	"colombia":{
		"display_name":"Colombia",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1e8-1f1f4.png",
		"name":"colombia"
	}
}

priorities = {
	'Mejorar la salud financiera de los clientes',
	'Ayudar a los clientes en la transición hacia un futuro sostenible',
	'Crecer en clientes',
	'Buscar la excelencia operativa'
}

@app.route('/')
def index():
	return render_template('pages/index.html', countries=countries)

@app.route('/select_priority/<country_name>')
def select_priority(country_name):
	endpoint = f'base_link/{country_name}'
	context = {
		"country": countries[country_name],
		"priorities": priorities
	}
	return render_template('pages/select_priority.html', **context)

@app.route('/country/<country_name>/<priority>')
def country_view(country_name, priority):

	context = {
		"country": countries['mexico'],
		"priority": 'Buscar la excelencia operativa'
	}
	
	return render_template('pages/country_view.html', **context)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888, debug=True)
 