class Student:
    def __init__(self):
        self.__name=""
        self.__marks=0
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_marks(self,marks):
        if 0<=marks<=100:
            self.__marks=marks
        else:
            print("error:marks should be between 0 and 100")
    def get_marks(self):
        return self.__marks
student1=Student()
student1.set_name("Alice")
student1.set_marks(50)
print("student name",student1.get_name())
print("student marks",student1.get_marks())
student1.set_marks(200)
print("Student Marks(after invalid input):", student1.get_marks())





