from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Sagar@1192@localhost/database1'
db = SQLAlchemy(app)
class Customer(db.Model):

    cid=db.Column(db.Integer(),primary_key=True)
    cage=db.Column(db.Integer())
    cname=db.Column(db.String(100),nullable=False)
    id= db.relationship('Account', backref='custom', uselist=True, lazy=False)


class Account(db.Model):
    id= db.Column(db.Integer(), primary_key=True)
    abal= db.Column(db.Float())
    atype= db.Column(db.String(100), nullable=False)
    customer_id= db.Column(db.Integer(), db.ForeignKey('customer.id'), nullable=False, unique=True)


def drop_Table():
    db.drop_all()

def create_table():
    db.create_al

import time
if __name__ == '__main__':
    drop_Table()
    time.sleep(3)
    db.create_all()
    time.sleep(3)

    cust1 = Customer(cid=111, cname='Sagar', cage=27,)



    db.session.add(cust1)
    db.session.commit()



####using relationship



#########--------using foreign key
    #cust2 = Customer(cid=111, cname='Sagar', cage=27)
    #cust2.cac=22

    #db.session.add(cust2)
    #db.session.commit()
####------using backref_-----------
    #cust3 = Customer(cid=333, cname='Sagar', cage=27)
    #cust3.custom=ac3


    #db.session.add(cust3)
    #db.session.commit()






