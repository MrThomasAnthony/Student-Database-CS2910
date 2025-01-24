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

    student = find_student_id(students_list,student_id)

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
    student = find_student(students_list,lastname = input('Enter student lastname: '))
    if student != None:
        student.display_student()
    else:
        print('Student Not Found')

def student_search_phone(students_list):
    student = find_student_phone(students_list,phone = input('Enter student phone: '))
    if student != None:
        student.display_student()
    else:
        print('Student Not Found')
    
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
    return course

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
    course_name = input('Enter course: ')
    semester = input('Enter semester: ')

    new_course = c.Course(course_name,len(course_list)+1,semester)

    course_list.append(new_course)

def course_average_semester(students_list,lastname,semester):
    student = find_student(students_list,lastname)
    if student != None:
        average = student.average_grade_semester(semester)
        print('\n\tAVERAGE - SEMESTER')
        print('--------------------------------------------------------------------')
        print(average)


#END OF COURSE OPERATIONS
       
def load_grades(course_list):
    infile = open('grades.csv','r')
    grades = infile.readlines()
    
    for record in grades:
        grade = line.replace(';',' ').replace('\n', '').split(' ')
        students_list.append(s.Student(grade[0],grade[1],grade[2],grade[3],grade[4]))
        
    infile.close()

def menu():
    print("-" * 50)
    print("STUDENTS DATABASE MANAGEMENT SYSTEM.")
    print("-" * 50)
    print("Menu...Enter an option!")
    print("-" * 50)
    print("1. Add New Student")
    print("2. Display Students")
    print("3. Display Sorted List")
    print("4. Display Courses")
    print("5. Display Semester")
    print("6. Course Code Search")
    print("7. Last Name Search")
    print("8. Phone Number Search")
    print("9. Display Courses by Code")
    print("10. Add Grade")
    print("11. Update student Info")
    print("12. Display Courses taken by Student")
    print("13. Calculate Student Average grade")
    print("14. Calculate the course Average")
    print("15. Display Sorted Course")
    print("16. Calculate Average by Semester ")
    print("17. Add Course")
    print("0. Exit")
    print("-" * 50)

def main():
    
    load_students(students_list) #load students from csv file and store in list
    load_courses(course_list) #load students from csv file and store in list
    
    while True:
        menu()

        option = input('Select operation: ')

        if option == '1':
            add_student(students_list,course_list)
        elif option == '2':
            list_all_students(students_list)
        elif option == '3':
            list_all_students_alpha_az(students_list)
        elif option == '4':
            list_all_courses(course_list)
        elif option == '5':
            list_all_courses_semester(course_list,semester=input('Enter Semester:'))
        elif option == '6':
            search_course_code(course_list,course_code=input('Enter Course Code:'))
        elif option == '7':
            student_search_lastname(students_list)
        elif option == '8':
            student_search_phone(students_list)
        elif option == '9':
            search_course_name(course_list,course_name=input('Enter Course Name: '))
        elif option == '10':
            continue
        elif option == '11':
            update_student(students_list)
        elif option == '12':
            student_course_lastname(students_list)
        elif option == '13':
            student_average_grade(students_list)
        elif option == '14':
            continue
        elif option == '15':
            list_all_courses_semester_az(course_list,semester=input('Enter Semester: '))
        elif option == '16':
            course_average_semester(students_list,lastname=input('Enter Lastname: '))
        elif option == '17':
            add_course(students_list)
        else:
            infile = open('students.csv','a')
            for student in students_list:
                infile.write(f"{student.get_id()};{student.get_lastname()};{student.get_firstname()};{student.get_phone()};{student.get_email()}\n")
            infile.close()
            break


main()