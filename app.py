from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = ('postgresql+psycopg:///school_db')

db = SQLAlchemy(app)

# for students ------------------------------

class Students(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)
    
    def __repr__(self):
        return f'{self.id} {self.first_name} - for students'
    


def student_serializer(stud: Students) ->dict: #these are hints
    return {
        'id' : stud.id,
        'first_name' : stud.first_name,
        'last_name' : stud.last_name,
        'age' : stud.age,
        'subject' : stud.subject
    }
    
# for teachers ------------------------------

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)   
    
    def __repr__(self):
        return f'{self.id} {self.first_name} - for teachers' 


def teacher_serializer(teach: Teachers) -> dict:
    return {
        'id' : teach.id,
        'first_name' : teach.first_name,
        'last_name' : teach.last_name,
        'age' : teach.age,
        'subject' : teach.subject        
    }


# for subjects ----------------------------

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255))
    
    def __repr__(self):
        return f'{self.id} {self.subject} - for subjects'

def subject_serializer(subj: Subjects) -> dict:
    return {
        'id' : subj.id,
        'subject' : subj.subject
    }


#below will be the start of my app.routes. will need to do for subject and teachers as well

@app.route('/') #don't forget the @ symbol
def home():
    return '<h1> WELCOME TO MY HOMEPAGE</h1>'

@app.route('/students', methods=['GET'])

def get_students():
    result = []
    all_students = Students.query.all()
    print(all_students)
    for stud in all_students:
        serialized = student_serializer(stud)
        result.append(serialized)
    return jsonify(result)
    















### -------- this will run the program-----------------------###

if __name__ == '__main__':
    app.run(debug=True, port= 8000)
