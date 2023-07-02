from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # SQLite database file path
app.config['SECRET_KEY'] = 'xyz123'
db = SQLAlchemy(app)
#Flask Assignment
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    college = db.Column(db.String(100))

    def __repr__(self):
        return f"<Student {self.name}>"

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        student = Student(name=name, college=college)
        db.session.add(student)
        db.session.commit()
        flash('Data added successfully!', 'success')
        return redirect(url_for('index'))  # Redirect to GET request for index route

    students = Student.query.all()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
