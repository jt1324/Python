from rich.panel import Panel
from rich import print
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, gross_salary, salary, min_wage, nin):
        self.name = name
        self.gross_salary = gross_salary
        self.salary = salary
        self.min_wage = min_wage
        self.nin = nin

    @abstractmethod
    def calc_salary(self):
        pass

    def analyse_salary(self):
        pass


class EmployeeHour(Employee):
    def __init__(self, name, value_hour, hours_worked):
        super().__init__(name, 0, 0, 0, 0)
        self.value_hour = value_hour
        self.hours_worked = hours_worked

    def calc_salary(self):
        self.nin = 0.20
        self.min_wage = 1800
        self.salary = (self.value_hour * self.hours_worked) * (1 - self.nin)

    def analyse_salary(self):
        print(f"{self.name}'s salary (Hourly Employee) is £{self.salary} and correspond to {self.salary/self.min_wage:.1f} minimum wages.")


class EmployeeMonth(Employee):
    def __init__(self, name, gross_salary):
        super().__init__(name, 0, 0, 0, 0)
        self.gross_salary = gross_salary

    def calc_salary(self):
        self.nin = 0.20
        self.min_wage = 1800
        self.salary =  self.gross_salary * (1 - self.nin)

    def analyse_salary(self):
        print(f"{self.name}'s salary (Monthly Employee) is £{self.salary} and correspond to {self.salary/self.min_wage:.1f} minimum wages.")
