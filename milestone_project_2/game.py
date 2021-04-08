from blackjack import Card, Deck, Hand, Chips

'''
    GAME FUNCTIONS
'''
playing = True

def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Please, provide an integer")
        else:
            if chips.bet > chips.total:
                print("You don't have enough chips! you have: {}".format(chips.total))
            else:
                break

def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while playing:
        x = input('Hit or Stand? Enter h or s ')
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands, Dealer's turn")
            playing = False
        else:
            print("Please, enter h (hit) or s (stand) only")

def show_some(player, dealer):

    print("\nDealer's hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("\nDealer's hand:",*dealer.cards, sep='\n')
    print(f"Value of Dealer's hand is: {dealer.value}")
    print("\nPlayer's hand:",*player.cards, sep='\n')
    print(f"Value of Player's hand is: {player.value}")

def player_busts(player, dealer, chips):
    print("DEALER WINS! PLAYER BUSTED!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("PLAYER WINS! DEALER BUSTED!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and player tie! PUSH!")

'''
    GAME LOOP
'''

while True:

    print("WELLCOME TO BLACKJACK")

    #create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up plauer's chips
    player_chips = Chips()

    # prompt the player for their bet
    take_bet(player_chips)

    # show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:
        # prompt for player to hit or stand
        hit_or_stand(deck, player_hand)

        # show some cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # if player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

        # if player hasn't busted, play dealer's hand until dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
            
            show_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)
        
    print("\nPlayer total chips are at: {}".format(player_chips.total))

    new_game = input("Would you like to play another hand? y/n: ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break     
    
