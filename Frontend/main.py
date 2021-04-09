from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, logout_user, login_required

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



@app.route('/')
def index():
    return render_template("index.html")
@app.route('/login.html')
def login():
    return render_template("login.html")
@app.route('/signup.html')
def signup():
    return render_template("signup.html")

@app.route('/submit', methods=['POST'])
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
            return render_template("list.html")

@app.route('/login', methods=['POST'])
def log():
    email = request.form.get('email')
    psd = request.form.get('psd')
    user = Signupd.query.filter_by(email=email, psd=psd).first()
    if not user:
        return render_template("signup.html")
    
    return render_template("list.html")

if __name__=='__main__':
    app.run(debug=True)
    