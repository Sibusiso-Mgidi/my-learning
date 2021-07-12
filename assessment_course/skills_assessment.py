

class Student(object):
    """
    This is a blueprint for storing student data
    """
    def __init__(self, student_no, first_name, last_name, course):
        self.student_no = int(student_no)
        self.first_name = first_name
        self.last_name = last_name
        self.course = course

    def __re__(self):
        return " %s %s studies %s" % (self.first_name, self.last_name, self.course)

class Question(object):
    """
    This is a blueprint for storing questions and answers.
    """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __repr__(self):
        """
        This method returns the question and answer
        """
        return "Question: {} \n Answer: {}".format(self.question, self.answer)

    def ask_an_evaluate(self):
        """
        Prints the question, and then checks if it is correct
        """
        print(self.question)
        user_answer = input("> ")
        if user_answer == self.answer:
            return True
        else:
            return False

class Exam(object):
    """
    This is a blueprint for storing students exam scores 
    """
