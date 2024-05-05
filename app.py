from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://newuser:newpassword@127.0.0.1/students'

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'  
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    cgpa = db.Column(db.Float)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students')
def students():
    student_records = Student.query.all()
    return render_template('students.html', students=student_records)

if __name__ == '__main__':
    app.run(debug=True)
