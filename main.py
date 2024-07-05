import random
import os
from image import logo
cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []


def clear_console():
    # Print enough newline characters to clear the screen
    print('\n' * 100)


def check_blackjack(cards):
    if 11 in cards and 10 in cards:
        return "y"
    else:
        return "n"


def check_score(cards):
    card_total = 0
    for individual_card in cards:
        card_total += individual_card
    return card_total


def deal(cards):
    next_card = random.choice(cards_deck)
    cards.append(next_card)


def play():

    for i in range(2):
        random_card = random.choice(cards_deck)
        user_cards.append(random_card)

    print(f"        Your cards: {user_cards}, current_score: {check_score(user_cards)}")
    computer_cards = []
    for i in range(2):
        random_card = random.choice(cards_deck)
        computer_cards.append(random_card)

    print(f"        computer's card: {computer_cards} ")

    if check_blackjack(cards=computer_cards) == 'y':

        print("computer wins with a blackjack. You lose")
    elif check_blackjack(cards=user_cards) == 'y':
        print("YOu have a clear blackjack.You win")
    else:
        game_continue = 'y'
        print("\n")
        while game_continue == 'y' and check_score(user_cards) < 21:

            extra_card = input("Type y to get another card, type n to pass: ")
            if extra_card == 'y':
                deal(user_cards)

                if 11 in user_cards and check_score(user_cards) > 21:
                    position_of_11 = user_cards.index(11)
                    user_cards[position_of_11] = 1
                print(f"        Your cards: {user_cards}, current_score: {check_score(user_cards)}")

            if extra_card == 'n' or check_score(user_cards) >= 21:
                while check_score(computer_cards) < 16:
                    deal(computer_cards)
                    if 11 in computer_cards and check_score(computer_cards) > 21:
                        position_of_11 = computer_cards.index(11)
                        computer_cards[position_of_11] = 1

                print(f"        Your final cards: {user_cards}, final_score: {check_score(user_cards)}")
                print(
                    f"        computer's final cards: {computer_cards} , computer's final score:{check_score(computer_cards)}")
                game_continue = 'n'
        if game_continue == 'n':
            if check_score(computer_cards) == check_score(user_cards):
                print("It's a draw")
            elif check_score(user_cards) > 21:
                print("You went over. You lose ")
            elif check_score(computer_cards) > 21:
                print("Computer went over. You win")
            elif check_score(user_cards) > check_score(computer_cards):
                print("Your score is higher. You win")
            elif check_score(computer_cards) > check_score(user_cards):
                print("Computer's score is higher. You lose.")
    lets_play = input("Do you want to play a game of blackjack? Type y for yes and n for no ")
    if lets_play == 'y':
        user_cards.clear()
        computer_cards.clear()

        play()


print(logo)
lets_play = input("Do you want to play a game of blackjack? Type y for yes and n for no ")

if lets_play == 'y':
    play()
