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

def check_for_blackJack(players_hand):
    if players_hand == 21:
        return False, True
    else:
        return True, False


#game setup
player_1 = Gambler()
player_1.gambler_pot()
the_house = Dealer()
new_deck = Deck()
new_deck.shuffle()

game_on = True


while game_on == True:
    bet_check = True
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
    for x in range(2):
        player_1.add_card(new_deck.deal_one())
        the_house.add_card(new_deck.deal_one())

    print("Gambler's Hand: ",player_1.all_cards[0],",", player_1.all_cards[1], "(",str(player_1.value),")")
    print("Dealer is showing: ", the_house.all_cards[1],"(",str(the_house.all_cards[1].value),")")

    hit, chicken_dinner = check_for_blackJack(player_1.value)
    bust = False

    while hit == True:
        decision = input('Do you want to HIT? (Y/N)')
        if decision == 'Y':
            player_1.add_card(new_deck.deal_one())
            if player_1.value > 21:
                if player_1.all_cards[-1].value == 11:
                    player_1.value = player_1.value - 10
                else:
                    hit = False
                    bust = True
                print('Card dealt: ', player_1.all_cards[-1])
                print('New Value:',str(player_1.value))
            elif player_1.value < 21:
                print('Card dealt: ', player_1.all_cards[-1])
                print('New Value:',str(player_1.value))
            elif player_1.value == 21:
                print('Card dealt: ', player_1.all_cards[-1])
                print('New Value:',str(player_1.value))
                hit = False
        elif decision == 'N':
            hit = False
        else:
            'You did not enter a "Y" of "N".  Please try again.'


    dealer_decision = False
    #dealer's turn to draw cards
    if bust == False and chicken_dinner == False:
        print("Dealer's turn!")
        print("Dealer is showing: ", the_house.all_cards[0],the_house.all_cards[1])
        while dealer_decision == False:
            the_house.add_card(new_deck.deal_one())
            print('Card dealt: ', the_house.all_cards[-1])
            print('New Value:',str(the_house.value))
            if the_house.value > 21:
                if the_house.all_cards[-1].value == 11:
                    the_house.value = player_1.value - 10
                else:
                    dealer_decision = True
            elif the_house.value > player_1.value:
                dealer_decision = True
            elif the_house.value >= 17:
                dealer_decision = True
            else:
                print('Dealer draws again.')

    #check who wins
    if chicken_dinner == True:
        print('Blackjack!')
        player_1.bank = player_1.bank + player_1_bet * 2
        print("You now have:", str(player_1.bank))
    elif the_house.value > 21:
        print('Dealer bust! You win!')
        player_1.bank = player_1.bank + player_1_bet * 2
        print("You now have:", str(player_1.bank))
    elif the_house.value > player_1.value:
        print('Dealer Wins!')
        print("You now have:", str(player_1.bank))
    elif player_1.value > 21:
        print('You busted!')
        print("You now have:", str(player_1.bank))
    elif player_1.value > the_house.value:
        print('You Win!')
        player_1.bank = player_1.bank + player_1_bet * 2
        print("You now have:", str(player_1.bank))
    elif player_1.value == the_house.value:
        print('A draw!')
        player_1.bank = player_1.bank + player_1_bet
        print("You now have:", str(player_1.bank))

    play_again_check = True
    while play_again_check == True:
        play_again = input('Would you like to play again? (Y/N)')
        if play_again == 'Y':
            if player_1.bank == 0:
                game_on = False
                play_again_check = False
                print('You are out of money!')
            else:
                game_on = True
                play_again_check = False
        elif play_again == 'N':
            game_on = False
            play_again_check = False
        else:
            print("You did not enter Y or N.")

    if len(new_deck.all_cards) < 10
        new_deck = Deck()

    player_1.clear_hand()
    the_house.clear_hand()
