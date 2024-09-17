from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Ajay, Test-1 app !\n office'


if __name__ == '__main__':
    # Change the port to your desired port number
    port = 8082
    app.run(host='0.0.0.0', port=port)
