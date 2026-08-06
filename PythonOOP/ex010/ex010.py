from rich import print

class Evaluation:
    def __init__(self, name, discipline, grade = 0):
        self.name = name
        self.discipline = discipline
        self._grade = grade

    # Creating validable attribute
    @property
    def grade(self):            #getter
        return self._grade

    @grade.setter               #setter
    def grade(self, value):
        if 0 <= value <= 10:
            return self._grade
        else:
            print("The grade must be between 0 and 10")

    