import course as c

class Student:
    def __init__(self, id, lastName, firstName, phone, email):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
        self.phone = phone
        self.email = email
        self.courses = []

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

    def add_course(self, course):
        self.courses.append(course)

    def average_grade(self):
        grade_sum = sum(each_course.get_grade() for each_course in self.courses)
        return grade_sum / len(self.courses) if self.courses else 0
    
    def average_grade_semester(self, semester):
        semester_courses = [each_course for each_course in self.courses if each_course.get_semester() == semester]
        grade_sum = sum(course.get_grade() for course in semester_courses)
        return grade_sum / len(semester_courses) if semester_courses else 0
    
    def get_course(self, course_name):
        for crse in self.courses:
            if crse.get_name() == course_name:
                return crse
        return None
