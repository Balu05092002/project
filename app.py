from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import config

app = Flask(__name__)
app.config.from_object(config)

mysql = MySQL(app)

@app.route('/')
def employee_list():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM employee")
    employees = cur.fetchall()
    return render_template('employee_list.html', employees=employees)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        emp_id = request.form['emp_id']
        designation = request.form['designation']
        department = request.form['department']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee (name, emp_id, designation, department) VALUES (%s, %s, %s, %s)",
                    (name, emp_id, designation, department))
        mysql.connection.commit()
        return redirect('/')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
