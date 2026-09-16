from game import play_round

def greet_player():
    print("Welcome to the Craps Table Simulator!")

def main():
    greet_player()
    bankroll = int(input("To begin enter your starting bankroll: $"))
    print("\nYou are starting with $",bankroll, "\n")

    # Asks the player to begin the roll
    while True:
        choice = input("Press Enter to roll the dice or -1 to quit...")

        if choice == "-1":
            break
        elif choice == "":
            result = play_round()
            print("\nRound result:", result, "\n")
        else:
            print("Invalid input.")

main()

