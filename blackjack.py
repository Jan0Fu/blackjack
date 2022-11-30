import random
import os

user_cards = []
cpu_cards = []
game_over = False

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, cpu_score):
    if user_score == cpu_score:
        return "Draw"
    elif cpu_score == 0:
        return "Dealer has Blackjack! You lose!"
    elif user_score == 0:
        return "You have Blackjack! You win!"
    elif user_score > 21:
        return "Its a bust! You lose."
    elif cpu_score > 21:
        return "Dealer is over 21. You win!"
    elif user_score > cpu_score:
        return "You win!"
    else:
        return "You lose!"    

for _ in range(2):
    user_cards.append(deal_card())
    cpu_cards.append(deal_card())

while not game_over:
    user_score = calculate_score(user_cards)
    cpu_score = calculate_score(cpu_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Cpu card: {cpu_cards[0]}")

    if user_score == 0 or cpu_score == 0 or user_score > 21:
        game_over = True 
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(deal_card())
        else:
            game_over = True

while cpu_score != 0 and cpu_score < 17:
    cpu_cards.append(deal_card())
    cpu_score = calculate_score(cpu_cards)
print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Dealers final hand: {cpu_cards}, final score: {cpu_score}")
print(compare(user_score, cpu_score))

#Hint 14: Ask the user if they want to restart the game. 
#If they answer yes, clear the console and start a new game of blackjack
#and show the logo from art.py.
