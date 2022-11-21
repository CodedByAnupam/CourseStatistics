# tee ratkaisu tänne
# wwite your solution here


def to_grade(ex, em):
    if (ex + em) <= 14:
        return 0
    elif ex + em <= 17:
        return 1
    elif ex + em <= 20:
        return 2
    elif ex + em <= 23:
        return 3
    elif ex + em <= 27:
        return 4
    else:
        return 5


def main():
    if True:
        # this is never executed
        file1 = input("Student information: ")
        file2 = input("Exercises completed: ")
        file3 = input("Exam points: ")
    else:
        # hard-coded input
        file1 = "students1.csv"
        file2 = "exercises1.csv"
        file3 = "exam_points1.csv"

    students = {}
    exercises = {}
    exams = {}

    with open(file1) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            if parts[0] == "id":
                continue
            students[parts[0]] = parts[1] + " " + parts[2]

    with open(file2) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            esum = 0
            if parts[0] == "id":
                continue
            for i in parts[1:]:
                esum += int(i)
            exercises[parts[0]] = esum

    with open(file3) as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            esum = 0
            if parts[0] == "id":
                continue
            for i in parts[1:]:
                esum += int(i)
            exams[parts[0]] = esum

    # print(students)
    # print(exercises)
    # print(exams)
    name = "name"
    exec_nbr = "exec_nbr"
    exec_pts = "exec_pts."
    exm_pts = "exm_pts."
    tot_pts = "tot_pts."
    grade = "grade"

    print(f"{name:30}{exec_nbr:10}{exec_pts:10}{exm_pts:10}{tot_pts:10}{grade:10}")

    for key, value in students.items():
        ex_points = int(((exercises[key] / 40) * 100) // 10)
        em_points = exams[key]

        total = ex_points + em_points
        # print(total)
        grade1 = to_grade(ex_points, em_points)
        # print(f"{ex_points} {em_points} {total} {grade1}")
        print(
            f"{students[key]:30}{exercises[key]:<10}{ex_points:<10}{em_points:<10}{total:<10}{grade1:<10}"
        )


main()
