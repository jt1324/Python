from ast import Pass
from rich import print, inspect

from classes import Student, Teacher, Employee



def main():
    s1 = Student("John", 20, "IT", "1A")
    s1.birthday()
    s1.enroll()
    s1.study()
    #inspect(s1, methods=True)

    t1 = Teacher("Jane", 30, "Math", "Master")
    t1.birthday()
    t1.teach()
    t1.study()
    #inspect(t1, methods=True)

    e1 = Employee("Jim", 40, "Manager", "HR")
    e1.birthday()
    e1.work()
    e1.study()
    #inspect(e1, methods=True)



if __name__ == "__main__":
    main()