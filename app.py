from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'popit'

mysql = MySQL(app)

# Main app route 
@app.route('/')
def index():
    return redirect(url_for('view_employees'))

# View all employees
@app.route('/employees')
def view_employees():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, first_name, last_name FROM employees")
    employees = cur.fetchall()
    cur.close()
    return render_template('view_employees.html', employees=employees)

# Add employee
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        employee_data = request.form
        first_name = employee_data['first_name']
        last_name = employee_data['last_name']
        position = employee_data['position']
        contact_no = employee_data['contact_no']
        personal_email = employee_data['personal_email']
        work_email = employee_data['work_email']
        manager = employee_data['manager']
        team_leader = employee_data['team_leader']
        blood_group = employee_data['blood_group']
        age = employee_data['age']
        sex = employee_data['sex']
        marital_status = employee_data['marital_status']
        address = employee_data['address']
        city = employee_data['city']
        NIC = employee_data['NIC']
        joined_date = employee_data['joined_date']
        years_spent = employee_data['years_spent']
        employment_status = employee_data['employment_status']
        bank_acc_no = employee_data['bank_acc_no']
        bank_code = employee_data['bank_code']
        bank_branch_code = employee_data['bank_branch_code']
        promotion_date = employee_data['promotion_date']
        
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employees (first_name, last_name, position, contact_no, personal_email, work_email, manager, team_leader, blood_group, age, sex, marital_status, address, city, NIC, joined_date, years_spent, employment_status, bank_acc_no, bank_code, bank_branch_code, promotion_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (first_name, last_name, position, contact_no, personal_email, work_email, manager, team_leader, blood_group, age, sex, marital_status, address, city, NIC, joined_date, years_spent, employment_status, bank_acc_no, bank_code, bank_branch_code, promotion_date))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('view_employees'))

    return render_template('add_employee.html')

# Update employee
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        employee_data = request.form
        first_name = employee_data['first_name']
        last_name = employee_data['last_name']
        position = employee_data['position']
        contact_no = employee_data['contact_no']
        personal_email = employee_data['personal_email']
        work_email = employee_data['work_email']
        manager = employee_data['manager']
        team_leader = employee_data['team_leader']
        blood_group = employee_data['blood_group']
        age = employee_data['age']
        sex = employee_data['sex']
        marital_status = employee_data['marital_status']
        address = employee_data['address']
        city = employee_data['city']
        NIC = employee_data['NIC']
        joined_date = employee_data['joined_date']
        years_spent = employee_data['years_spent']
        employment_status = employee_data['employment_status']
        bank_acc_no = employee_data['bank_acc_no']
        bank_code = employee_data['bank_code']
        bank_branch_code = employee_data['bank_branch_code']
        promotion_date = employee_data['promotion_date']
        
        cur.execute("UPDATE employees SET first_name = %s, last_name = %s, position = %s, contact_no = %s, personal_email = %s, work_email = %s, manager = %s, team_leader = %s, blood_group = %s, age = %s, sex = %s, marital_status = %s, address = %s, city = %s, NIC = %s, joined_date = %s, years_spent = %s, employment_status = %s, bank_acc_no = %s, bank_code = %s, bank_branch_code = %s, promotion_date = %s WHERE id = %s", 
                    (first_name, last_name, position, contact_no, personal_email, work_email, manager, team_leader, blood_group, age, sex, marital_status, address, city, NIC, joined_date, years_spent, employment_status, bank_acc_no, bank_code, bank_branch_code, promotion_date, id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('view_employees'))
   
    cur.execute("SELECT * FROM employees WHERE id = %s", (id,))
    employee = cur.fetchone()
    cur.close()
    return render_template('update_employee.html', employee=employee) 

# Delete employee
@app.route('/delete/<int:id>', methods=['POST'])
def delete_employee(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employees WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('view_employees'))

if __name__ == '__main__':
    app.run(debug=True)
