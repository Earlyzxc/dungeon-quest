import random

print("WELCOME TO THE DUNGEON QUEST! ")
print()
while True:
    name = input("What's your name adventurer?: ").strip()

    if not name:
        print("Please! Enter your name")
        continue

    break

stats = {
    "name": name,
    "attack": 15,
    "hp": 100,
    "gold": 0
}

monsters = [
    {
        "name": "slime",
        "attack": 5,
        "hp": 75,
        "gold": 10
    },
    {
        "name": "goblin",
        "attack": 10,
        "hp": 40,
        "gold": 15
    },
    {
        "name": "skeleton",
        "attack": 15,
        "hp": 30,
        "gold": 20
    }
]

def encounter():
    monster = random.choice(monsters)
    print(f"wild {monster['name']} has appeared! ")
    return monster


while True:

    print()
    print("1. Raid Dungeon (WIP)")
    print("2. View Stats")
    print("3. Exit")

    try: 
        choice = int(input("Enter a number: "))
    except ValueError:
        print("That's not a number! Please Try again")
        continue

    if choice == 1:
        monster = encounter()
    elif choice == 2:
        print(f"Name: {stats['name']}")
        print(f"Attack: {stats['attack']}")
        print(f"Hp: {stats['hp']}")
        print(f"Gold: {stats['gold']}")
    elif choice == 3:
        print("Thank you for playing!")
        break
    else:
        print("Invalid number")