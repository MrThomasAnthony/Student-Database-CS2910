class Course:
    grade = 0
    def __init__(self,name,code,semester):
        self.name = name
        self.code = code
        self.semester = semester

    def get_code(self):
        return self.code

    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name

    def set_semester(self, semester):
        self.semester = semester
        
    def get_semester(self):
        return self.semester
    
    def set_grade(self, grade):
        self.grade = grade
    
    def get_grade(self):
        return int(self.grade)
        
    def display_course(self):
        print(f"Name: {self.get_name()} Code: {self.get_code()} Semester: {self.get_semester()}")
