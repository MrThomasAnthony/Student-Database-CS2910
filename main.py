import student as s
import course as c

#START OF STUDENT OPERATIONS
def load_students(students_list):
    infile = open('students.csv','r')
    students = infile.readlines()
    
    for line in students:
        student = line.replace(';',' ').replace('\n', '').split(' ')
        students_list.append(s.Student(student[0],student[1],student[2],student[3],student[4]))
        
    infile.close()
    
def list_all_students(students_list):
    print('\n\tSTUDENTS - UNSORTED')
    print('--------------------------------------------------------------------')
    for student in students_list:
        student.display_student()
        
def list_all_students_alpha_az(students_list):
    sorted_students = sorted(students_list, key=lambda student: student.lastName)
    print('\n\tSTUDENTS - SORTED FROM A-Z')
    print('--------------------------------------------------------------------')
    for student in sorted_students:
        student.display_student()
        
def list_all_students_alpha_za(students_list):
    sorted_students = sorted(students_list, key=lambda student: student.lastName, reverse=True)
    print('\n\tSTUDENTS - SORTED FROM Z-A')
    print('--------------------------------------------------------------------')
    for student in sorted_students:
        student.display_student()

def add_student(students_list,course_list):
    id = 1
    course_id = 1
    lastName = input('Enter Student\'s Lastname: ')
    course = input('Enter Student\'s Course: ')
    sememster = input('Enter Semester: ')
    grade = input('Enter Student\'s Grade: ')
    
    for student in students_list:
        id+=1
        
    for course in course_list:
        course_id+=1
    
    student = s.Student(id,lastName,'na','na','na')
    students_list.append(student)
    print('Student Added! You can update student information late!')
    new_course = c.Course(course,course_id,sememster)
    new_course.grade = grade
    course_list.append(new_course)
    student.add_course(course)

def update_student(students_list):
    student_id = input('Enter Student ID: ')
    option = ''
    for student in students_list:
        if student.get_id() == student_id:
            print('1. Update student lastname')
            print('2. Update student firstname')
            print('3. Update student phone number')
            print('4. Update student email')
            option = input('Enter from above list!')

            if option == '1':
                data = input('Enter new lastname: ')
                student.set_lastname(data)
            elif option == '2':
                data = input('Enter new firstname: ')
                student.set_fistname(data)
            elif option == '3':
                data = input('Enter new phone number: ')
                student.set_phone(data)
            else:
                data = input('Enter new emai: ')
                student.set_email(data)
        else:
            print('Student does not exist!')
        
def student_search_lastname(students_list):
    lastname = input('Enter student lastname: ')
    for student in students_list:
        if lastname == student.get_lastname():
            student.display_student()
        else:
            print('Student not found!')

def student_search_phone(students_list):
    phone = input('Enter student phone number: ')
    for student in students_list:
        if phone == student.get_phone():
            student.display_student()
        else:
            print('Student not found!')
    
def student_course_lastname(students_list):
    lastname = input('Enter student lastname: ')
    for student in students_list:
        if lastname == student.get_lastname():
            student.display_courses()
        else:
            print('Student not found!')
#END OF STUDENT OPERATIONS

#START OF COURSE OPERATIONS
def load_courses(course_list):
    infile = open('courses.csv','r')
    courses = infile.readlines()
    
    for line in courses:
        course = line.replace(';',' ').replace('\n', '').split(' ')
        course_list.append(c.Course(course[0],course[2],course[1]))
        
    infile.close()
    
def list_all_courses(course_list):
    print('\n\tCOURSES')
    print('--------------------------------------------------------------------')
    for course in course_list:
        course.display_course()
        
def list_all_courses_semester(course_list, semester):
    print('\n\tCOURSES DURING ' + semester.upper())
    print('--------------------------------------------------------------------')
    for course in course_list:
        if course.get_semester() == semester.lower():
            course.display_course()

def list_all_courses_semester_az(course_list, semester):
    sorted_courses = sorted(course_list, key=lambda course: course.name)
    print('\n\tCOURSES DURING ' + semester.upper() + ' A-Z')
    print('--------------------------------------------------------------------')
    for course in sorted_courses:
        if course.get_semester() == semester.lower():
            course.display_course()
     
def list_all_courses_semester_za(course_list, semester):
    sorted_courses = sorted(course_list, key=lambda course: course.name, reverse=True)
    print('\n\tCOURSES DURING ' + semester.upper() + ' Z-A')
    print('--------------------------------------------------------------------')
    for course in sorted_courses:
        if course.get_semester() == semester.lower():
            course.display_course()
#END OF COURSE OPERATIONS
       
def main():
    students_list = [] #list to hold all students
    course_list = [] #list to hold all course
    load_students(students_list) #load students from csv file and store in list
    load_courses(course_list) #load students from csv file and store in list
    list_all_students(students_list) #display all students
    list_all_courses(course_list) #display all courses
    list_all_courses_semester(course_list,'fall') #display all courses filtered by sememster
    list_all_courses_semester_az(course_list,'fall') #display all courses from a-z
    list_all_courses_semester_za(course_list,'fall') #display all courses from z-a
    list_all_students_alpha_za(students_list) #display all students from z-a
    add_student(students_list,course_list)
    list_all_students(students_list) #display all students
    student_course_lastname(students_list)
main()