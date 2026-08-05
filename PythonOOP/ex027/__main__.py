from persona_rpg import *

def main():
    p1 = Warrior("Kratos", 2000)
    p2 = Wizard("Merlin", 3000)

    p1.attack(p2, 1000)
    p2.heal()
    p2.attack(p1, 20000)
    p1.heal()

if __name__ == "__main__":
    main()