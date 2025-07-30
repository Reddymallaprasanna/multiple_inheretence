class intern:  #super class
    def __init__(self,name):
        self.name=name
    def display_intern(self):
        print(f"Name :{self.name}")

class employee(intern): #clas
    def __init__(self,emp_id):
        super().__init__(name)
        self.emp_id=emp_id
    def display_emp(self):
        print(f"Employee ID :{self.emp_id}")

class manager(employee): #sub class
    def __init__(self,name,emp_id,dept):
        super().__init__(emp_id)
        self.dept=dept
    def display_manager(self):
        print(f"Department :{self.dept}")
name=input("Enter name :")
emp_id=input("Enter the employee_id :")
dept=input("Enter the Department :")
m=manager(name,emp_id,dept)
m.display_intern()
m.display_emp()
m.display_manager()