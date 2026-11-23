print("WELCOME TO THE DUNGEON QUEST! ")
name = input("What's your name adventurer?: ")

stats = {
    "name": name,
    "hp": 100,
    "gold": 0
}
while True:
    print("1. Raid Dungeon (WIP)")
    print("2. View Stats")
    print("3. Exit")

    try: 
        choice = int(input("Enter a number: "))
    except ValueError:
        print("That's not a number! Please Try again")
        continue

    if choice == 1:
        print("This is not available")
    elif choice == 2:
        print(f"Name: {stats["name"]}")
        print(f"Hp: {stats['hp']}")
        print(f"Gold: {stats['gold']}")
    elif choice == 3:
        print("Thank you for playing!")
        break