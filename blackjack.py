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

for _ in range(2):
    user_cards.append(deal_card())
    cpu_cards.append(deal_card())

user_score = calculate_score(user_cards)
cpu_score = calculate_score(cpu_cards)
print(f"   Your cards: {user_cards}, current score: {user_score}")
print(f"   Cpu card: {cpu_cards[0]}")

if user_score == 0 or cpu_score == 0 or user_score > 21:
    game_over = True 