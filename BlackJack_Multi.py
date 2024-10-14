from random import*

def card_name_and_value(random_card_rank):
    match random_card_rank:
        case 1:
            card_name = "an Ace"
            card_value = 11
        case 11:
            card_name = "a Jack"
            card_value = 10
        case 12:
            card_name = "a Queen"
            card_value = 10
        case 13:
            card_name = "a King"
            card_value = 10
        case 8:
            card_name = "an 8"
            card_value = 8
        case _:
            card_name = "a " + str(random_card_rank)
            card_value = random_card_rank  
    print(f"Drew {card_name}")
    return card_value





def starting_hand_value():
    value = card_name_and_value(randint(1, 13)) + card_name_and_value(randint(1, 13))
    return value





def player_turn(player_name):
    print("-----------")
    print(f"{player_name}'S TURN")
    print("-----------")
    hand_value = starting_hand_value()
    another_card = "y"
    while (hand_value < 21):
        another_card = input(f"You have {hand_value}. Hit (y/n)?")
        match another_card:
            case "y":
                hand_value += card_name_and_value(randint(1, 13))
            case "n":
                break
            case _:
                print("Sorry I didn't get that.")
    print(f"Final hand: {hand_value}")
    if hand_value == 21:
        print('BLACKJACK!')
    elif hand_value > 21:
        print('BUST.')
    return hand_value




def dealer_turn():
    print("-----------")
    print("DEALER TURN")
    print("-----------")
    hand_value = starting_hand_value()
    print(f"Dealer has {hand_value}.")
    while (hand_value < 17):
        hand_value += card_name_and_value(randint(1, 13))
    print(f"Final hand: {hand_value}")
    if hand_value == 21:
        print('BLACKJACK!')
    elif hand_value > 21:
        print('BUST.')
    return hand_value




def checking_win_or_loss_and_scores_updating(player_name, player_final_hand, dealer_final_hand, players_and_their_scores, players_and_their_final_hand, eliminated_players):

    if player_final_hand <= 21 and (player_final_hand > dealer_final_hand or dealer_final_hand > 21):
        players_and_their_scores[player_name] += 1
        print(f"{player_name} wins! Score: {players_and_their_scores[player_name]}")
    elif player_final_hand > 21 or (dealer_final_hand <= 21 and dealer_final_hand > player_final_hand):
        players_and_their_scores[player_name] -= 1
        print(f"{player_name} loses! Score: {players_and_their_scores[player_name]}")    
    else:
        print(f"{player_name} pushes. Score: {players_and_their_scores[player_name]}")

    if players_and_their_scores[player_name] == 0:
        print(f"{player_name} eliminated!")
        eliminated_players.append(player_name)
        




def blackjacking():
   no_of_players = int(input("Welcome to Blackjack! How many players? "))
   while no_of_players <= 0:
       no_of_players = int(input("Number of players must be at least 1. Enter the number of players again. "))
   players_and_their_scores = {}
   players_and_their_final_hand = {}
   eliminated_players = []
   for i in range(1, no_of_players + 1):
      name = input(f"What is player {i}'s name? ")
      players_and_their_final_hand[name] = 0
      players_and_their_scores[name] = 3

   play_again = True
   while play_again:
       
       for player in players_and_their_final_hand:
           players_and_their_final_hand[player] = player_turn(player)
       dealer_final_hand = dealer_turn()
       print("-----------")
       print("GAME RESULT")
       print("-----------")
       for player in players_and_their_final_hand:
           checking_win_or_loss_and_scores_updating(player, players_and_their_final_hand[player], dealer_final_hand, players_and_their_scores, players_and_their_final_hand, eliminated_players)

       for player in eliminated_players:
           del players_and_their_scores[player]
           del players_and_their_final_hand[player]
       eliminated_players.clear()

       if len(players_and_their_final_hand) == 0:
           break    
       play_again_question = input("Do you want to play another hand (y/n)?")
       if play_again_question == "n":
           play_again = False
        
   if len(players_and_their_final_hand) == 0:
       print("All players eliminated!")
           


blackjacking()
