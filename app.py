from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL 配置
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'student_management'

mysql = MySQL(app)

# 主網頁
@app.route('/')
def main():
    return render_template('main.html')

# 學生管理
@app.route('/students', methods=['GET', 'POST'])
def students():
    if request.method == 'POST':
        # 新增學生
        name = request.form['name']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email) VALUES (%s, %s)", (name, email))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('students'))
    
    # 顯示學生列表
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    return render_template('students.html', students=data)

# 課程管理
@app.route('/courses', methods=['GET', 'POST'])
def courses():
    if request.method == 'POST':
        # 新增課程
        name = request.form['name']
        description = request.form['description']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO courses (name, description) VALUES (%s, %s)", (name, description))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('courses'))
    
    # 顯示課程列表
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM courses")
    data = cur.fetchall()
    cur.close()

    return render_template('courses.html', courses=data)

# 成績管理
@app.route('/grades', methods=['GET', 'POST'])
def grades():
    if request.method == 'POST':
        student_id = request.form['student_id']
        course_id = request.form['course_id']
        grade = request.form['grade']
        
        # 將成績插入到資料庫
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO grades (student_id, course_id, grade) VALUES (%s, %s, %s)", (student_id, course_id, grade))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('grades'))
    
    # 顯示成績列表
    cur = mysql.connection.cursor()
    cur.execute("SELECT g.id, s.name AS student_name, c.name AS course_name, g.grade FROM grades g JOIN students s ON g.student_id = s.id JOIN courses c ON g.course_id = c.id")
    grades_data = cur.fetchall()
    cur.close()
    
    # 從資料庫中獲取學生和課程的列表
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, name FROM students")
    students = cur.fetchall()
    cur.execute("SELECT id, name FROM courses")
    courses = cur.fetchall()
    cur.close()
    
    return render_template('grades.html', grades=grades_data, students=students, courses=courses)

if __name__ == '__main__':
    app.run(debug=True)