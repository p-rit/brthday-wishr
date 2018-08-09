from flask import Flask , render_template ,request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_email
from datetime import datetime as dt
from threading import Thread


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://uhwuyiiqxssiyr:4cea753d4f4082c6b9ad665421ff30a8f0a0c4fd15658d029f4f12f64c325104@ec2-54-227-241-179.compute-1.amazonaws.com:5432/de8pks67p4gpeg?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
	__tablename__ = "data"
	id = db.Column(db.Integer , primary_key = True)
	email = db.Column(db.String(100),unique=False)	
	date = db.Column(db.Date)
	name = db.Column(db.String)

	def __init__(self,email,date,name):
    		self.email = email
    		self.date = date
    		self.name = name

	
@app.route("/")
def home():
		
		return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
	if request.method=='POST':
		mail = request.form['email_name']
		dob = request.form['dob_name']
		name = request.form['name']
		if db.session.query(Data).filter(Data.email==mail).count()==0:
				data = Data(mail,dob,name)
				db.session.add(data)
				db.session.commit()
				thr = Thread(target = wish,args=[mail,dob,name])
				thr.start()
           
				return render_template("success.html")
		return render_template("index.html" , text ='Seems we have get already from that email address!')

def wish(mail,dob,name):
	while  True:
		d = db.session.query(Data.id).all()
		if d != None:
			for id_ in d:
				date_ = db.session.query(Data.date).filter(Data.id == id_[0]).scalar()
				
				if date_.year==dt.now().year and date_.month ==dt.now().month and date_.day ==dt.now().day and dt.now().hour== 0 and dt.now().minute == 0 and dt.now().second ==0:
					name = db.session.query(Data.name).filter(Data.id==id_[0]).scalar()
					mail = db.session.query(Data.email).filter(Data.id==id_[0]).scalar()
					send_email(mail,name)
					
					

if __name__ =="__main__":
	app.run(debug=True)