from random import shuffle
from time import sleep


def card_total(hand):
    non_aces = []
    aces = 0
    for card in hand:
        if card == 'Ace':
            aces += 1
        else:
            non_aces.append(card)
    total = sum(non_aces)
    if aces == 0:
        return total
    elif aces == 1:
        if total == 10:
            return 21
        elif total < 10:
            return total + 11
        else:
            return total + 1
    elif aces == 2:
        if total == 9:
            return 21
        elif total < 9:
            return total + 12
        else:
            return total + 2
        return 21
    elif aces == 3:
        if total == 8:
            return 21
        elif total < 8:
            return total + 13
        else:
            return total + 3
    else:
        if total == 7:
            return 21
        elif total < 7:
            return total + 14
        else:
            return total + 4


def deal(hand, deck):
    hand.append(deck.pop())


def dealer_call(dealer, deck):
    print('dealer\'s play')
    total = card_total(dealer)
    print(dealer, ' --> ', total)
    while total < 17:
        sleep(.500)
        deal(dealer, deck)
        total = card_total(dealer)
        print(dealer, ' --> ', total)

    if total > 21:
        print('The dealer has busted!')


def players_input(you, deck):
    while True:
        response = input('Would you like another card? ')
        print()
        if response.lower().strip() == 'yes':
            deal(you, deck)
            print(you)
            print(card_total(you))
            if card_total(you) > 21:
                print('You have busted!')
                break
        elif response.lower().strip() == 'no':
            break
        else:
            print('invalid input')


def winner(you, dealer):
    if card_total(dealer) == 21:
        print('The dealer has won!')
    elif card_total(you) == 21:
        print('You are the winner!')
    elif card_total(dealer) > 21:
        print('You are the winner!')
    elif card_total(you) > 21:
        print('Dealer won...')
    elif card_total(dealer) > card_total(you) and card_total(dealer) <= 21:
        print('The dealer has won!')
    elif card_total(you) > card_total(dealer) and card_total(you) <= 21:
        print('You are the winner!')
    elif card_total(you) == card_total(dealer):
        print('Tied Game!')


def blackjack():
    # the_cards = {'King': 10, 'Queen': 10, 'Jack': 10}

    deck = [
        'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7,
        6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10,
        10, 10, 9, 8, 7, 6, 5, 4, 3, 2
    ]

    shuffle(deck)
    you = []
    dealer = []

    while True:
        deal(dealer, deck)
        deal(dealer, deck)
        deal(you, deck)
        deal(you, deck)
        break
    print("Your Hand {}\nTotal: {}".format(you, card_total(you)))
    print()
    print("Dealer's Hand [{},?]".format(dealer[1]))
    print()

    players_input(you, deck)
    # if card_total(you) <= 21:
    dealer_call(dealer, deck)
    winner(you, dealer)
    print()
    print("Your Total: {}\nThe Dealers Total: {}".format(
        card_total(you), card_total(dealer)))


def main():
    # while True:
    blackjack()


if __name__ == '__main__':
    main()
