from rich.panel import Panel
from rich import print
from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, gross_salary=0, salary=0, min_wage=0, nin=0):
        self.name = name
        self.gross_salary = gross_salary
        self.salary = salary
        self.min_wage = 1800
        self.nin = 0.20

    @abstractmethod
    def calc_salary(self):
        pass

    def analyse_salary(self):
        pass


class EmployeeHour(Employee):
    def __init__(self, name, value_hour, hours_worked):
        super().__init__(name)
        self.value_hour = value_hour
        self.hours_worked = hours_worked

    def calc_salary(self):
        self.salary = (self.value_hour * self.hours_worked) * (1 - self.nin)

    def analyse_salary(self):
        panel = Panel(f"[blue]{self.name}'s[/blue] salary [magenta](Hourly Employee)[/magenta] is [green]£{self.salary:.2f}[/green] and correspond to [yellow]{self.salary/self.min_wage:.1f} minimum wages[/yellow].", title = "Salary Analysis", width = 50, expand = False, border_style = "light_green")
        print(panel)


class EmployeeMonth(Employee):
    def __init__(self, name, gross_salary):
        super().__init__(name)
        self.gross_salary = gross_salary

    def calc_salary(self):
        self.salary =  self.gross_salary * (1 - self.nin)

    def analyse_salary(self):
        panel = Panel(f"[blue]{self.name}'s[/blue] salary [magenta](Monthly Employee)[/magenta] is [green]£{self.salary:.2f}[/green] and correspond to [yellow]{self.salary/self.min_wage:.1f} minimum wages[/yellow].", title = "Salary Analysis", width = 50, expand = False, border_style = "light_green")
        print(panel)
