from flask import Flask, render_template, request ,jsonify
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


import urllib.parse
# from pymongo import MongoClient, ServerApi

username = "udhayaprof"
password = urllib.parse.quote_plus("udhaya@2004@")  # This will automatically encode the special characters
uri = f"mongodb+srv://{username}:{password}@cluster0.xpfyl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))



# uri = "mongodb+srv://udhayaprof:<udhaya@2004@>@cluster0.xpfyl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db=client.eventify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/msgsent" , methods=["post"])
def sentmsg():
    name=request.form["name"]
    email=request.form["email"]
    phonenumber=request.form["phonenumber"]
    message=request.form["message"]
    data={"name":name,"email":email,"phone__number":phonenumber,"message":message}
    print(data)
    db.events.insert_one(data)

    return jsonify({'msg': 'Event details added successfully'})


if __name__ == '__main__':
    app.run(debug=True)
 