import course as c
class Student:
    courses = []
    def __init__(self,id,lastName,firstName,phone,email):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
        self.phone = phone
        self.email = email

    def get_id(self):
        return self.id
    
    def get_lastname(self):
        return self.lastName
    
    def set_lastname(self, lastName):
        self.lastName = lastName

    def get_firstname(self):
        return self.firstName
    
    def set_firstname(self, firstName):
        self.firstName = firstName
    
    def get_phone(self):
        return self.phone
    
    def set_phone(self, phone):
        self.phone = phone

    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def display_student(self):
        print(f"ID: {self.get_id()} \tLastname: {self.get_lastname()} \tFirstname: {self.get_firstname()} \tPhone: {self.get_phone()} \tEmail: {self.get_email()}\n")

    def display_courses(self):
        for each_course in self.courses:
            print(f"Name: {each_course.get_name()} \tCode: {each_course.get_code()} \tSemester: {each_course.get_semester()} \tGrade: {each_course.get_grade()}")


    def add_course(self,course):
        self.courses.append(course)

    def average_grade(self):
        grade_sum = 0
        for each_course in self.courses:
            grade_sum += each_course.get_grade()
        return grade_sum/len(self.courses)
    
    def average_grade_semester(self, semester):
        grade_sum = 0
        for each_course in self.courses:
            if each_course.get_semester() == semester:
                grade_sum += each_course.get_grade()
        return grade_sum/len(self.courses)