import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3001))  # Get port from environment variable, defaulting to 3000
    app.run(host="0.0.0.0", debug=True, port=port)
