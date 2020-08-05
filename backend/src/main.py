from entities.entity import Session, engine, Base
from entities.employee import Employee

# generate database schema
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
employees = session.query(Employee).all()

if len(employees) == 0:
    # create and persist dummy exam
    python_employee = Employee("Jelani Hurtault", "806-470-4067", "script")
    session.add(python_employee)
    session.commit()
    session.close()

    # reload exams
    employees = session.query(Employee).all()

# show existing exams
print('### Employees:')
for employee in employees:
    print(f'({employee.id}) {employee.full_name} - {employee.phone_number}')