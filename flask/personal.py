import json
import sqlite3
from flask import Flask, render_template, request, url_for, request, jsonify
app=Flask(__name__)

@app.route("/")
def index():
   return render_template("personal.html")

@app.route('/createpersonal')
def createpersonal():
 print('a')
#if request.method=='POST':
 opersonal=request.get_json()

 print(opersonal)
 cn=sqlite3.connect('test.db')

 cu=cn.cursor
 types='table'
 name='personal'
 cn.execute("SELECT count(*) FROM sqlite_master WHERE type=? AND name=?",(types,name))
 co=cu.fetchall()
 if co>0:
  cn.execute('create table personal(name text,phone test)')

 cn.close()

 return jsonify("a")

@app.route('/addpersonal',methods=['POST','GET'])
def addpersonal():
#  if request.method=='POST':
  opersonal=request.get_json()

  print(opersonal)
  cn=sqlite3.connect('test.db')
  cu=cn.cursor
  name=opersonal['name']
  phone=opersonal['phone']
  cn.execute("insert into personal(name,phone)values(?,?)", (name, phone))
  cn.commit()
  cn.close()
  return jsonify("a")

@app.route("/getpersonal")
def getpersonal():
 if request.method=='GET':
  cn=sqlite3.connect('test.db')
  cu=cn.cursor
  cn.execute('select name,phone from personal')
  lpersonal=cu.fetchall()
  cn.close()
  return jsonify(lpersonal)

@app.route("/getpersonalcount",methods=['POST'])
def getpersonalcount():
 if request.method=='POST':
  cn=sqlite3.connect('test.db')
  cu=cn.cursor
  cn.execute('select count(*) from personal')
  co=cu.fetchall()
  cn.close()
  return jsonify(co)

@app.route("/getpersonalid")
def getpersonalid():
 if request.method=='GET':
  id = request.get_json()
  cn=sqlite3.connect('test.db')
  cu=cn.cursor
  cn.execute('select name,phone from personal where rowid='+id)
  opersonal=cu.fetchall()
  cn.close()
  return jsonify(opersonal)

@app.route('/changepersonal',methods=['POST','GET'])
def changepersonal():
 if request.method=='POST':
  personal=request.get_json()
  cn=sqlite3.connect('test.db')
  cu=cn.cursor
  cn.execute('update personal set name=personal.name,phone=personal.phone where rowid='+personal.id)
  cn.commit()
  cn.close()
  return jsonify("")

@app.route('/removepersonal',methods=['POST','GET'])
def removepersonal():
 if request.method=='POST':
  personal=request.get_json()
  cn=sqlite3.connect('test.db')
  cu=cn.cursor
  cn.execute('delete from personal where rowid='+personal.id)
  cn.commit()
  cn.close()
  return jsonify("")

if __name__=="__main__":
 app.run(debug=True)