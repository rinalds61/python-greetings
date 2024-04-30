import argparse

app = Flask(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=5000, type=int, help='Port to run the server on.')
    args = parser.parse_args()

    app.run(debug=True, host='0.0.0.0', port=args.port)
