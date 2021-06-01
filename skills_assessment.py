"""
Object Orientated programming(OOP)

3 main concepts of Object Orintated Programming(OOP)
- Encapsulation
- Abstraction
- Polymorphism

Encapsulation:
- wraps up data under a single units
- It binds together code and the data it manipulates

Abstraction:
- displaying only essential information about the data to the outside world, hiding the background details or implementation.

Polymorphism:
- The ability to make many forms, different forms and interchangeable types.

1. Class
- It is a way of organizing and producing objects with similar attributes and methods.

2. Instance Attribute:
- It is an instance set directly on the object, as opposed to claaa attributes.

3. Method
- Are functions of objects
"""

"""YOU ARE TASKED TO CREATE A SCRIPT FOR STUDENTS ASSESSMENT

"""
class  Student():
    def __init__(self, first_name, last_name, student_number, course_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.course_name = course_name
        self.address = address

    def __str__(self):
        return "First name: {} \nLast name: {} \nStudent number: {} \nCourse: {} \nAddress: {}".format(self.first_name, self.last_name, self.student_number, self.course_name, self.address)
    


student_details = Student("Sibusiso", "Mgidi", "1141573", "BSC. Honours in Computer Science", "Braamfontein")
print(student_details)