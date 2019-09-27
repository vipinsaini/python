from classes import Student

student1 = Student("Vipin", "B.tech", 3.0, False)
student2 = Student("Savi", "MBA", 5.0, True)
print(student1.name + " is honor:" + str(student1.on_honor_roll()))
print(student2.name + " is honor:" + str(student2.on_honor_roll()))


