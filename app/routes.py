from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello, from the Open Service Broker!"