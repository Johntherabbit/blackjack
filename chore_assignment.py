from random import shuffle


def main():
    class_of_2018 = [
        'Cole Anderson', 'Timothy Bowling', 'Logan Harrell', 'Desma Hervey',
        'Ginger Keys', 'Matt Lipsey', 'Myeisha Madkins', 'Henry Moore',
        'John Morgan', 'Irma Patton', 'Danny Peterson', 'Jakylan Standifer',
        'Justice Taylor', 'Ray Turner', 'Cody van der Poel', 'Andrew Wheeler'
    ]

    chores = [
        'Take out classroom trash', 'Sweep classroom Wednesday',
        'Sweep classrom Friday', 'Sweep Hallway Wednesday',
        'Sweep Hallway Friday', 'Clean bathroom 1', 'Clean bathroom 2',
        'Take out kitchen trash.', 'Sweep stairs Wednesday',
        'Sweep stairs Friday', 'set up lunch Monday', 'set up lunch Tuesday',
        'set up lunch Wednesday', 'set up lunch Thursday',
        'Set up lunch Friday', 'Just dance or something'
    ]

    shuffle(chores)

    for name in class_of_2018:
        print("Student: {}\nChore: {}".format(name, chores.pop()))
        print()
    return


if __name__ == '__main__':
    main()
