from game import play_round
from bet import (place_pass_line_bet, can_place_bet,
                 settle_pass_line_bet)

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

                bankroll = bankroll - pass_bet

                result = play_round()

                bankroll = settle_pass_line_bet(bankroll, pass_bet,
                                                result)

                print(f"Current bankroll: ${bankroll}")
            else:
                print("Invalid funds for table minimum")
                break
        else:
            print("Invalid input.")

main()

