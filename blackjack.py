from random import shuffle


def deal(list, deck):
    list.append(deck.pop())


def dealer_call(dealer, deck):
    total = sum(dealer)
    if total < 17:
        return deal(dealer, deck)
    elif total >= 17:
        return total


def players_input(you, deck):
    while True:
        response = input('Would you like another card? ')
        if response == 'yes':
            return deal(you, deck)
            print(you)


def main():
    deck = [
        11, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 10, 10, 10, 9, 8, 7, 6, 5,
        4, 3, 2, 11, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11, 10, 10, 10, 9, 8,
        7, 6, 5, 4, 3, 2
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
    print("Your Hand {}".format(you))
    print("Dealer's Hand [{},?]".format(dealer[1]))

    dealer_call(dealer, deck)
    players_input(you, deck)


if __name__ == '__main__':
    main()
