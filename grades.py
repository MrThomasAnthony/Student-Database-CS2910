class Grades:
    grades = []
    def __init__(self,code,lastname,firstname,grade):
        self.code = code
        self.lastname = lastname
        self.firstname = firstname
        self.grades.append(grade)
        
    def add_grade(self,grade):
        self.grades.append(grade)