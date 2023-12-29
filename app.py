from flask import Flask,render_template,request
import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='12345678',database='employeemanagementsystem')
mycursor = conn.cursor()
# Create the flask Application
app=Flask(__name__)

#create a dictionary for login

user_dict={'admin':'1234','Sivajith':'abcd'}


# Define a route and corresponding view

@app.route('/')
def Hello():
    #return "Hello World!!!"
    # Call our html Page
    return render_template('index.html')

# Define a route and corresponding view Home page
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/emp_home', methods=['POST'])
def emp_home():
    username=request.form['username']
    pwd=request.form['password']
    if username not in user_dict:
        return render_template('login.html', msg='Invalid Username')
    elif user_dict[username]!=pwd:
        return render_template('login.html', msg='Invalid Password')
    else:
        return render_template('home.html',user=username)

#view
@app.route('/view')
def view():
        query="SELECT * FROM EMPLOYEES"
        mycursor.execute(query)
        data=mycursor.fetchall()
        return render_template('view.html',sqldata=data)
#search
@app.route('/search')
def search():
    return render_template('search.html')
@app.route('/searchresult', methods=['POST'])
def searchresult():
    ename=request.form.get('empname')
    query="SELECt * FROM EMPLOYEES WHERE emp_name LIKE '%{}%'".format(ename)
    mycursor.execute(query)
    data=mycursor.fetchall()
    if not data:
        return render_template('search.html',msg="Employee not found")
    else:
        return render_template('view.html',sqldata=data)
# Add Employee
@app.route('/add')
def add():
    return render_template('add.html')
                           
@app.route('/addemployee',methods=['POST'])
def addemployee():
    empid=request.form('emp_id')
    ename=request.form('emp_name')
    salary=request.form('emp_salary')
    dept=request.form('emp_dept')
    query="INSERT INTO EMPLOYEES VALUES(%s,%s,%s,%s)" 
    data=(empid,ename,salary,dept)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('home.html')

def add():
    return render_template('add.html')


    # Run flask Applications
if __name__=='__main__':
    app.run(debug=True)