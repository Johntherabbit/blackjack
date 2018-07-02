def input_grades():
    grades = []
    print("Enter your grades, enter 'grade' to grade or 'quit' to quit.")
    while True:
        response = input("Enter a grade: ")
        if response == 'quit':
            break
        elif response == 'grade':
            average = round(float(sum(grades) / len(grades)), 2)
            return average
        else:
            grades.append(int(response))


def final_grade(average):
    if average >= 90.0:
        print("Your average is {} and your final grade is {}".format(
            average, 'A'))
    elif average >= 80.0:
        print("Your average is {} and your final grade is {}".format(
            average, 'B'))
    elif average >= 70.0:
        print("Your average is {} and your final grade is {}".format(
            average, 'C'))
    elif average >= 65.0:
        print("Your average is {} and your final grade is {}".format(
            average, 'D'))
    elif average < 65.0:
        print("Your average is {} and your final grade is {}".format(
            average, 'F'))


def main():
    average = input_grades()
    final_grade(average)


if __name__ == '__main__':
    main()
