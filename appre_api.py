from flask import Flask, jsonify
import json
import random
import apprentice_data

app = Flask(__name__)

@app.route('/')
def home():
    data = apprentice_data.get_data()
    return data
if __name__ == '__main__':
    app.run(debug=True)