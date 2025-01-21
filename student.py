import course as c
class Student:
    course = []
    def __init__(self,id,lastName,firstName,phone,email):
        self.id = id
        self.lastName = lastName
        self.firstName = firstName
        self.phone = phone
        self.email = email
    
    def display_student(self):
        print(f"ID: {self.id} Lastname: {self.lastName} Firstname: {self.firstName} Phone: {self.phone} Email: {self.email}")
