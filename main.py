from game import roll_dice

def greet_player():
    print("Welcome to the Craps Table Simulator!")

def main():
    greet_player()
    bankroll = int(input("To begin enter your starting bankroll: $"))
    print()
    print("You are starting with $",bankroll)
    print()

    # Asks the player to begin the roll
    input("Press Enter to roll the dice...")
    print()

    #Roll the dice and store total
    total = roll_dice()

main()

