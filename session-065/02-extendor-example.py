class Employee: 
    def __init__(self, emp_name:str, emp_id:int, emp_sal:float): 
        self.emp_name = emp_name 
        self.emp_id = emp_id 
        self.emp_sal = emp_sal 

    def get_salary(self) -> float: 
        return self.emp_sal 

    def set_salary(self, new_sal:float) -> None: 
        self.emp_sal = new_sal 

    def show_info(self): 
        print(f'Name:{self.emp_name}')
        print(f'ID:{self.emp_id}')
        print(f'Salary:{self.emp_sal}')

class Manager(Employee): 
    def __init__(self, manager_name:str, manager_emp_id:int, sal:float,manager_team_size:int): 
        Employee.__init__(self, manager_name, manager_emp_id, 10000.0)
        self.team_size = manager_team_size 

    def get_manager_team_size(self) -> int: 
        return self.manager_team_size

    # Base class method get_salary()  (Base class = Employee)
    # is reimplemented by derived class (Derived Class = Manager)
    # But derived class' implementation invokes base class' implementation 
    # (i.e. Manager's get_salary() class Employee's get_salary)
    # and adds some logic to it, making a get_salary() in Manager an extendor method 
    # Overriding for the purpose of extension 
    def get_salary(self): 
        basic_sal = Employee.get_salary(self)
        return 1.15 * basic_sal # Manager salary is 15% more than employee salary 

m = Manager("sagar",11,1123,3)
m.show_info()

