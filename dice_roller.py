import random

def roll_dice(sides=6):
    return random.randint(1, sides)

if __name__ == "__main__":
    print("Dice Roller 🎲")
    while True:
        sides = input("How many sides? (default=6): ")
        sides = int(sides) if sides.strip() else 6
        print(f"You rolled: {roll_dice(sides)}")
        if input("Roll again? (y/n): ").lower() != "y":
            break
