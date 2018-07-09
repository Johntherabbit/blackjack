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
        print()

    if total > 21:
        print('The dealer has busted!')
        print()


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


# betting has been left out until multiplayer betting has improved
def winner(you, dealer):  #, total_cash, money):
    if card_total(dealer) == 21:
        print('The dealer has won!')
        #total_cash.remove(money)
    elif card_total(you) == 21:
        #total_cash.append(money)
        print('You are a winner!')
    elif card_total(you) > 21:
        #total_cash.remove(money)
        print('The dealer has won!')
    elif card_total(dealer) > 21:
        #total_cash.append(money)
        print('You are a winner!')
    elif card_total(dealer) > card_total(you) and card_total(dealer) <= 21:
        #total_cash.remove(money)
        print('The dealer has won!')
    elif card_total(you) > card_total(dealer) and card_total(you) <= 21:
        #total_cash.append(money)
        print('You are a winner!')
    elif card_total(you) == card_total(dealer):
        print('You will be refunded your money so you can try again ')
        print('Tied Game!')
    print()
    #collect_money(total_cash)


def collect_money(total_cash):
    if sum(total_cash) > 0:
        print('Collect your earnings: ${}'.format(sum(total_cash)))
    else:
        print('Whoops, looks like you lost your bet!')


def bet_placing():
    while True:
        response = input('How much would you like to bet? >>> ')
        if response.isdigit() == False:
            print('Not a valid number.')
        elif int(response) > 20:
            print('Price is too high, please stay within the $20 limit.')
        elif int(response) == 0:
            print('You must place a bet to play.')
        elif int(response) > 1 and int(response) <= 20:
            return int(response)


def multiplayer():
    while True:
        response = input(
            'Press s for singleplayer, or press m for multiplayer >>> ')
        if response == 's':
            blackjack()
            play_again()
            return None
        elif response == 'm':
            multiplayer_blackjack()
            play_again()
            return None
        else:
            print('Please provide a valid answer.')


def multiplayer_blackjack():
    deck = [
        'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7,
        6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10,
        10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3,
        2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8,
        7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10,
        10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3,
        2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8,
        7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10,
        10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3,
        2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8,
        7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10,
        10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3,
        2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8,
        7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10,
        10, 10, 9, 8, 7, 6, 5, 4, 3, 2
    ]

    shuffle(deck)
    players = [[], []]
    dealer = []

    while True:
        deal(dealer, deck)
        deal(dealer, deck)

        for player in players:
            deal(players[0], deck)
            deal(players[0], deck)
            deal(players[1], deck)
            deal(players[1], deck)
            break
        break
    print(".....\nPlayer one's Hand {}\nTotal: {}\n".format(
        players[0], card_total(players[0])))
    players_input(players[0], deck)
    print(".....\nPlayer two's Hand {}\nTotal: {}\n".format(
        players[1], card_total(players[1])))
    print("Dealer's Hand [{},?]\n".format(dealer[1]))
    players_input(players[1], deck)
    dealer_call(dealer, deck)
    print(
        "\n.....\nPlayer one:\nTotal: {}\nThe Dealers Total: {}\n".format(
            card_total(players[0]), dealer), card_total(dealer))
    winner(players[0], dealer)
    print(
        "\n.....\nPlayer two:\nTotal: {}\nThe Dealers Total: {}\n".format(
            card_total(players[1]), dealer), card_total(dealer))
    winner(players[1], dealer)


def blackjack():
    deck = [
        'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7,
        6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10,
        10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3,
        2, 'Ace', 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2
    ]

    shuffle(deck)
    you = []
    dealer = []
    total_cash = []

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
    #money = bet_placing()
    #total_cash.append(money)

    players_input(you, deck)
    dealer_call(dealer, deck)
    winner(you, dealer)  #, total_cash, money)
    print()
    print("This Game\'s Results\nYour Total: {}\nThe Dealers Total: {}".format(
        card_total(you), card_total(dealer)))


def play_again():
    print()
    while True:
        response = input('Would you like to play again? ')
        if response == 'yes':
            blackjack()
        elif response == 'no':
            break


def multiplayer_play_again():
    print()
    response = input('Would you all like to play again? ')
    while True:
        if response == 'yes':
            multiplayer_blackjack()
            return None
        elif response == 'no\n.....':
            break


def main():
    multiplayer()


if __name__ == '__main__':
    main()
