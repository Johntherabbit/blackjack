from random import shuffle


def deal():
    cards = [
        13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5,
        4, 3, 2, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12, 11, 10, 9, 8,
        7, 6, 5, 4, 3, 2
    ]
    shuffle(cards)
    deck_1 = cards[26:]
    pile_1 = []
    deck_2 = cards[:26]
    pile_2 = []
    #cards = []

    while True:
        x = deck_1.pop()
        y = deck_2.pop()

        print(
            "Player 1: Drew {}\nLength of Hand: {}\nvs\nPlayer 2: Drew {}\nLength of Hand: {}".
            format(x, len(deck_1), y, len(deck_2)))
        print()
        input()
        #cards.extend([x, y])

        if len(deck_1) == 0:
            shuffle(pile_1)
            deck_1 = pile_1.copy()
            pile_1 = []
            print('Player two wins!')
            return

        elif len(deck_2) == 0:
            shuffle(pile_2)
            deck_2 = pile_2.copy()
            pile_2 = []
            print('Player one wins!')
            return

        elif x > y:
            pile_1.extend([x, y])
        elif x < y:
            pile_2.extend([x, y])

    #while True:


#
#    x = deck_1.pop()
#    y = deck_2.pop()
#
#    print("Player 1: Drew {}\nvs\nPlayer 2: Drew {}".format(x, y))
#    print()
#    input()
#    if deck_1 == []:
#        print('$$$$$$$$')
#        print('Player 2 Wins!')
#        print('$$$$$$$$')
#        print()
#        return
#    elif deck_2 == []:
#        print('$$$$$$$$')
#        print('Player 1 Wins!')
#        print('$$$$$$$$')
#        print()
#        return
#    elif x > y:
#        deck_1.extend([x, y])
#    elif x < y:
#        deck_2.extend([x, y])


def main():

    deal()


if __name__ == '__main__':
    main()
