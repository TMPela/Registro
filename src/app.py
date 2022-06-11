from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/register-db'

mongo = PyMongo(app)

@app.route('/')
def index():
    return 'Holas'

@app.route('/teachers', methods=['POST'])
def createTeacher():
    name = request.json['name']
    surname = request.json['surname']

    if name and surname:
        id = mongo.db.teachers.insert_one({
            'name': name,
            'surname': surname
        })

        response = {
            'id': str(id),
            'name': name,
            'surname': surname
        }

        return response
    else:
        return 'Error'

if __name__ == '__main__':
    app.run()
