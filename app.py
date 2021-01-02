from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
#from send_email import send_email
from sqlalchemy.sql import func
#from werkzeug import secure_filename


app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:sm00th1y!@localhost/order_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://lgigskweroooiu:1e48d154ed70f7ebfc32962330bcf96940fbccfe931fb8697870bc52ba0d82b7@ec2-52-204-20-42.compute-1.amazonaws.com:5432/da9uvl2gj8vicn?sslmode=require'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__="data"
    id =db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=False)
    product_=db.Column(db.Integer)
    quant_=db.Column(db.Integer)

    def __init__(self, email_, product_, quant_):
        self.email_=email_
        self.product_=product_
        self.quant_= quant_

@app.route("/")   
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    #global file
    if request.method=='POST':
         email=request.form["email_name"]
         product=request.form["product_name"]
         quant=request.form["product_quantity"]
         send_email(email, product, quant)
         print(email, product, quant)
       
         #data=Data(email,product,quant)
         #db.session.add(data)
         #db.session.commit()
         return render_template("success.html")



        #average_height=db.session.query(func.avg(Data.height_)).scalar()
        #average_height=round(average_height, 1)
       # count = db.session.query(Data.height_).count()
       
        #print(average_height)
        
    #return render_template('index.html', text="Seems like we got something from that email once!")



#@app.route("/download")
#def download():
    #return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug=True
    app.run(port=5000)