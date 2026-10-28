
def can_place_bet(bankroll, table_minimum):
    if bankroll < table_minimum:
        return False
    else:
        return True

def place_pass_line_bet(bankroll, table_minimum):

    while True:
        try:
            bet = int(input(f"Enter Pass Line bet (minimum ${table_minimum})"))

            if bet < table_minimum:
                print("Bet is below table minimum.")

            elif bet > bankroll:
                print("Error. Not enough money!")

            else:
                return bet

        except ValueError:
            print ("Please enter a dollar amount.")

def settle_pass_line_bet(bankroll, pass_bet, result):
    if result == "win":
        bankroll = bankroll + (pass_bet * 2)

    return bankroll