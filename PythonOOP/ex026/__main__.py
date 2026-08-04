from rich import print, inspect
from employees import *

def main():
    f1 = EmployeeHour("Mabel", 15, 200)
    f1.calc_salary()
    f1.analyse_salary()

    f2 = EmployeeMonth("Jake", 4200)
    f2.calc_salary()
    f2.analyse_salary()

if __name__ == "__main__":
    main()