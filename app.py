from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
#from werkzeug import secure_filename


app=Flask(__name__)
#engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
#app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:sm00th1y!@localhost/order_collector'
app.config['SQLALCHEMY_DATABASE_URI']='postgres://kfdqilbhbkibkr:abe29e535db1e9638e241b0b13d235ecb226b1589dce171caca9e3b0d1dd4028@ec2-35-168-77-215.compute-1.amazonaws.com:5432/d61lqlabdov8e0?sslmode=require'
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
       # if db.session.query(Data).filter(Data.email_ == email).count()== 0:
         data=Data(email,product,quant)
         db.session.add(data)
         db.session.commit()
         return render_template("success.html")



        #average_height=db.session.query(func.avg(Data.height_)).scalar()
        #average_height=round(average_height, 1)
       # count = db.session.query(Data.height_).count()
       
        #print(average_height)
        
    #return render_template('index.html', text="Seems like we got something from that email once!")



@app.route("/download")
def download():
    return send_file("uploaded"+file.filename, attachment_filename="yourfile.csv", as_attachment=True)


if __name__ == '__main__':
    app.debug=True
    app.run()