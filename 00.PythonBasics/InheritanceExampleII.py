class Person:
    def __init__(self, name, age, residence_place):
        self.name = name
        self.age = age
        self.residence_place = residence_place

    def description(self):
        print("Name:", self.name, "Age:", self.age, "Place of residence:", self.residence_place)


class Employee(Person):
    def __init__(self, salary, seniority, name_employee, age_employee, residence_employee):
        super().__init__(name_employee, age_employee, residence_employee)
        self.salary = salary
        self.seniority = seniority

    def description(self):
        super().description()
        print("Salary:", self.salary, "Seniority:", self.seniority)


Peter = Employee(1500, 15, "Peter", 45, "Spain")
Peter.description()
print(isinstance(Peter, Person))
