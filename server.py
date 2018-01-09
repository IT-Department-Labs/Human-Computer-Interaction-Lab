from gevent.pywsgi import WSGIServer
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Set server address 127.0.0.1:5000/
    app.run(host="0.0.0.0", port=5000, debug=True)
    http_server = WSGIServer(app)
    http_server.serve_forever()