
# Here we import a student class from file student

from student import student

student1 = student("Jim", "Business", 3.5, False)  # We create an object student which gives values to the class student
student2 = student("Jane", "IT", 2, True)


print(student1.name)


print("Student 1 is " + str(student1.is_honored()))
