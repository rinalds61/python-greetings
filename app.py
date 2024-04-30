from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    port1 = process.env.PORT
    app.run(host="0.0.0.0", debug=True, port=port1)
