from flask import Flask
from connector import Connector
app = Flask(__name__)
connector = Connector()

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/test_query/')
def test_query():
	return connector.execute_query('input_sql.txt')
