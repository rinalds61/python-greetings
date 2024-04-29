import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    port = 7001  # Set the port explicitly to 7001
    app.run(host="0.0.0.0", debug=True, port=port)
