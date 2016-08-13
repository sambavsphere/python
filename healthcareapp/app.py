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

@app.route('/symptomevaluation',methods=['GET','POST'])
def symptomevaluation():
	symptoms =""
	message = ""
	evaluated_diseases=""
	con = connect()
	cur = con.cursor()
	cur.execute("select symptoms from dieseases")
	l=cur.fetchall()
	s=""
	for i in l:
	    s=s+","+i[0]
	l1=s.split(',')
	l2=set(l1)
	symptoms = [i.strip() for i in l2]
	if request.method=="POST":
		selected_symptoms=[]
		for s_symptom in request.form.iteritems():
			selected_symptoms.append(s_symptom[1])
		evaluated_diseases=[]
		for symp in selected_symptoms:
			query = "select dieseasename from dieseases where symptoms like '%{0}%'".format(symp)
			cur.execute(query)
			diseases=cur.fetchall()
			for i in diseases:
				evaluated_diseases.append(i[0])



	return render_template('symptomevaluation.html',message=message,symptoms=symptoms,evaluated_diseases=set(evaluated_diseases))


@app.route('/diseasereg',methods=['POST','GET'])
def diseasereg():
	message=""
	if request.method=="POST":
		con = connect()
		cur=con.cursor()
		cur.execute('select max(id) from dieseases')
		max_id = cur.fetchone()[0] 
		if max_id:
			max_id = max_id+1
		else:
			max_id=1
		values={
		'id':max_id,
		'disease':request.form['disease'],
		'symptoms':request.form['symptoms'],
		}
		query = "insert into dieseases values(%(id)s,'%(disease)s','%(symptoms)s')"%values
		con.execute(query)
		con.commit()
		disconnect(con)
		message = "disease registered sucessfully"
	return render_template("diseasereg.html",message=message)

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
	
	#inserting into disease database

app.run(debug=True)

