from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return jsonify({"message": "Hello, world!"})

if __name__ == '__main__':
    app.run()
