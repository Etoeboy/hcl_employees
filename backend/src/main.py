from flask import Flask, jsonify, request

from entities.entity import Session, engine, Base
from entities.employee import Employee, EmployeeSchema

# creating the Flask application
app = Flask(__name__)

# generate database schema
Base.metadata.create_all(engine)

@app.route('/')
def welcome():
    return "<h1>Welcome to my employee database!</h1>"


@app.route('/employees')
def get_employees():
    # fetching from the database
    session = Session()
    employee_objects = session.query(Employee).all()

    # transforming into JSON-serializable objects
    schema = EmployeeSchema(many=True)
    employees = schema.dump(employee_objects)

    # serializing as JSON
    session.close()
    return jsonify(employees)


@app.route('/employees', methods=['POST'])
def add_employee():
    # mount employee object
    posted_employee = EmployeeSchema(only=('full_name', 'phone_number'))\
        .load(request.get_json())

    employee = Employee(**posted_employee, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(employee)
    session.commit()

    # return created exam
    new_employee = EmployeeSchema().dump(employee)
    session.close()
    return jsonify(new_employee), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)