from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect
import random
import qrcode
import os
from PIL import Image

app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///login.db"
app.config['SQLALCHEMY_BINDS'] = {
'token_customer' : 'sqlite:///customer token.db', 
'card_customer' : 'sqlite:///customer card.db', 
'attendance' : 'sqlite:///attendance.db', 
'salary' : 'sqlite:///salary.db',
'token_employee' : 'sqlite:///employee token.db', 
'card_employee' : 'sqlite:///employee card.db',
'token_admin' : 'sqlite:///admin token.db', 
'feedback' : 'sqlite:///feedback.db', 
'card_admin' : 'sqlite:///admin card.db'
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



class Feedback(db.Model):
    __bind_key__ = "feedback"
    SNo = db.Column(db.Integer, primary_key=True)
    Feedback = db.Column(db.String(100), nullable=False)
    Date_given = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Feedback} - {self.Date_given}"


class login_details(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(100), nullable=False)
    Last_Name = db.Column(db.String(100), nullable=False)
    Username = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    Gender = db.Column(db.String(20), nullable=False)
    Designation = db.Column(db.String(20), nullable=False)
    Date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.First_Name} - {self.Last_Name} - {self.Username} - {self.Password} - {self.Address} - {self.Gender} - {self.Designation} - {self.Date_created}"


class employee_token_details(db.Model):
    __bind_key__ = 'token_employee'
    SNo = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Order_ID = db.Column(db.String(10), nullable=False)
    Initial = db.Column(db.String(100), nullable=False)
    Final = db.Column(db.String(100), nullable=False)
    Date_requested = db.Column(db.DateTime, default=datetime.utcnow)

    Designation = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Username} - {self.DOB} - {self.Address} - {self.City} - {self.Order_ID} - {self.Initial} - {self.Final} - {self.Date_requested} - {self.Designation}"


class employee_card_details(db.Model):
    __bind_key__ = 'card_employee'
    SNo = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    Order_ID = db.Column(db.String(10), nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Amount = db.Column(db.String(100), nullable=False)
    Date_requested = db.Column(db.DateTime, default=datetime.utcnow)

    Designation = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Username} - {self.DOB} - {self.Address} - {self.Order_ID} - {self.City} - {self.Initial} - {self.Final} - {self.Date_requested} - {self.Designation}"
class admin_token_details(db.Model):
    __bind_key__ = 'token_admin'
    SNo = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Order_ID = db.Column(db.String(10), nullable=False)
    Initial = db.Column(db.String(100), nullable=False)
    Final = db.Column(db.String(100), nullable=False)
    Date_requested = db.Column(db.DateTime, default=datetime.utcnow)

    Designation = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Username} - {self.DOB} - {self.Address} - {self.City} - {self.Order_ID} - {self.Initial} - {self.Final} - {self.Date_requested} - {self.Designation}"


class admin_card_details(db.Model):
    __bind_key__ = 'card_admin'
    SNo = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    Order_ID = db.Column(db.String(10), nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Amount = db.Column(db.String(100), nullable=False)
    Date_requested = db.Column(db.DateTime, default=datetime.utcnow)

    Designation = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Username} - {self.DOB} - {self.Address} - {self.Order_ID} - {self.City} - {self.Initial} - {self.Final} - {self.Date_requested} - {self.Designation}"
class customer_token_details(db.Model):
    __bind_key__ = 'token_customer'
    SNo = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Order_ID = db.Column(db.String(10), nullable=False)
    Initial = db.Column(db.String(100), nullable=False)
    Final = db.Column(db.String(100), nullable=False)
    Date_requested = db.Column(db.DateTime, default=datetime.utcnow)

    Designation = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Username} - {self.DOB} - {self.Address} - {self.City} - {self.Order_ID} - {self.Initial} - {self.Final} - {self.Date_requested} - {self.Designation}"


class customer_card_details(db.Model):
    __bind_key__ = 'card_customer'
    SNo = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    Order_ID = db.Column(db.String(10), nullable=False)
    City = db.Column(db.String(100), nullable=False)
    Amount = db.Column(db.String(100), nullable=False)
    Date_requested = db.Column(db.DateTime, default=datetime.utcnow)

    Designation = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Username} - {self.DOB} - {self.Address} - {self.Order_ID} - {self.City} - {self.Initial} - {self.Final} - {self.Date_requested} - {self.Designation}"


