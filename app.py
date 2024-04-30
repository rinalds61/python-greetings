from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    # Retrieve port from environment variable (can be named PORT)
    port = int(os.environ.get('PORT', 5000))  # Set default if not found
    app.run(host="0.0.0.0", debug=True, port=port)
