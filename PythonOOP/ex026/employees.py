from rich.panel import Panel
from rich import print
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, gross_salary, salary, min_wage, nin):
        self.name = name
        self.gorss_salary = gross_salary
        self.salary = salary
        self.nim_wage = min_wage
        self.nin = nin

    @abstractmethod
    def calc_salary(self):
        pass

    def analyse_salary(self):
        pass


class Hourly(Employee):
    def __init__(self, name, value_hour, hours_worked):
        self.name = name
        self.value_hour = value_hour
        self.hours_worked = hours_worked

    def calc_salary(self):
        pass


class Monthly(Employee):
    def __init__(self, name, nim_wage, nin):
        self.name = name
        self.min_wage = min_wage
        self.nin = nin

    def calc_salary(self):
        pass


