import flask

app = flask.Flask(__name__)

@app.route('/')
def printHello():
        return "Hello"

if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True, port=8080)


