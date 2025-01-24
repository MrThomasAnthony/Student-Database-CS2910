class Grade:
    
    def __init__(self,code,lastname,firstname,course_grade):
        self.code = code
        self.lastname = lastname
        self.firstname = firstname
        self.grades.append(course_grade)
        self.grades = []
        
    def add_grade(self,grade):
        self.grades.append(grade)