from flask import Flask, render_template,url_for;
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime;


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tesr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)


class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)



  #function to return task id  
    def __repr__(self) -> str:
        return '<Task %r>' % self.id
    


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/base')
def base():
    return render_template('base.html')





if __name__== "__main__" :
 
    app.run (debug=True)

