import os, art
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    card=random.choice(cards)
    return card
def calculate_score(cardss): 
    if sum(cardss)==21 and len(cardss)==2:
        return 0
    if 11 in cardss and sum(cardss)>21:
            cardss[cardss.index(11)]=1
    return sum(cardss)
def compare(us,co):
    if us==co:
        return "Draw"
    elif co==0:
        return "Lose, opponent has Blackjack"
    elif us==0:
        return "You Win with a Blackjack"
    elif us>21:
        return "You went over. You lose"
    elif co>21:
        return "Computer went over. You win"
    elif us>co:
        return "You win"
    else:
        return "You lose"
def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over=False
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        b=calculate_score(user_cards)
        c=calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {b}")
        print(f"    Computer's first cards: {computer_cards[0]}")
        if b==0 or c==0 or b>21:
            is_game_over=True
        else:
            user_deal=input("Type 'y' to get another card, type 'n' to pass: ")
            if user_deal=="y":
                user_cards.append(deal_card())
            else:
                is_game_over=True
    while c!=0 and c<17:
        computer_cards.append(deal_card())
        c=calculate_score(computer_cards)
    print(f"     Your final hand: {user_cards}, finnal score: {b}")
    print(f"    Computer's final hand: {computer_cards}, final score: {c}")
    print(compare(b,c))
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y":
    clear_screen()
    play_game()
    
