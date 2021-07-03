print("Student marks evaluation program")
student_mark = input("Enter the student's grade: ")


def evaluation(mark):
    assessment = "approved"
    if mark < 5:
        assessment = "failure"
    return assessment


print(evaluation(int(student_mark)))
