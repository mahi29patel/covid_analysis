from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required
import csv
import numpy as np
import string
import re
import pandas as pd
import random
import time

# Python3 code to remove whitespace
def remove(string):
    return string.replace(" ", "")
      

app=Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/coviddb'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#----------------------------------------------------------------------------#
class Signupd(db.Model):
    __tablename__ = 'signup'
    email = db.Column(db.String(50), primary_key=True)
    hname = db.Column(db.String(50), unique=True)
    psd = db.Column(db.String(50))
    cpsd = db.Column(db.String(50))
   

    def __init__(self, email, hname, psd, cpsd):
        self.email = email
        self.hname = hname
        self.psd = psd
        self.cpsd = cpsd

#----------------------------------------------------------------------------#

@app.route('/')
def index():
    return render_template("index.html")
  
@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/signup.html')
def signup():
    return render_template("signup.html")

@app.route('/sensor.html')
def sensor():
    return render_template("sensor.html")

#-------------------------------LOADING DATA---------------------------------------------#
headings= ("Patient ID","Name", "Room no.", "Doctor name", "Date of admit", "Severity")

with open('Frontend\hospital_data.csv') as f:
    l = list(csv.reader(f, delimiter=","))

data = np.array(l[1:])
@app.route('/list.html')
def table():
    return render_template("list.html", headings=headings, data=data)

#------------------------------------SIGN UP----------------------------------------#

@app.route('/login.html', methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form['email']
        hname = request.form['hname']
        psd = request.form['psd']
        cpsd = request.form['cpsd']
        # print(customer, dealer, rating, comments)
        if email=='' or psd=='':
            return render_template("signup.html")
        #print(email, psd)
        if db.session.query(Signupd).filter(Signupd.email == email).count() == 0:
            data = Signupd(email, hname, psd, cpsd)
            db.session.add(data)
            db.session.commit()
            return render_template("login.html")

#-----------------------------------LOGIN-----------------------------------------#

@app.route('/login', methods=['POST'])
def log():
    email = request.form.get('email')
    psd = request.form.get('psd')
    user = Signupd.query.filter_by(email=email, psd=psd).first()
    if not user:
        return render_template("signup.html")
    else:
        return render_template("list.html", headings=headings, data=data)



@app.route('/sensor',methods = ['POST', 'GET'])
def result():
   result = request.form.get('patient')
   print(remove(result))
   res1= int(re.sub('\D', '', result))
   print(res1)
   
   headings1= ("Patient ID","Age", "SpO2", "Temperature", "HeartRate", "RespiratoryRate")
   df2 = pd.read_csv('Frontend\patients_data.csv')
   data1=df2.loc[df2['PatientID'] == res1].to_numpy()
   return render_template("sensor.html", headings=headings1, data=data1)

if __name__=='__main__':
    app.run(debug=True)
 

var = 1
while var == 1 :
    df1 = pd.read_csv('Frontend\hospital_data.csv')
    df1 = df1.sort_values(by = 'PatientID')
    #print(df1.head())
    #print("Mahi")
    df = pd.read_csv('Frontend\patients_data.csv')
    #print(df.head())

    length= len(df.index)
    #print(length)

    for i in range(length):
        df.loc[i, 'SpO2']=float(random.randrange(800, 1000))/10
        df.loc[i, 'Temperature']=float(random.randrange(9900, 10500))/100
        df.loc[i, 'HeartRate']=random.randint(70,110)
        df.loc[i, 'RespiratoryRate']=random.randint(14,30)


    print(df.head())


    for i in range (length):

        if df.SpO2[i]<90:
            s='Extremely Severe'
        elif df.Temperature[i]>104:
            s='Extremely Severe'
        elif df.HeartRate[i]>110:
            s='Extremely Severe'
        elif df.RespiratoryRate[i]>25:
            s='Extremely Severe'

        elif df.Temperature[i]>100.4 and df.HeartRate[i]>100:
            s= 'Moderately Severe'
        elif df.Temperature[i]>100.4 and df.SpO2[i]>=90 and df.SpO2[i]<=92:
            s= 'Moderately Severe'
        elif df.RespiratoryRate[i]>22 and df.SpO2[i]>=90 and df.SpO2[i]<=92:
            s= 'Moderately Severe'
        elif df.Age[i]>60 and (df.HeartRate[i]>100 or (df.SpO2[i]>=90 and df.SpO2[i]<=92) or df.RespiratoryRate[i]>22 or df.Temperature[i]>100.4):
            s= 'Moderately Severe'
        elif df.SpO2[i]>=90 and df.SpO2[i]<=92 and df.HeartRate[i]>100:
            s= 'Moderately Severe'

        else:
            s= 'Normal'

        df1.loc[i, 'Severity'] = s
        df1 = df1.sort_values(by = 'Severity')
        df1.to_csv('Frontend\hospital_data.csv', index=False)
        df.to_csv('Frontend\patients_data.csv', index=False)

    #df1.to_csv('Frontend\hosp_data.csv', index=False)
    with open('Frontend\hospital_data.csv') as f:
        l = list(csv.reader(f, delimiter=","))

    data = np.array(l[1:])

    df2 = pd.read_csv('Frontend\patients_data.csv')
    #print(df1)
    #print(df2)
    
    time.sleep(30)

   
