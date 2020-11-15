#Blackjack
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
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()

class Gambler:
    def __init__(self,bank=0.00,hand=[],value=0):
        self.bank = bank
        self.hand = hand
        self.value = value

    def gambler_pot(self):
        self.bank = float(input('How much are you playing with:'))

    

    def clear_hand(self):
        pass

    def __str__(self):
        return 'The Gambler has $' + str(self.bank) + ' in his account.'

class Dealer:
    def __init__(self,bank=0.00,hand=[]):
        self.bank = bank
        self.hand = hand

    def clear_hand(self):
        pass

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
    for x in range(2):
        player_1.hand.append(new_deck.deal_one())
        rivers.hand.append(new_deck.deal_one())
    for x,player_1.hand in enumerate(player_1.hand):
        player_1.value = player_1.hand.value + player_1.value
    print(player_1.hand[0])
    print(str(player_1.hand))
    return player_1,rivers,new_deck

def hit_or_stay(my_hand,deck):
    my_hand_value = 0
    for x,my_hand in enumerate(my_hand):
        my_hand_value = my_hand.value + my_hand_value
    print('Current Value:',str(my_hand_value))
    hit = True
    while hit == True:
        decision = input('Do you want to HIT or STAY? (Y/N)')
        if decision == 'Y':
            my_hand.append(deck.deal_one())
            my_hand_value = my_hand[-1].value + my_hand_value
            print('Current Value:',str(my_hand_value))
            #my_hand,deck = hit_me(my_hand,deck)
            #check_hand_value
        elif decision == 'N':
            hit = False
        else:
            'You did not enter a "Y" of "N".  Please try again.'
    return my_hand, deck

def hit_me(my_hand,deck):
    my_hand_value = 0
    #my_hand.append(deck.deal_one())
    for y,my_hand in enumerate(my_hand):
    #    my_hand_value = my_hand.value + my_hand_value
        print(my_hand)
    return my_hand,deck

def dealer_draws():
    pass

def results():
    pass

def play_again():
    pass

#game setup
player_1 = Gambler()
player_1.gambler_pot()
rivers = Dealer()
new_deck = Deck()
new_deck.shuffle()

game_on = True
bet_check = True

while game_on == True:

    while bet_check == True:
        #loop to make sure bet is under amount in the bank
        player_1_bet = place_a_bet()
        #print(str(player_1_bet))
        bet_check = check_bet(player_1_bet,player_1.bank)
        if bet_check == True:
            print('Oops! You do not have that much in your pot!  Enter a different amount.')
        else:
            player_1.bank = player_1.bank - player_1_bet
            print("Let's Play! You're bank is now $",str(player_1.bank))

    #deal cards
    player_1, rivers, new_deck = initial_deal_cards(player_1,rivers,new_deck)
    print("Gambler's Hand: ", player_1.hand[0],',' ,player_1.hand[1])
    print("Dealer's Hand: ", rivers.hand[1])
    #print(len(new_deck.all_cards))

    #ask player if they want to hit or stay
    #player_1.hand, new_deck = hit_or_stay(player_1.hand,new_deck)
    #print(len(new_deck.all_cards))
    hit = True
    while hit == True:
        decision = input('Do you want to HIT or STAY? (Y/N)')
        if decision == 'Y':
            player_1.hand.append(new_deck.deal_one())
            player_1.hand.value = player_1.hand[-1].value + player_1.value
            print('Current Value:',str(my_hand_value))
            #my_hand,deck = hit_me(my_hand,deck)
            #check_hand_value
        elif decision == 'N':
            hit = False
        else:
            'You did not enter a "Y" of "N".  Please try again.'



    game_on = False
