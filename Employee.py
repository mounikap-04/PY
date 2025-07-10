class Employee:
    def __init__(self,name=None,age=None,salary=None):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Error: Salary must be greater than 0.")
    def get_salary(self):
        return self.__salary
    def set_age(self, age):
        if 18 <= age <= 100:
            self.__age = age
        else:
            print("Error: Age must be between 18 and 100.")
    def get_age(self):
        return self.__age
emp = Employee()
emp.set_name("John Doe")
emp.set_salary(50000.0)
emp.set_age(30)
print("Employee Name:", emp.get_name())
print("Employee Salary:", emp.get_salary())
print("Employee Age:", emp.get_age())
emp.set_salary(-1000)
