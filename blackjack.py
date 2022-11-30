import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
cpu_cards = []
game_over = False

def random_card():
    return random.choice(cards)


def blackjack():
    user_cards.append(random_card())
    cpu_cards.append(random_card())
    user_cards.append(random_card())
    if user_cards[1] == 11 and sum(user_cards) > 21:
        user_cards[1] = 1
    cpu_cards.append(random_card())
    if cpu_cards[1] == 11 and sum(cpu_cards) > 21:
        cpu_cards[1] = 1
    print(user_cards)
    print(cpu_cards[0])
    if sum(cpu_cards) == 21:
        return "Dealer has 21, you lost..."
    elif sum(user_cards) == 21:
        "21, blackjack! You won!"
    game_input = input("Pick a card?: y/n")
    if game_input == "y":
        user_cards.append(random_card())
        cpu_cards.append(random_card())
        if sum(user_cards) > 21:
            return "f{sum(user_cards)} bust! You lost}"
        print(sum(user_cards))

        

    elif game_input == "n":
        print(sum(user_cards))
        print(sum(cpu_cards))
        if sum(user_cards) == sum(cpu_cards):
            return "Draw"
        elif sum(user_cards) > sum(cpu_cards):
            return "You won!"
        else:
            "You lost"
    else:
        print("Invalid input, try again")
        return blackjack()
    


while not game_over:
    user_input = input("Do you want to play?: y/n")
    if user_input == "n":
        game_over = True
    elif user_input == "y":
        blackjack()
    else:
        print("Invalid input, try again")
