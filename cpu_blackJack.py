#Blackjack
#computer runs blackjack 100 times

import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
'Jack','Queen','King','Ace')

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,
'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}


class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self):
        self.all_cards = []
        for x in range(6):
            for suit in suits:
                for rank in ranks:
                    created_card = Card(suit,rank)
                    self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

class Gambler:
    def __init__(self,bank=0.00,value=0):
        self.bank = bank
        self.all_cards = []
        self.value = value

    def gambler_pot(self):
        self.bank = float(input('How much are you playing with:'))

    def add_card(self,new_card):
        self.all_cards.append(new_card)
        self.value = self.value + self.all_cards[-1].value

    def clear_hand(self):
        self.all_cards = []
        self.value = 0

    def __str__(self):
        return 'The Gambler has $' + str(self.bank) + ' in his account.'

class Dealer:
    def __init__(self,bank=0.00,value=0):
        self.bank = bank
        self.all_cards = []
        self.value = value

    def add_card(self,new_card):
        self.all_cards.append(new_card)
        self.value = self.value + self.all_cards[-1].value

    def clear_hand(self):
        self.all_cards = []
        self.value = 0

def place_a_bet():
    #need to add a error check to make sure it is a integer greater than 1.
    bet = float(input('Enter a bet: '))
    return bet

def check_bet(players_bet,players_pot):
    new_players_pot = 0
    new_players_pot = players_pot - players_bet
    if new_players_pot < 0:
        return True
    else:
        return False

def initial_deal_cards(player_1,rivers,new_deck):
    pass


#game setup
player_1 = Gambler()
#player_1.gambler_pot()
the_house = Dealer()
new_deck = Deck()
new_deck.shuffle()
player_1_win_count = 0
the_house_win_count = 0
total_games_played = 0

#game_on = True
bet_check = True
counter = 0
while counter < 100:

    #deal cards
    for x in range(2):
        player_1.add_card(new_deck.deal_one())
        the_house.add_card(new_deck.deal_one())

    #print("Gambler's Hand: ",player_1.all_cards[0],",", player_1.all_cards[1], "(",str(player_1.value),")")
    #print("Dealer is showing: ", the_house.all_cards[1])

    player_stay = False
    while player_stay == False:
        if player_1.value >=17:
            if player_1.value > 21:
                player_stay = True
                player_bust = True
                the_house_win = True
            else:
                player_stay = True
                player_bust = False
        else:
            player_1.add_card(new_deck.deal_one())

    #print("Gambler's Hand: ", str(player_1.value))
    #print("Dealer is showing: ",the_house.all_cards[0],",", the_house.all_cards[1], "(",str(the_house.value),")")

    the_house_decision = False
    while player_bust == False and the_house_decision == False:
        if the_house.value > 21:
            the_house_decision = True
            the_house_win = False
        elif the_house.value < 21 and the_house.value > player_1.value:
            the_house_decision = True
            the_house_win = True
        elif the_house.value < 21 and the_house.value < player_1.value:
            the_house.add_card(new_deck.deal_one())
        elif the_house.value == player_1.value:
            the_house_win = 'Draw'
            the_house_decision = True
        elif the_house.value == 21:
            the_house_decision = True
            the_house_win = True

    if the_house_win == True:
        the_house_win_count = the_house_win_count + 1
        total_games_played = total_games_played + 1
    elif the_house_win == 'Draw':
        total_games_played = total_games_played + 1
    else:
        player_1_win_count = player_1_win_count + 1
        total_games_played = total_games_played + 1


    if len(new_deck.all_cards) < 20:
        new_deck = Deck()
        new_deck.shuffle()
    else:
        player_1.clear_hand()
        the_house.clear_hand()

    counter = counter + 1

    #game_on = False

print("The gambler won ", str(player_1_win_count)," hands.")
print("The dealer won ", str(the_house_win_count)," hands.")
print("The number of draws were",str(total_games_played-the_house_win_count-player_1_win_count))
print("A total of ", str(total_games_played)," hands were played.")
