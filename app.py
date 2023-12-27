import os
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/contact", methods=["POST"])
def review_post():
        name_receive = request.form['name_give']
        email_receive = request.form['email_give']
        messages_receive = request.form['messages_give']

        doc = {
            'name' : name_receive,
            'email':email_receive,
            'message' : messages_receive 
        }
        db.contact_coffe.insert_one(doc)
        return jsonify({'msg':'POST request'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
