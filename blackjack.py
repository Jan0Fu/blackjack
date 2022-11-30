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
    cpu_cards.append(random_card())
    print(user_cards)
    print(cpu_cards[0])

    return


while not game_over:
    user_input = input("Do you want to play?: y/n")
    if user_input == "n":
        game_over = True
    elif user_input == "y":
        blackjack()
    else:
        print("Invalid input, try again")
