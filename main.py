import random
RUN_CHANCE = 70
HP_RESTORE = 5
HEALING_POTIONS = 5
LOST_GOLD = 5
CRIT_CHANCE = 15
CRIT_MULTIPLIER = 2

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
    "maxHP":100,
    "hp": 100,
    "gold": 0
}

monsters = [
    {
        "name": "slime",
        "attack": 5,
        "maxHP":75,
        "hp": 75,
        "gold": 10
    },
    {
        "name": "goblin",
        "attack": 10,
        "maxHP":40,
        "hp": 40,
        "gold": 15
    },
    {
        "name": "skeleton",
        "attack": 15,
        "maxHP":30,
        "hp": 30,
        "gold": 20
    }
]

def encounter():
    monster = random.choice(monsters)
    print(f"wild {monster['name']} has appeared! ")
    return monster


def battle(monster):
    hp_potion_remaining = HEALING_POTIONS
    print()
    monster = monster.copy()
    print(f"Battle started against {monster['name']}!")

    print(f"Your HP: {stats['hp']}")
    print(f"Enemy HP: {monster['hp']}")
    print()

    while True:
        print("PICK YOUR TURN")
        print("1. Attack")
        print("2. Heal")
        print(f"3. Run ({RUN_CHANCE}%)")

        try:
            choice = int(input("Enter your action: "))
        except ValueError:
            print("It's not a number")
            continue

        if choice == 1:
            damage = stats["attack"]
            if random.randint(1,100) <= CRIT_CHANCE:
                damage = damage * CRIT_MULTIPLIER
                print(f"Your attack crits and dealt {damage} damage")
            else:
                print(f"You attacked and dealt {damage} damage")
            monster['hp'] = max(monster['hp'] - damage, 0)
            print(f"Enemy has {monster['hp']} hp left")
            if monster['hp'] <= 0:
                print(f"{monster['name']} has been slain")
                print(f"You earned {monster['gold']} gold")
                stats['gold'] = stats["gold"] + monster['gold']
                break
        elif choice == 2:
            if hp_potion_remaining <= 0:
                print("You ran out of healing potion! ")
                continue
            elif stats['hp'] == stats["maxHP"]:
                print("Your hp is full!")
                continue
            else:
                stats['hp'] = min(stats["hp"] + HP_RESTORE, stats["maxHP"])
                print(f"You healed now you have {stats['hp']} hp")
                hp_potion_remaining -= 1
                print(f"You only have {hp_potion_remaining} healing potion left")
        elif choice == 3:
            if random.randint(1, 100) <= RUN_CHANCE:
                print("You successfully ran away!")
                break
            else:
                print("Failed to escape!")
        else:
            print("Invalid Input!")
            continue

        print()
        print(f"You received {monster['attack']} damage!")
        stats["hp"] = max(stats["hp"] - monster['attack'], 0)
        print(f"Your remaining HP: {stats['hp']}")

        if stats['hp'] <= 0:
            print("You died! Better luck next time!")
            print()

            gold_to_lose = min(stats['gold'], LOST_GOLD)
            stats["gold"] -= gold_to_lose

            print(f"You lost: {gold_to_lose} gold")
            print(f"Remaining Gold: {stats['gold']}")

            stats['hp'] = stats["maxHP"]
            break

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
        battle(monster)
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