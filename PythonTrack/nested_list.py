if __name__ == '__main__':
    # read number of students
    n = int(input())

    # create an empty list to store students' data
    students = []

    # read each student's data and add to the list
    for i in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # find the second lowest score
    scores = sorted(set([student[1] for student in students]))
    second_lowest_score = scores[1]

    # find the names of students with the second lowest score
    names = [student[0] for student in students if student[1] == second_lowest_score]

    # sort the names and print them
    for name in sorted(names):
        print(name)
