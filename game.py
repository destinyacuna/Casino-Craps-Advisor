import random

def roll_dice():
    # Generate two random dice values
    die1 = random.randint (1,6)
    die2 = random.randint (1,6)

    total_roll = die1 + die2

    print(f"Player rolled a {die1} and a {die2}.")
    print(f"Total: {total_roll}")

    return total_roll
