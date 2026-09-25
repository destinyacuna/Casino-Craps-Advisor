
def can_place_bet(bankroll, table_minimum):
    if bankroll < table_minimum:
        return False
    else:
        return True

def place_pass_line_bet(bankroll, table_minimum):

    while True:
        try:
            bet = int(input(f"Enter Pass Line bet (minimum ${table_minimum})"))
            break
        except ValueError:
            print ("Please enter a dollar amount.")

    while bet < table_minimum or bet > bankroll:
        if bet < table_minimum:
            print("Bet is below table minimum.")

        elif bankroll > bet:
            print("Error. Not enough money!")

        bet = int(input("Enter a valid bet $"))

    return bet
