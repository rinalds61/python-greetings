from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greetings')
def greetings():
    return jsonify({"greeting": "Hello from Python App!"})

if __name__ == '__main__':
    import argparse
    port1 = int(os.environ.get('PORT', 5000))
   # parser = argparse.ArgumentParser()
    #parser.add_argument('--port', default=5000, type=int, help='Port to run the server on.')
    #args = parser.parse_args()
    
    app.run(debug=True, host='0.0.0.0', port=port1)
