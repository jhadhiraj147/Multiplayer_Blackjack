from random import randint
class Card:
    def __init__(self):
        self.rank = randint(1, 13)

    def get_card_name_and_value(self):
        match self.rank:
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
                card_name = "a " + str(self.rank)
                card_value = self.rank
        print(f"Drew {card_name}")
        return card_value


class Player:
    def __init__(self, name):
        self.name = name
        self.hand_value = 0
        self.score = 3

    def draw_starting_hand(self):
        self.hand_value = Card().get_card_name_and_value() + Card().get_card_name_and_value()
        return self.hand_value

    def take_turn(self):
        print("-----------")
        print(f"{self.name.upper()}'S TURN")
        print("-----------")
        self.hand_value = self.draw_starting_hand()
        while self.hand_value < 21:
            another_card = input(f"You have {self.hand_value}. Hit (y/n)? ")
            if another_card == "y":
                self.hand_value += Card().get_card_name_and_value()
            elif another_card == "n":
                break
            else:
                print("Sorry, I didn't get that.")
        print(f"Final hand: {self.hand_value}")
        if self.hand_value == 21:
            print('BLACKJACK!')
        elif self.hand_value > 21:
            print('BUST.')
        return self.hand_value


class Dealer(Player):
    def take_turn(self):
        print("-----------")
        print("DEALER TURN")
        print("-----------")
        self.hand_value = self.draw_starting_hand()
        print(f"Dealer has {self.hand_value}.")
        while self.hand_value < 17:
            self.hand_value += Card().get_card_name_and_value()
        print(f"Final hand: {self.hand_value}")
        if self.hand_value == 21:
            print('BLACKJACK!')
        elif self.hand_value > 21:
            print('BUST.')
        return self.hand_value


class BlackjackGame:
    def __init__(self):
        self.players = []
        self.dealer = Dealer("Dealer")

    def setup_game(self):
        no_of_players = int(input("Welcome to Blackjack! How many players? "))
        while no_of_players <= 0:
            no_of_players = int(input("Number of players must be at least 1. Enter the number of players again: "))
        for i in range(1, no_of_players + 1):
            name = input(f"What is player {i}'s name? ")
            self.players.append(Player(name))

    def check_results(self, player, dealer_final_hand):
        if player.hand_value <= 21 and (player.hand_value > dealer_final_hand or dealer_final_hand > 21):
            player.score += 1
            print(f"{player.name} wins! Score: {player.score}")
        elif player.hand_value > 21 or (dealer_final_hand <= 21 and dealer_final_hand > player.hand_value):
            player.score -= 1
            print(f"{player.name} loses! Score: {player.score}")
        else:
            print(f"{player.name} pushes. Score: {player.score}")

    def play_round(self):
        eliminated_players = []
        for player in self.players:
            player.take_turn()

        dealer_final_hand = self.dealer.take_turn()

        print("-----------")
        print("GAME RESULT")
        print("-----------")

        for player in self.players:
            self.check_results(player, dealer_final_hand)
            if player.score == 0:
                print(f"{player.name} eliminated!")
                eliminated_players.append(player)

        for player in eliminated_players:
            self.players.remove(player)

        if len(self.players) == 0:
            print("All players eliminated!")

    def start_game(self):
        self.setup_game()
        play_again = True
        while play_again and len(self.players) > 0:
            self.play_round()
            if len(self.players) == 0:
                break
            play_again_question = input("Do you want to play another hand (y/n)? ")
            play_again = play_again_question == "y"



game = BlackjackGame()
game.start_game()

