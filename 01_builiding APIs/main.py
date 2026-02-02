from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List

employee_db: List[Employee] = []# variable: data_type[list of employee obj] = value

app = FastAPI()

#1. Read all employees
@app.get('/employees', response_model= List[Employee])
def get_employees():
    return employee_db
# #2. Read single employee or specific employee
# @app.get('/employees/{employee_id}', response_model= Employee) #format: employee/5, employee/20, means employee/id
# def get_employee(employee_id: int):
#     for emp in employee_db:
#         if emp.id == employee_id:
#             return emp
#     return {'error': 'Employee not found'}

#2. Read single employee or specific employee
@app.get('/employees/{emp_id}', response_model=Employee)
def get_employee(emp_id:int):
    for index, employee in enumerate(employee_db):
        if(employee.id == emp_id):
            return employee_db[index]
    raise HTTPException(status_code = 404, detail= 'Employee Not Found')

#3. Create or add  employee
@app.post('/add_employee', response_model= Employee)
def add_employee(new_employee:Employee):
    for employee in employee_db:
        if employee.id == new_employee.id:
            raise HTTPException(status_code=400, detail='Employee already exists')
    employee_db.append(new_employee)
    return new_employee    

#4. Update employee
@app.put('/update_employee/{emp_id}', response_model = Employee)
def update_employee(emp_id:int, updated_employee: Employee):
    for index, employee in enumerate(employee_db):
        if(employee.id == emp_id):
            employee_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code = 404, detail= 'Employee Not Found')



#5. Delete employee

@app.delete('/delete_employee/{emp_id}')
def delete_employee(emp_id: int):
       for index, employee in enumerate(employee_db):
            if(employee.id == emp_id):
                del employee_db[index]
                return {'message': 'Employee deleted successfully'}
       raise HTTPException(status_code = 404, detail= 'Employee Not Found')

  



