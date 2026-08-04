from rich import print, inspect
from employees import *

def main():
    f1 = EmployeeHour("Mabel", 16.5, 200)
    f1.calc_salary()
    f1.analyse_salary()

    f2 = EmployeeMonth("Jake", (36200/12))
    f2.calc_salary()
    f2.analyse_salary()

if __name__ == "__main__":
    main()