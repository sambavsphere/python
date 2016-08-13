from flask import Flask,render_template,request
app = Flask(__name__)
import sqlite3
def connect():
	con = sqlite3.connect('healthcare.db')
	return con
def disconnect(con):
	con.close()

# @app.route('/')
# def fun():
# 	return "hello world"

# @app.route('/init')
# def fun1():
# 	return "<h1>hello world</h1>"
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/login',methods=['POST','GET'])
def login():
	message=""
	if request.method=="POST":
		query = "select count(*) from users where username='%(username)s' and password='%(password)s'"%request.form
		con = connect()
		cur = con.cursor()
		cur.execute(query)
		number_of_users = cur.fetchone()[0]
		if number_of_users>=1:
			message = "Login successful"
		else:
			message = "Login failed"
	return render_template('login.html',message=message)

@app.route('/registration', methods=['POST','GET'])
def registrtation():
	message = ""
	if request.method=="POST":
		try:
			con = connect()
			cur = con.cursor()
			cur.execute('select max(id) from users')
			max_id = cur.fetchone()[0]+1
			values = {
			'username':request.form['username'],
			'password':request.form['password'],
			'id':max_id
			}
			query = "insert into users values('%(id)s','%(username)s','%(password)s')"%values
			con.execute(query)
			con.commit()
			disconnect(con)
			message = "user registered succesfully"
		except Exception as err:
			message=str(err)
	return render_template("registration.html",message=message)

app.run(debug=True)