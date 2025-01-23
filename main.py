import student as s
import course as c

students_list = [] #list to hold all students
course_list = [] #list to hold all course

#START OF STUDENT OPERATIONS
def load_students(students_list):
    infile = open('students.csv','r')
    students = infile.readlines()
    
    for line in students:
        student = line.replace(';',' ').replace('\n', '').split(' ')
        students_list.append(s.Student(student[0],student[1],student[2],student[3],student[4]))
        
    infile.close()
    
def find_student(student_list,lastname):
    student = None
    for learner in student_list:
        if lastname == learner.lastName:
            student = learner
        else:
            continue
    return student

def find_student_id(student_list,id):
    student = None
    for learner in student_list:
        if id == learner.id:
            student = learner
        else:
            continue
    return student

def find_student_phone(student_list,phone):
    student = None
    for learner in student_list:
        if phone == learner.get_phone():
            student = learner
        else:
            continue
    return student

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
    lastName = input('Enter Student\'s Lastname: ')
    course = input('Enter Student\'s Course: ')
    sememster = input('Enter Semester: ')
    grade = input('Enter Student\'s Grade: ')
    
    student = s.Student(len(students_list)+1,lastName,'na','na','na')
    students_list.append(student)
    print('Student Added! You can update student information late!')

    new_course = c.Course(course,len(course_list)+1,sememster)
    new_course.grade = grade

    course_list.append(new_course)
    student.add_course(new_course)

def update_student(students_list):
    student_id = input('Enter Student ID: ')
    option = ''

    student = find_student_id(students_list,int(student_id))

    if student != None:
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
            student.set_firstname(data)
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
    student = find_student(students_list,lastname)

    if student != None:
        print('\n\tCOURSES(S)')
        print('--------------------------------------------------------------------')
        student.display_courses()
    else:
        print('Student does not exist!')

def student_average_grade(students_list):
    average = 0
    student_lastname = input('Enter student lastname: ')

    student = find_student(students_list,student_lastname)

    if student != None:
        print('\n\tAVERAGE')
        print('--------------------------------------------------------------------')
        print(student.average_grade())
    else:
        print('Student does not exist!')
    
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

def search_course_name(course_list, course_name):
    course = None
    for cse in course_list:
        if course_name == cse.get_name():
            course = cse
        else:
            continue
    
    if course == None:
        print('Course does not exist!')
    else:
        course.display_course()

def search_course_code(course_list, course_code):
    course = None
    for cse in course_list:
        if course_code == cse.get_code():
            course = cse
        else:
            continue
    
    if course == None:
        print('Course does not exist!')
    else:
        course.display_course()

def add_course(students_list):
    student_lastname = input('Enter student lastname: ')
    course_name = input('Enter course: ')
    semester = input('Enter semester: ')

    student = find_student(students_list,student_lastname)
    new_course = c.Course(course_name,len(course_list)+1,semester)
    new_course.set_grade(grade=input('Enter grade: '))

    if student != None:
        student.add_course(new_course)
        print('Course added!')
    else:
        print('Student does not exist!')
            
#END OF COURSE OPERATIONS
       
def load_grades(course_list):
    infile = open('grades.csv','r')
    grades = infile.readlines()
    
    for record in grades:
        grade = line.replace(';',' ').replace('\n', '').split(' ')
        students_list.append(s.Student(grade[0],grade[1],grade[2],grade[3],grade[4]))
        
    infile.close()

def main():
    
    load_students(students_list) #load students from csv file and store in list
    load_courses(course_list) #load students from csv file and store in list
    add_course(students_list)
    add_course(students_list)
    add_course(students_list)
    student_course_lastname(students_list)
    student_average_grade(students_list)

main()