from api_functions import consume_api
from flask_cors import CORS

from config import create_app

from flask import render_template

app = create_app()
CORS(app)


countries = [
	{
		"display_name":"España",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1ea-1f1f8.png",
		"name":"spain"
	},
	{
		"display_name":"México",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1f2-1f1fd.png",
		"name":"mexico"
	},
	{
		"display_name":"Perú",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1f5-1f1ea.png",
		"name":"peru"
	},
	{
		"display_name":"Argentina",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1e6-1f1f7.png",
		"name":"argentina"
	},
	{
		"display_name":"Colombia",
		"flag":"https://images.emojiterra.com/google/noto-emoji/unicode-13.1/128px/1f1e8-1f1f4.png",
		"name":"colombia"
	}
]

@app.route('/')
def index():
	return render_template('pages/index.html', countries=countries)

@app.route('/country/<country_name>')
def method_name(country_name):
	endpoint = f'base_link/{country_name}'
	data = consume_api(endpoint)
	return render_template('pages/country_view.html', data=data)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888, debug=True)
 