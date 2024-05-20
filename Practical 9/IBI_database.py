#This code functions to help the faculty to keep a record of the students in IBI1
#define a class named IBI
#initialise the attributes needed
#check if the score is a valid score
class IBI:
    def __init__(self, name, major, code_portfolio_score, group_project_score, exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score = exam_score
    
    def correct_score(self, code_portfolio_score):
        if not 0 <= int(self.code_portfolio_score) <= 100:
            raise ValueError("Invalid score input. Please enter a score between 0 to 100.")
        return code_portfolio_score()
    
    def correct_score(self, group_project_score):
        if not 0 <= int(self.group_project_score) <= 100:
            raise ValueError("Invalid score input. Please enter a score between 0 to 100.")
        return group_project_score()
    
    def correct_score(self, exam_score):
        if not 0 <= int(self.exam_score) <= 100:
            raise ValueError("Invalid score input. Please enter a score between 0 to 100.")
        return exam_score()
    
    def IBI1_students_record(self):
        print(f"Student's name: {self.name}")
        print(f"student's major: {self.major}")
        print(f"Student's code portfolio score: {self.code_portfolio_score}")
        print(f"Student's group project score: {self.group_project_score}")
        print(f"Student's exam score: {self.exam_score}")
        
student = IBI("Chong Junliang", "BMI", "102", "101", "101")
student.IBI1_students_record()
student.correct_score("code_portfolio_score")
student.correct_score("group_project_score")
student.correct_score("exam_score")