def input_grades():
    grades = []
    print("Enter your grades, enter 'grade' to grade or 'quit' to quit.")
    while True:
        response = input("Enter a grade: ")
        if response == 'quit':
            break
        elif response == 'grade':
            print(round(float(sum(grades) / len(grades)), 2))
            grades.clear()
        else:
            grades.append(int(response))


def main():
    input_grades()


if __name__ == '__main__':
    main()
