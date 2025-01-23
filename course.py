class Course:
    grade = 0
    def __init__(self,name,code,semester):
        self.name = name
        self.code = code
        self.semester = semester
        
    def get_semester(self):
        return self.semester
        
    def display_course(self):
        print(f"Name: {self.name} Code: {self.code} Semester: {self.semester} Grade: {self.grade}")
