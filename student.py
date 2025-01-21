import course as c
class Student:
    course = []
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
        self.lastName = firstName
    
    def get_phone(self):
        return self.phone
    
    def set_phone(self, phone):
        self.phone = phone

    
    def get_email(self):
        return self.email
    
    def set_email(self, email):
        self.email = email

    def display_student(self):
        print(f"ID: {self.get_id()} Lastname: {self.get_lastname()} Firstname: {self.get_firstname()} Phone: {self.get_phone()} Email: {self.get_email()}")

    def display_courses(self):
        for course in self.course:
            course.display_course()

    def add_course(self,course):
        self.course.append(course)