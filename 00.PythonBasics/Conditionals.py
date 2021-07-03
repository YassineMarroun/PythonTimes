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


age = -7

if 0 < age < 100:
    print("Age is correct")
else:
    print("Age is incorrect")


president_salary = int(input("Enter the president's salary: "))
print("President salary: " + str(president_salary))

director_salary = int(input("Enter the director's salary: "))
print("Director salary: " + str(director_salary))

area_manager_salary = int(input("Enter the salary of the area manager: "))
print("Area manager salary: " + str(area_manager_salary))

administrative_salary = int(input("Enter the salary of the administrative: "))
print("Administrative salary: " + str(administrative_salary))

if administrative_salary < area_manager_salary < director_salary < president_salary:
    print("Everything works correctly")
else:
    print("Something is wrong with the accounts of the company")


print("Scholarship Program 2020")
school_distance = int(input("Enter the distance to the school in km: "))
print(school_distance)

numberOf_brothers = int(input("Enter the number of siblings in the center: "))
print(numberOf_brothers)

family_salary = int(input("Enter the gross annual salary: "))
print(family_salary)

if school_distance > 40 and numberOf_brothers > 2 or family_salary <= 20000:
    print("You are entitled to a scholarship")
else:
    print("You do not have the right to a scholarship")


print("Optative subjects for 2020")
print("Optative subjects: Computer Graphics - Software Testing- Usability and Accessibility")
option = input("Enter the chosen subject: ")
subject = option.lower()

if subject in ("computer graphics", "software testing", "usability and accessibility"):
    print("Chosen subject " + subject)
else:
    print("The subject chosen not provided")
