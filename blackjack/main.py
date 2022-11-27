import random

cards = {
    "A": [1, 11],
    "2": [2],
    "3": [3],
    "4": [4],
    "5": [5],
    "6": [6],
    "7": [7],
    "8": [8],
    "9": [9],
    "10": [10],
    "J": [10],
    "Q": [10],
    "K": [10],
}


def get_random_card():
    """Returns random card from cards list"""
    random_card = random.choice(list(cards))
    return {random_card: cards[random_card]}


def get_card_status(players_cards=[], is_dealer=False):
    """Returns card labels as list and total point as number"""
    cards_key = []
    cards_total_point = 0

    # collect all card's key
    for card in players_cards:
        cards_key.append(list(card.keys())[0])

    # calculate total points
    for key in cards_key:
        if not key == "A":
            cards_total_point += cards[key][0]
        elif is_dealer:
            # If card is "A" and is dealer, dealer uses "A" as 1 if total point is larger than 10. Otherwise dealer uses "A" as 11.
            if cards_total_point > 10:
                cards_total_point += 1
            else:
                cards_total_point += 11
        else:
            # If card is "A" and is user, user can select if user want use this card as 1 or 11
            use_card_as = input(f'You have "A"! Do you want use this as 1 or 11 ? \n')
            use_card_as_in_number = 0

            while use_card_as_in_number == 0:
                if use_card_as == "1":
                    use_card_as_in_number = 1
                elif use_card_as == "11":
                    use_card_as_in_number = 11
                else:
                    use_card_as = input("Please enter correct value. 1 or 11? \n")

            cards_total_point += use_card_as_in_number

    return {
        "card_labels": cards_key,
        "total_point": cards_total_point,
    }


# Start Game
# input('Hit the enter to start game!')

users_cards = []
dealers_cards = []

# Dealer and user get random card
dealers_cards.append(get_random_card())
for _ in range(2):
    users_cards.append(get_random_card())


user_result = get_card_status(users_cards)
dealer_result = get_card_status(dealers_cards, is_dealer=True)

print(f'You have {" and ".join(user_result["card_labels"])}')
print(f'Dealer have {" and ".join(dealer_result["card_labels"])}')

# Case if user have jackpot
if user_result["total_point"] == 21:
    while dealer_result["total_point"] < 18:
        new_dealers_card = get_random_card()
        dealers_cards.append(new_dealers_card)
        dealer_result = get_card_status(dealers_cards)
        print(f'Dealer have {" and ".join(dealer_result["card_labels"])}')

    if dealer_result["total_point"] == 21:
        print("Draw!")
    else:
        print("Jackpot! Congraturation!")

# Ask if user want hit or stand
else:
    user_game_result = 0

    while user_game_result == 0:
        user_hit = input("Enter 1 to hit and 2 to stand. \n") == "1"

        # Case if user hit
        if user_hit:
            new_users_card = get_random_card()
            print(f"{list(new_users_card.keys())[0]} is the new card!")

            users_cards.append(new_users_card)
            user_result = get_card_status(users_cards)
            print(f'You have {" and ".join(user_result["card_labels"])}')

            if user_result["total_point"] > 21:
                print(f'Your total point is {user_result["total_point"]}! You lost!')
                user_game_result = "USER LOST!"

            if user_result["total_point"] == 21:
                user_hit = "2"

            # Case if user stand
        else:
            while user_game_result == 0 and dealer_result["total_point"] <= 17:
                new_card = get_random_card()
                dealers_cards.append(new_card)
                print(f'Dealer have {" and ".join(dealer_result["card_labels"])}')
                print(f'Dealer\'s total count is {dealer_result["total_point"]}')
                dealer_result = get_card_status(dealers_cards, is_dealer=True)

                if dealer_result["total_point"] == user_result["total_point"]:
                    user_game_result = "Draw"
                elif (
                    dealer_result["total_point"] > user_result["total_point"]
                    and dealer_result["total_point"] <= 21
                ):
                    user_game_result = "User Won!"
                elif dealer_result["total_point"] > 21:
                    user_game_result = "USER LOST!"

        print(f'Dealer\'s total point is {dealer_result["total_point"]}')
        print(f"{user_game_result}")
