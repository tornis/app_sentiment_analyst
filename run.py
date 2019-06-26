from flask import Flask , jsonify, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')

def index():
	return '<h3>Para usar a API basta fazer a chamada da seguinte forma:</h3><p>http://127.0.0.1:5000/api/v1/sentiment/texto_a_ser_analizado</p><b><p>Exemplo:</p></b><a href="http://127.0.0.1:5000/api/v1/sentiment/Olá Mundo">http://127.0.0.1:5000/api/v1/sentiment/Olá Mundo</a>'

@app.route('/api/v1/sentiment', methods = ['POST', 'GET'])
def sentiment():
	message = request.args.get('message')
	text = TextBlob(message)
	if text.detect_language() != 'en':
		traduz = TextBlob(str(text.translate(to='en')))

	response = {'polarity' : traduz.polarity , 'subjectivity' : traduz.subjectivity }
	return jsonify(response)

if __name__ == "__main__":
	app.run(debug=True)

