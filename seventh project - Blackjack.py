logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
import replit


def deal_to_user():
    for _ in range(2):
        users_hand.append(random.choice(cards))
    return users_hand


def score_calculator(hand):
    score = 0
    for card in hand:
        score += card
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score_calculator(hand)
        return score
    return score


def deal_to_pc():
    for _ in range(2):
        pc_hand.append(random.choice(cards))
    return pc_hand


def scoreboard(user, pc):
    print(f"Your cards: {user}, current score: {score_calculator(user)}\n")

    print(f"Dealer's first card: {pc}\n\n")


def users_final_hand(hand):
    another_card = input("Type 'y' to get another card, or 'n' to pass. ")

    if another_card == 'n':
        return hand

    elif another_card == 'y':
        hand.append(random.choice(cards))
        scoreboard(hand, pc_hand[0])
        users_final_hand(hand)
        return hand


    else:
        print("Please enter 'y' for yes or 'n' for no. ")
        users_final_hand(hand)
        return hand


def pc_final_hand(pcs_hand):
    if score_calculator(pcs_hand) < 17:
        pcs_hand.append(random.choice(cards))
        pc_final_hand(pcs_hand)
        return pcs_hand


    else:
        return pcs_hand


def result_decider(user_score, pc_score):
    if user_score == 21:
        print("Blackjack! You won. ")
    elif pc_score == 21:
        print("You lost. The Dealer has a Blackjack. ")
    elif user_score > 21:
        print("You went over, you lose. ")
    elif pc_score > 21:
        print("You win! The dealer went over. ")
    elif user_score == pc_score:
        print("Its a draw. ")
    elif user_score > pc_score:
        print("You win! Your score is higher. ")
    else:
        print("You lost. ")


continue_game = True
while continue_game:
    ans = input("Would you like to play a game of Blackjack? type 'y' or 'n'. ")
    if ans == 'n':
        continue_game = False
    elif ans == 'y':
        replit.clear()
        print(logo)
        users_hand = []
        pc_hand = []
        deal_to_user()
        deal_to_pc()

        scoreboard(users_hand, pc_hand[0])
        final_pc_hand = pc_final_hand(pc_hand)
        final_user_hand = users_final_hand(users_hand)
        final_user_score = score_calculator(final_user_hand)
        final_pc_score = score_calculator(final_pc_hand)

        print(f"Your  final cards: {final_user_hand}, final score: {final_user_score}\n")

        print(f"Dealer's final cards: {final_pc_hand}, final score: {final_pc_score}\n")

        result_decider(final_user_score, final_pc_score)


    else:
        print("Please enter 'y' for yes or 'n' for no.")
