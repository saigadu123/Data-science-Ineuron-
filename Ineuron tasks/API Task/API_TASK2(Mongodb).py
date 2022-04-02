from flask import Flask,request,jsonify
import mysql.connector as conn
import pymongo

app = Flask(__name__)

@app.route('///abc/def',methods=['POST'])
def showdata1():
    if(request.method=='POST'):
        client = pymongo.MongoClient(
              "mongodb+srv://saikrishna:saikrishna@cluster0.cozy6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",
              tls=True, tlsAllowInvalidCertificates=True)
        db = client.test
        coll1 = db.sai

    return jsonify(str([i for i in coll1.find()]))


if __name__ == '__main__':
    app.run()

