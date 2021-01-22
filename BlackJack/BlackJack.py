import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

class deck:
    def __init__(self):
        self.contents = []

    def deal_card(self):
        return self.contents.pop()
    
    def shuffle(self):
        random.shuffle(self.contents)

    def show(self):
        for x in self.contents:
            print("\t{}".format(x))

    def card_num(self):
        return len(self.contents)

    def get_value(self):
        total = 0
        for x in self.contents:
            total += x.value
        return total


class wallet:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.balance = self.balance - amount


while True:
    try:
        balance = int(input('Please enter wallet amount in dollars: '))
    except ValueError:
        print('Sorry')
    else:
        if balance <= 0:
            print('Your balance cannot be zero or less.')
        else:  
            break
p_bal = wallet(balance)


run = True
round = 0
while run:

    round += 1
    bet_amt = 0
    player = deck()
    dealer = deck()
    main_deck = deck()
    round_on = True
    proceed = False
    decision = ' '
    print('________________________________________')
    print("ROUND: {}".format(round))

    while True:
        try:
            bet_amt = int(input('Enter a bet amount: '))
        except ValueError:
            print('Sorry')
        else:
            if bet_amt > p_bal.balance:
                print('You do not have enough.')
            else:
                break

    for suit in suits:
        for rank in ranks:
            new_card = card(suit, rank)
            main_deck.contents.append(new_card)
    main_deck.shuffle()
    
    
    for x in range(0,2):
        player.contents.append(main_deck.deal_card())
        dealer.contents.append(main_deck.deal_card())

    print('________________________________________')
    print("You've been dealt: ")
    player.show()
    print("Value: {}".format(player.get_value()))
    print('________________________________________')
    print()
    print("The dealer has: ")
    print(f'\t{dealer.contents[0]}')
    print("\tUNKNOWN CARD")
    print("Value: ???")
    print('________________________________________')

    while round_on:
        while proceed == False:
            try: 
                decision = int(input('Hit (1) or Stay (2)?: '))
            except ValueError:
                print('Sorry?')
            else:
                if decision == 1:
                    player.contents.append(main_deck.deal_card())
                    proceed = False
                    print('Your cards now:')
                    player.show()
                    print("Value: {}".format(player.get_value()))
                    print('________________________________________')
                elif decision == 2:
                    proceed = True
                else:
                    print('Sorry?')

        if player.get_value() > 21:
            print("BUST! And you've lost {}".format(bet_amt))
            p_bal.withdraw(bet_amt)
        elif player.get_value() == dealer.get_value:
            if player.get_value() == 21 and (player.card_num() > dealer.card_num()):
                print("Lost to the dealer!")
                p_bal.withdraw(bet_amt)
            else:
                print("PUSH! No money gained or Lost")
        else:
            if player.get_value() < dealer.get_value():
                print("Lost to the dealer!")
                p_bal.withdraw(bet_amt)
            else:
                print("Win! You've beaten the dealer!")
                p_bal.deposit(bet_amt)
        
        print("The Dealer Had:")
        dealer.show()
        print("You now have {}".format(p_bal.balance))
        round_on = False
        if p_bal.balance <= 0:
            print("You're broke! Good Game!")
            run = False


        





    