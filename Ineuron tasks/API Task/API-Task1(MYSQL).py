import mysql.connector as conn
from flask import Flask,request, jsonify



app = Flask(__name__)

@app.route('/sqldatabase',methods=['GET','POST'])
def Showdata():
    if(request.method == 'POST'):
       mydb = conn.connect(host='localhost',user='root',passwd='SaiKrishna@151')
       cs= mydb.cursor()
       cs.execute("use krishna")
       cs.execute("select * from sai")
    return jsonify(str(cs.fetchall()))


if __name__ == '__main__':
    app.run()