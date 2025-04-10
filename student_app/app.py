from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store student records
students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        student = {'name': name, 'roll': roll}
        students.append(student)
        return redirect(url_for('index'))
    return render_template('add_student.html')

@app.route('/delete/<int:index>')
def delete_student(index):
    if 0 <= index < len(students):
        students.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
