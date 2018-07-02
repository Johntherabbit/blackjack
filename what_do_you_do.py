def print_options():
    print('Who would you like to know about?')
    print()
    print(
        'Glen Evans\nKagan Coughlin\nBethany Cooper\nSage Nichols\nJohn Marsalis\nCarla Lewis\nSean Anthony\nNate Clark'
    )
    print()


def search_person(persons):
    for name in persons:
        response = input('Enter a name ')
        if response in persons:
            print(response, persons[response])
            print()
        else:
            print('Invalid response')


def main():
    persons = {
        'Glen Evans': 'co-founder',
        'Kagan Coughlin': 'co-founder',
        'Bethany Cooper': 'founding trustee',
        'Sage Nichols': 'founding trustee',
        'John Marsalis': 'founding trustee',
        'Carla Lewis': 'trustee',
        'Sean Anthony': 'director',
        'Nate Clark': 'technical director'
    }
    print_options()
    search_person(persons)


if __name__ == '__main__':
    main()
