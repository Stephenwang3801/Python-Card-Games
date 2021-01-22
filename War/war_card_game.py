import random

#Declaring global sets and dictionaries for set suits, ranks, and corresponding values
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#Defining deck and card classes
class card:

    #Initializing card object with a corresponding randomly generated suit, rank and, value
    def __init__(self, suit, rank): 
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    #Printing card values
    def __str__(self):
        return self.rank+ ' of ' + self.suit

class deck:
    
    #Initializing deck object with a card holding list
    def __init__(self):
        self.contents = []

    #Deals card by popping off the end
    def deal_card(self):
        return self.contents.pop()

    #Appends cards to the deck object
    def add_cards(self, addition):
        for card in addition:
            self.contents.append(card)

#Initializing program loop
game_over = False
    
#Game intro
print('War the card game simulation:')
print('- 2 Players, each player starts with 27 cards.')
print('- Every round, a car from each deck will be draw and compared.')
print('- Player with the larger card takes both.')
print('- In the case of a tie, more cards are drawn to break stalemate.')
print('- Runs until one deck (the loser) runs out.')   

#create parent deck and player decks
main_deck = deck()
player1_deck = deck()
player2_deck = deck()

#load up main deck and shuffle
for suit in suits:
    for rank in ranks:
        new_card = card(suit, rank)
        main_deck.contents.append(new_card)
random.shuffle(main_deck.contents)

    #dealing cards to player decks
for i in range(0, 26):
    player1_deck.contents.append(main_deck.deal_card())
    player2_deck.contents.append(main_deck.deal_card())

    #Initializing Game loop
round = 0
while game_over == False:
    war = True
    cards = []
    round += 1
    print('Round: {} \tPlayer1: {} \tPlayer2: {}'.format(round, len(player1_deck.contents), len(player2_deck.contents)))
    cards.append(player1_deck.deal_card())
    print('Player1: {}'.format(cards[0]))
    cards.append(player2_deck.deal_card())
    print('Player2: {}'.format(cards[1]))
        
    #Checking for war scenario and 
    while war:
        if cards[0].value > cards[1].value:
            print('(P1 takes the round)\n________________________________________________________________')
            for i in cards:
                player1_deck.contents.append(i)
            war = False

        elif cards[0].value < cards[1].value:
            print('(P2 takes the round)\n________________________________________________________________')
            for i in cards:
                player2_deck.contents.append(i)
            war = False
        else:
            print('WAR!')
            commence = True
            war = False
            while commence:
                if (len(player1_deck.contents) < 1):
                    print('Player 2 has won!\n________________________________________________________________')
                    commence = False
                    game_over = True
                    run = False  
                elif (len(player2_deck.contents) < 1):
                    print('Player 1 has won!\n________________________________________________________________')
                    commence = False
                    game_over = True
                    run = False  
                else:
                    cards.append(player1_deck.deal_card())
                    cards.append(player2_deck.deal_card())
                    print('Player1 has dealt: {}\t|\tPlayer2 has dealt: {}'.format(cards[-2], cards[-1]))
                    if(cards[-2].value > cards[-1].value):
                        print('\nPlayer 1 has won the war!')
                        player1_deck.add_cards(cards)
                        commence = False
                    elif(cards[-2].value < cards[-1].value):
                        print('\nPlayer 2 has won the war!')
                        player2_deck.add_cards(cards)
                        commence = False
            print('________________________________________________________________')

        if len(player1_deck.contents) == 0:
            print('Player 2 has won!\n________________________________________________________________')
            game_over = True
        elif len(player2_deck.contents) == 0:
            print('Player 1 has won!\n________________________________________________________________')
            game_over = True
        else:
            continue

        
        
               
                


        