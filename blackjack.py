# Single player blackjack game
# Created by Dhruv Dange using python 3

from random import shuffle, randint
import time
import os

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'King':10, 'Queen':10, 'Jack':10, 'Ace':11}
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'King', 'Queen', 'Jack', 'Ace']

# Defination 
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

    def display_card(self):
        print(f"\t{self.rank} of {self.suit}")
    
    def hide_card(self):
        print("\t[Card Face Down]")
    
class Deck:

    def __init__(self):
        self.deck_cards = []

        for suit in suits:
            for rank in ranks:
                x = Card(suit, rank)
                self.deck_cards.append(x)
    
    def __str__(self):
        for x in self.deck_cards:
            x.display_card()
    
    def shuffle_deck(self):

        shuffle(self.deck_cards)
    
    def draw_card(self):
        card_pos = randint(0,51)
        return self.deck_cards[card_pos]



def rules():
    os.system("cls")
    req_inp = ['y','n']
    option = 'x'
    
    print("WELCOME TO BLACKJACK!!")
    print("This is a single player version of Blackjack!")
    print("Do you want to learn how to play?\n")
    while option not in req_inp:
        option = input("Enter y/n:  ")
    if option == 'y':
        print("\nThese are the rules for blackjack: ")
        print("1. Bet a certain amount of chips. Everyone starts with 100 chips.")
        print("2. You will be given two cards initially and can request additional cards.")
        print("3. Try to reach a total value of 21 or less while beating the dealer to it.")
        print("4. Go above 21 and you bust i.e. Game Over!")
        print("5. Win and earn double your bet. Lose and try again.")
        input("Press any key to continue...")
    print("\nLets play")
    

class Hands:

    def __init__(self):
        self.game_hand = Deck()
        self.game_hand.shuffle_deck()
        self.player_cards = []
        self.dealer_cards = []
        self.player_card_values = 0
        self.dealer_card_values = 0
        self.player_chips = 100
        self.bet = 0
        self.player_cards.append(self.game_hand.draw_card())
        self.player_cards.append(self.game_hand.draw_card())
        self.dealer_cards.append(self.game_hand.draw_card())
        self.dealer_cards.append(self.game_hand.draw_card())


    def __str__(self):
        print(self.game_hand) 
    
    def display_hand(self,x ):
        os.system("cls")
        print("This is the dealers hand: ")
        if x == 1:
            self.dealer_cards[0].display_card()
            self.dealer_cards[1].hide_card()
            print("\n\n")
        else:
            for card in self.dealer_cards:
                card.display_card()
        print("\nPlayer, this is your hand: ")
        for card in self.player_cards:
            card.display_card()
            
    def get_card_values(self, deck, val):
        ace_card = 0
        val = 0
        for x in deck:
            val += x.value
            if x.value == 11:
                ace_card = 1
        if val > 21:
            if ace_card == 1:
                val = val - 10
                ace_card = 0
                print("Ace card value taken as 1")
        return val

    def dealer_hand(self):
        self.display_hand(2)
        self.dealer_card_values = self.get_card_values(self.dealer_cards, self.dealer_card_values)
        while self.dealer_card_values < 21:
            if self.player_card_values >= self.dealer_card_values and self.dealer_card_values < 21:
                os.system("cls")
                self.dealer_cards.append(self.game_hand.draw_card())
                self.display_hand(2)
                self.dealer_card_values = self.get_card_values(self.dealer_cards, self.dealer_card_values)
                continue
            elif self.dealer_card_values > self.player_card_values and self.dealer_card_values < 21:
                print("Dealer Wins!!")
                self.update_chips(0)
            elif self.player_card_values > self.dealer_card_values and self.player_card_values < 21:
                print("You win!!")
                self.update_chips(1)
        if self.dealer_card_values >= 21:
            if self.dealer_card_values > 21 and self.player_card_values <= 21:
                print("Dealer bust! You win")
                self.update_chips(1)
            elif self.dealer_card_values == 21:
                print("Dealer Blackjack")
                self.update_chips(0)
        

    def player_hand(self):
        req_inp = ['y','n']
        option = 0
        print(f"Current number of chips: {self.player_chips}")
        self.bet = int(input("Enter bet amount: "))
        while self.bet > self.player_chips:
            print("Invalid bet amount.  Please enter again.")
            self.bet = int(input("Enter bet amount: "))
        os.system("cls")
        self.display_hand(1)
        self.player_card_values = self.get_card_values(self.player_cards, self.player_card_values)
        while option not in req_inp:
            option = input("Do you want another card? y/n ")
            if option == 'y':
                self.player_cards.append(self.game_hand.draw_card())
                self.display_hand(1)
                self.player_card_values = self.get_card_values(self.player_cards, self.player_card_values)
                option = 0
                if self.player_card_values > 21:
                    print("Oops you busted! Better luck next time.")
                    self.update_chips(0)
                continue
            else:
                self.dealer_hand()

    def update_chips(self, outcome):
        if outcome == True:
            self.player_chips += self.bet
        elif outcome == False:
            self.player_chips -= self.bet
        
        if self.player_chips <= 0:
            print("You lost all your chips. Game Over")
            exit()
        else:
            print(f"\n\n{self.player_chips} chips left.") 
            choice = input("Do you want to play again? y/n ")
            if choice == 'y':
                self.reset()
                self.player_hand()
            elif choice == 'n': 
                exit()
            
    def reset(self):
        self.dealer_card_values = 0
        self.player_card_values = 0
        self.player_cards = []
        self.dealer_cards = []
        self.game_hand.shuffle_deck()
        self.player_cards.append(self.game_hand.draw_card())
        self.player_cards.append(self.game_hand.draw_card())
        self.dealer_cards.append(self.game_hand.draw_card())
        self.dealer_cards.append(self.game_hand.draw_card())

        
rules()
game_init = Hands()
game_init.player_hand()