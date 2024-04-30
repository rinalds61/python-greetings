import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    # Set the PORT environment variable within the script
    os.environ['PORT'] = '7002'
    
    # Now the Flask app will use the port specified in the PORT environment variable
    port = int(os.environ.get('PORT', 7001))  # Get port from environment variable, defaulting to 7001
    app.run(host="0.0.0.0", debug=True, port=port)
