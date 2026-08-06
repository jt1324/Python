import ex009
from rich import print, inspect


def main():
    av1 = ex009.Evaluation("Pedro", "Math", 9.5)
    print(f"[blue]{av1.name}[/] has grade [green]{av1.get_grade()}[/] in [red]{av1.discipline}[/]")
    inspect(av1, private=True)


if __name__ == "__main__":
    main()

