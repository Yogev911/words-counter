from flask import Flask
app = Flask(__name__)
from flask import jsonify

@app.route('/')
def hello():
    return jsonify({"st": "Invalid emailsefge nsefkgj jnsfgjn ajg 4j nsa jrg"}), 200

if __name__ == '__main__':
    app.run(port=8080)