import random

def roll_dice():
    # Generate two random dice values
    die1 = random.randint (1,6)
    die2 = random.randint (1,6)

    total_roll = die1 + die2

    print(f"Player rolled a {die1} and a {die2}.")
    print(f"Total: {total_roll}")

    return total_roll

def check_come_out_roll(total):
    if total in (7,11):
        return "win"
    elif total in (2, 3 , 12):
        return "lose"
    else:
        point = total
        return point

def play_point_phase(point):
    while True:
        input ("Press Enter to roll again.")

        total = roll_dice()

        if total == point:
            return "win"
        elif total == 7:
            return "lose"

def play_round():
    total = roll_dice()

    result = check_come_out_roll(total)
    if result == "win":
        return "win"
    elif result == "lose":
        return "lose"
    else:
        return play_point_phase(result)
