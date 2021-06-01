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

class  Student():
    """
    This is a blueprint fr getting the students demographic dataset.
    """
    def __init__(self, first_name, last_name, student_number, course_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.course_name = course_name
        self.address = address

    def __str__(self):
        """
        returns demographic data
        """
        return "First name: {} \nLast name: {} \nStudent number: {} \nCourse: {} \nAddress: {}".format(self.first_name, self.last_name, self.student_number, self.course_name, self.address)
    
class Question():
    """
    This is a blueprint for storing quetsions and solutions.
    """
    def __init__(self, question, solution):
        self.question = question
        self.solution = solution

    def __str__(self):
        """
        This method returns the question and solution.
        """
        return "Question: {} \n Solution: {}".format(self.question, self.solution)

    def ask_and_evaluate(self):
        """
        This method prints thee questio and prompts the user to answer.
        :returns: boolean values (True or False)
        """

        print(self.question)
        user_solution = input("Enter the solution: \n")
        if user_solution == self.solution:
            return True
        else:
            return False
        
class Exam():
    """
    This is a blueprint for students exam questions
    """
    def __init__(self, exam_name, store_questions):
        self.exam_name = exam_name
        self.store_questions = []

    def __str__(self):
        """
        This method returns exam name and questions
        """
        return "This is the {} Exam\n  The questions for this Exam are {}: \n".format(self.exam_name, self.question)

    def add_question(self, questions, correct_solutions):
        """
        This is a method which adds questions and correct answers for a specific exam.
        """
        self.store_questions.append(Question(questions,correct_solutions))

    def conduct_exams(self):
        """
        This function asks questions and returns the score of how many were correct.
        """
        
        correct_sols = 0
        for question in self.store_questions:
            
            if question.ask_and_evaluate():
                correct_sols += 1
        
        score = (correct_sols/len(self.store_questions)) * 100
        return score
            




        


    
# test the class
question = Question("1. Was Sibusiso Mgidi born on the 2nd of January 1996: \n",True)

question.ask_and_evaluate()

print(question)
