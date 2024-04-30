from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    import argparse
    port = int(os.environ.get('PORT', 5000))
    # ... rest of the code for argument parsing or environment variable usage
    app.run(debug=True, host='0.0.0.0', port=port)
