from game import play_round
from bet import place_pass_line_bet, can_place_bet

def greet_player():
    print("Welcome to the Craps Table Simulator!")

def main():
    greet_player()
    bankroll = int(input("To begin enter your starting bankroll: $"))
    print("\nYou are starting with $",bankroll, "\n")
    table_minimum = 10

    # Asks the player to begin the roll
    while True:
        choice = input("Press Enter to start a round or -1 to quit...")

        if choice == "-1":
            print("Thanks for playing Craps!")
            break
        elif choice == "":
            if can_place_bet(bankroll, table_minimum):
                pass_bet = place_pass_line_bet(bankroll, table_minimum)
                result = play_round()
            else:
                print("Invalid funds for table minimum")
                break
        else:
            print("Invalid input.")

main()