class attendance(db.Model):
    __bind_key__ = 'attendance'
    SNo = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    Dept_Name = db.Column(db.String(100), nullable=False)
    Dept_ID = db.Column(db.String(100), nullable=False)
    Emp_ID = db.Column(db.String(100), nullable=False)
    Date = db.Column(db.String(100), nullable=False)
    Day = db.Column(db.String(20), nullable=False)
    Designation = db.Column(db.String(20), nullable=False)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Username} - {self.DOB} - {self.Dept_Name} - {self.Dept_ID} - {self.Emp_ID} - {self.Date} - {self.Day} - {self.Designation}"

class salary(db.Model):
    __bind_key__ = 'salary'
    SNo = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    DOB = db.Column(db.String(100), nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    Dept_Name = db.Column(db.String(100), nullable=False)
    Dept_ID = db.Column(db.String(100), nullable=False)
    Emp_ID = db.Column(db.String(100), nullable=False)
    Amount_Paid = db.Column(db.String(100), nullable=False)
    Date = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"{self.SNo} - {self.Username} - {self.DOB} - {self.Dept_Name} - {self.Dept_ID} - {self.Emp_ID} - {self.Amount_Paid} - {self.Date}"




@app.route("/about")
def about():
    return render_template("about.html")



@app.route("/rate", methods=['GET','POST'])
def rate():
    if request.method == 'POST':
        feedback = request.form['feedback']
        feed = Feedback(Feedback=feedback)
        db.session.add(feed)
        db.session.commit()

    return render_template("rate.html")

@app.route("/", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        q = login_details.query.all()
        if len(q)==0:
            f_name = request.form['fname']
            l_name = request.form['lname']
            u_name = request.form['uname']
            pswd = request.form['pass']
            addr = request.form['add']
            gen = request.form['gender']
            desg = request.form['desig']
            test = login_details(First_Name=f_name,Last_Name=l_name,Username=u_name,Password=pswd,Address=addr,Gender=gen,Designation=desg)
            db.session.add(test)
            db.session.commit()
            if desg == "customer":
                return render_template("c/index.html",username=u_name)
            if desg == "employee":
                return render_template("e/index.html",username=u_name)
            if desg == "admin":
                return render_template("a/index.html",username=u_name)
        elif len(q)!=0:
            f_name = request.form['fname']
            l_name = request.form['lname']
            u_name = request.form['uname']
            pswd = request.form['pass']
            addr = request.form['add']
            gen = request.form['gender']
            desg = request.form['desig']
            conf = login_details.query.filter_by(Username=u_name).first()
            conf1 = login_details.query.filter_by(First_Name=f_name,Last_Name=l_name,Username=u_name,Password=pswd, Designation=desg).first()
            if conf is None:
                test = login_details(First_Name=f_name,Last_Name=l_name,Username=u_name,Password=pswd,Address=addr,Gender=gen,Designation=desg)
                db.session.add(test)
                db.session.commit()
                if desg == "customer":
                    return render_template("c/index.html",username=u_name)
                elif desg == "employee":
                    return render_template("e/index.html",username=u_name)
                elif desg == "admin":
                    return render_template("a/index.html",username=u_name)
            elif conf1 is not None:
                if desg == "customer":
                    return render_template("c/index.html",username=u_name)
                elif desg == "employee":
                    return render_template("e/index.html",username=u_name)
                elif desg == "admin":
                    return render_template("a/index.html",username=u_name)
                
                return redirect("/")

            
    return render_template('index.html')


            
        
            

@app.route("/c/home", methods=['GET','POST'])
def c_home():
    return render_template("c/index.html")

@app.route("/c/delete_token/<int:SNo>")
def c_delete_token(SNo):
    delete = customer_token_details.query.filter_by(SNo=SNo,Username=u__name).first()
    db.session.delete(delete)
    db.session.commit()
   
    return redirect('/c/actions')

@app.route("/c/delete_card/<int:SNo>")
def c_delete_card(SNo):
    delete = customer_card_details.query.filter_by(SNo=SNo,Username=u__name).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect('/c/actions')

@app.route("/c/token", methods=['GET','POST'])
def c_token():
    if request.method == 'POST':
        if os.path.isfile('qr.png') is True:
            os.remove('qr.png')
        else:
            global ic
            import random as r
            alphaChars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
            randChars = []
            charCount = 6
            for a in range(charCount):
                randChars.append(r.choice(alphaChars))
            a = "".join(randChars)
            img=qrcode.make(a)
            ic = img.save('/static/qr.png')
            uname = request.form['uname']
            dob = request.form['dob']
            address = request.form['add']
            city = request.form['city']
            Order_ID = a
            initial = request.form['in_s']
            final = request.form['fi_s']
            desg = 'customer'

            test1 = customer_token_details(Username=uname,DOB=dob,Address=address,City=city,Order_ID=Order_ID,Initial=initial,  Final=final,Designation=desg)
            db.session.add(test1)
            db.session.commit()
    return render_template("c/rd_four.html")
    

@app.route("/c/card", methods=['GET','POST'])
def c_card():
    if request.method == 'POST':
        if os.path.isfile('qr.png') is True:
            os.remove('qr.png')
        else:
            global ic1
            import random as r
            alphaChars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
            randChars = []
            charCount = 6
            for a in range(charCount):
                randChars.append(r.choice(alphaChars))
            a = "".join(randChars)
            img=qrcode.make(a)
            ic1 = img.save('/static/qr.png')
            uname = request.form['uname']
            dob = request.form['dob']
            address = request.form['add']
            Order_ID = a
            city = request.form['city']
            amount = request.form['amt']
            desg = 'customer'

            test2 = customer_card_details(Username=uname,DOB=dob,Address=address,Order_ID=Order_ID,City=city,Amount=amount,Designation=desg)
            db.session.add(test2)
            db.session.commit()

        
    return render_template("c/rd_five.html")

@app.route("/c/actions", methods=['GET','POST'])
def c_actions():
    global u__name
    if request.method == 'POST':
        u__name = request.form['username']
        act = customer_token_details.query.filter_by(Username=u__name)
        act1 = customer_card_details.query.filter_by(Username=u__name)
        return render_template("c/rd_one.html", act=act, act1=act1)
    else:
        return render_template("c/rd_one.html")




@app.route("/e/home", methods=['GET','POST'])
def e_home():
    return render_template("e/index.html")

@app.route("/e/delete_token/<int:SNo>")
def e_delete_token(SNo):
    delete = employee_token_details.query.filter_by(SNo=SNo,Username=user_name).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect('/e/actions')

@app.route("/e/delete_card/<int:SNo>")
def e_delete_card(SNo):
    delete = employee_card_details.query.filter_by(SNo=SNo,Username=user_name).first()
    db.session.delete(delete)
    db.session.commit()
    return redirect('/e/actions')

@app.route("/e/actions", methods=['GET','POST'])
def e_actions():
    global user_name
    if request.method == 'POST':
        user_name = request.form['uname']
        act = employee_token_details.query.filter_by(Username=user_name)
        act1 = employee_card_details.query.filter_by(Username=user_name)
        
        return render_template("e/rd_two.html", act=act, act1=act1)
    else:
        return render_template("e/rd_two.html")
@app.route("/e/attendance", methods=['GET','POST'])
def e_attendance():
    if request.method == 'POST':
        username = request.form['uname']
        dob = request.form['dob']
        d_name = request.form['d_name']
        d_id = request.form['d_id']
        emp_id = request.form['emp_id']
        date = request.form['date']
        day = request.form['day']
        desg = 'employee'

        test7 = attendance(Username=username,DOB=dob,Dept_Name=d_name,Dept_ID=d_id,Emp_ID=emp_id,Date=date,Day=day,Designation=desg)
        db.session.add(test7)
        db.session.commit()
    return render_template("e/rd_three.html")

@app.route("/e/token", methods=['GET','POST'])
def e_token():
    if request.method == 'POST':
        username = request.form['uname']
        if os.path.isfile('qr.png') is True:
            os.remove('qr.png')
        else:
            global ie
            import random as r
            alphaChars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
            randChars = []
            charCount = 6
            for a in range(charCount):
                randChars.append(r.choice(alphaChars))
            a = "".join(randChars)
            img=qrcode.make(a)
            ie = img.save('qr.png')
        dob = request.form['dob']
        address = request.form['add']
        city = request.form['city']
        Order_ID = a
        initial = request.form['in_s']
        final = request.form['fi_s']
        desg = 'employee'

        test3 = employee_token_details(Username=username,DOB=dob,Address=address,City=city,Order_ID=Order_ID,Initial=initial,Final=final,Designation=desg)
        db.session.add(test3)
        db.session.commit()
    return render_template("e/rd_four.html")

@app.route("/e/card", methods=['GET','POST'])
def e_card():
    if request.method == 'POST':
        if os.path.isfile('qr.png') is True:
            os.remove('qr.png')
        else:
            global ie1
            import random as r
            alphaChars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
            randChars = []
            charCount = 6
            for a in range(charCount):
                randChars.append(r.choice(alphaChars))
            a = "".join(randChars)
            img1=qrcode.make(a)
            ie1 = img1.save('qr.png')
            username = request.form['uname']
            dob = request.form['dob']
            address = request.form['add']
            Order_ID = a
            city = request.form['city']
            amount = request.form['amt']
            desg = 'employee'

            test4 = employee_card_details(Username=username,DOB=dob,Address=address,Order_ID=Order_ID,City=city,Amount=amount,Designation=desg)
            db.session.add(test4)
            db.session.commit()
        
    return render_template("e/rd_five.html")



    

@app.route("/a/home", methods=['GET','POST'])
def a_home():
    return render_template("a/index.html")

@app.route("/a/records")
def a_records():
    alltest = login_details.query.all()
    alltest1 = employee_token_details.query.all()
    alltest2 = employee_card_details.query.all()
    alltest3 = admin_token_details.query.all()
    alltest4 = admin_card_details.query.all()
    alltest5 = customer_token_details.query.all()
    alltest6 = customer_card_details.query.all()
    if os.path.isfile('qr.png') is True:
            os.remove('qr.png')
    else:
        import random as r
        alphaChars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
        randChars = []
        randChars1 = []
        charCount = 6
        for a in range(charCount):
                randChars.append(r.choice(alphaChars))
                randChars1.append(r.choice(alphaChars))
        a = "".join(randChars)
        a1 = "".join(randChars1)
        img=qrcode.make(a)
        img1=qrcode.make(a1)
        i = img.save('qrcode.png')   
        i1 = img1.save('qrcode1.png')   
    return render_template("a/rd_one.html", alltest=alltest, alltest1=alltest1, alltest2=alltest2, alltest3=alltest3, alltest4=alltest4, alltest5=alltest5, alltest6=alltest6, i=i, i1=i1)

@app.route("/a/salary", methods=['GET','POST'])
def a_salary():
    if request.method == 'POST':
        uname = request.form['uname']
        dob = request.form['dob']
        address = request.form['add']
        d_name = request.form['d_name']
        d_id = request.form['d_id']
        emp_id = request.form['emp_id']
        amt = request.form['amt']
        pay_date = request.form['pay_date']

        test8 = salary(Username=uname,DOB=dob,Address=address,Dept_Name=d_name,Dept_ID=d_id,Emp_ID=emp_id,Amount_Paid=amt,Date=pay_date)
        db.session.add(test8)
        db.session.commit()
    return render_template("a/rd_two.html")

@app.route("/a/attendance", methods=['GET','POST'])
def a_attendance():
    alltest7 = attendance.query.all()
    return render_template("a/rd_three.html", alltest7=alltest7)

@app.route("/a/token", methods=['GET','POST'])
def a_token():
    if request.method == 'POST':
        username = request.form['uname']
        if os.path.isfile('qr.png') is True:
            os.remove('qr.png')
        else:
            global ia
            import random as r
            alphaChars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
            randChars = []
            charCount = 6
            for a in range(charCount):
                randChars.append(r.choice(alphaChars))
            a = "".join(randChars)
            img=qrcode.make(a)
            ia = img.save('qr.png')
            dob = request.form['dob']
            address = request.form['add']
            city = request.form['city']
            Order_ID = a
            initial = request.form['in_s']
            final = request.form['fi_s']
            desg = 'admin'

            test5 = admin_token_details(Username=username,DOB=dob,Address=address,City=city,Order_ID=Order_ID,Initial=initial,Final=final,Designation=desg)
            db.session.add(test5)
            db.session.commit()
        
    return render_template("a/rd_four.html")

@app.route("/a/card", methods=['GET','POST'])
def a_card():
    if request.method == 'POST':
        if os.path.isfile('qr.png') is True:
            os.remove('qr.png')
        else:
            global ia1
            import random as r
            alphaChars = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
            randChars = []
            charCount = 6
            for a in range(charCount):
                randChars.append(r.choice(alphaChars))
            a = "".join(randChars)
            img=qrcode.make(a)
            ia1 = img.save('qr.png')
            username = request.form['uname']
            dob = request.form['dob']
            address = request.form['add']
            Order_ID = a
            city = request.form['city']
            amount = request.form['amt']
            desg = 'admin'

            test6 = admin_card_details(Username=username,DOB=dob,Address=address,Order_ID=Order_ID,City=city,Amount=amount,Designation=desg)
            db.session.add(test6)
            db.session.commit()
        
    return render_template("a/rd_five.html")

    

if __name__ == "__main__":
    app.run(debug=True)





