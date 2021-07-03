
print("Student marks evaluation program")
student_mark = input("Enter the student's grade: ")


def evaluation(mark):
    assessment = "approved"
    if mark < 5:
        assessment = "failure"
    return assessment


print(evaluation(int(student_mark)))


print("Marks verification")
student_mark = int(input("Enter your mark, please: "))

if student_mark < 5:
    print("Failure")
elif student_mark < 6:
    print("Approved")
elif student_mark < 7:
    print("Good")
elif student_mark < 9:
    print("Remarkable")
else:
    print("Outstanding")
print("The program has ended")
