import student as s
import course as c

students_list = [] # List to hold all students
course_list = [] # List to hold all courses

# START OF STUDENT OPERATIONS
def load_students(students_list):
    # Load students from CSV file
    infile_students = open('students.csv', 'r')
    
    students = infile_students.readlines()
    
    for line in students:
        # Process each line and create Student objects
        student = line.replace(';', ' ').replace('\n', '').split(' ')
        students_list.append(s.Student(student[0], student[1], student[2], student[3], student[4]))
        
    infile_students.close()

def find_student(students_list, lastname):
    # Find student by last name
    student = None
    for learner in students_list:
        if lastname == learner.lastName:
            student = learner
        else:
            continue
    return student

def find_student_id(students_list, id):
    # Find student by ID
    student = None
    for learner in students_list:
        if id == learner.id:
            student = learner
        else:
            continue
    return student

def find_student_phone(students_list, phone):
    # Find student by phone number
    student = None
    for learner in students_list:
        if phone == learner.get_phone():
            student = learner
        else:
            continue
    return student

def list_all_students(students_list):
    # Display all students in unsorted order
    print('\n\tSTUDENTS - UNSORTED')
    print('--------------------------------------------------------------------')
    for student in students_list:
        student.display_student()
        
def list_all_students_alpha_az(students_list):
    # Display all students sorted alphabetically A-Z
    sorted_students = sorted(students_list, key=lambda student: student.lastName)
    print('\n\tSTUDENTS - SORTED FROM A-Z')
    print('--------------------------------------------------------------------')
    for student in sorted_students:
        student.display_student()
        
def list_all_students_alpha_za(students_list):
    # Display all students sorted alphabetically Z-A
    sorted_students = sorted(students_list, key=lambda student: student.lastName, reverse=True)
    print('\n\tSTUDENTS - SORTED FROM Z-A')
    print('--------------------------------------------------------------------')
    for student in sorted_students:
        student.display_student()

def add_student(students_list, course_list):
    # Add a new student to the list
    lastName = input('Enter Student\'s Lastname: ')
    firstName = input('Enter Student\'s Firstname: ')
    phone = input('Enter Student\'s Phone Number: ')
    email = input('Enter Student\'s Email Address: ')
    student = s.Student(str(len(students_list) + 1), lastName, firstName, phone, email)
    students_list.append(student)
    print('Student Added!')

def add_course(course_list):
    # Add a new course to the list
    course = input('Enter Course: ')
    sememster = input('Enter Semester: ')
    new_course = c.Course(course, str(len(course_list) + 1), sememster)
    course_list.append(new_course)
    print('Course Added Successfully!')

def update_student(students_list):
    # Update student information
    student_id = input('Enter Student ID: ')
    option = ''

    student = find_student_id(students_list, student_id)

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
            data = input('Enter new email: ')
            student.set_email(data)
    else:
        print('Student does not exist!')

def student_search_lastname(students_list):
    # Search for a student by last name
    student = find_student(students_list, lastname=input('Enter student lastname: '))
    if student != None:
        student.display_student()
    else:
        print('Student Not Found')

def student_search_phone(students_list):
    # Search for a student by phone number
    student = find_student_phone(students_list, phone=input('Enter student phone: '))
    if student != None:
        student.display_student()
    else:
        print('Student Not Found')

def student_course_lastname(students_list):
    # List all courses taken by a student (search by last name)
    lastname = input('Enter student lastname: ')
    student = find_student(students_list, lastname)

    if student != None:
        print('\n\tCOURSES(S)')
        print('--------------------------------------------------------------------')
        student.display_courses()
    else:
        print('Student does not exist!')

def student_average_grade(students_list):
    # Calculate the average grade of a student
    average = 0
    student_lastname = input('Enter student lastname: ')

    student = find_student(students_list, student_lastname)

    if student != None:
        print('\n\tAVERAGE')
        print('--------------------------------------------------------------------')
        print(student.average_grade())
    else:
        print('Student does not exist!')
    
# END OF STUDENT OPERATIONS

# START OF COURSE OPERATIONS
def load_courses(course_list):
    # Load courses from CSV file
    infile = open('courses.csv', 'r')
    courses = infile.readlines()
    
    for line in courses:
        # Process each line and create Course objects
        course = line.replace(';', ' ').replace('\n', '').split(' ')
        course_list.append(c.Course(course[0], course[2], course[1]))
        
    infile.close()

def list_all_courses(course_list):
    # Display all courses
    print('\n\tCOURSES')
    print('--------------------------------------------------------------------')
    for course in course_list:
        course.display_course()

def list_all_courses_semester(course_list, semester):
    # Display all courses by semester
    print('\n\tCOURSES DURING ' + semester.upper())
    print('--------------------------------------------------------------------')
    for course in course_list:
        if course.get_semester() == semester.lower():
            course.display_course()
    return course

def list_all_courses_semester_az(course_list, semester):
    # Display all courses by semester sorted A-Z
    sorted_courses = sorted(course_list, key=lambda course: course.name)
    print('\n\tCOURSES DURING ' + semester.upper() + ' A-Z')
    print('--------------------------------------------------------------------')
    for course in sorted_courses:
        if course.get_semester() == semester.lower():
            course.display_course()

def list_all_courses_semester_za(course_list, semester):
    # Display all courses by semester sorted Z-A
    sorted_courses = sorted(course_list, key=lambda course: course.name, reverse=True)
    print('\n\tCOURSES DURING ' + semester.upper() + ' Z-A')
    print('--------------------------------------------------------------------')
    for course in sorted_courses:
        if course.get_semester() == semester.lower():
            course.display_course()

def search_course_name(course_list, course_name):
    # Search for a course by name
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
    # Search for a course by code
    course = None
    for cse in course_list:
        if course_code == cse.get_code():
            course = cse
        else:
            continue
    
    if course == None:
        print('Course does not exist!')
        
    return course

def add_course(course_list):
    # Add a new course to the list
    course_name = input('Enter course: ')
    semester = input('Enter semester: ')

    new_course = c.Course(course_name, len(course_list) + 1, semester)

    course_list.append(new_course)
    print('Course Added Successfully!')

def course_average_semester(students_list, lastname, semester):
    # Display the average grade for a student in a specific semester
    student = find_student(students_list, lastname)
    if student != None:
        average = student.average_grade_semester(semester)
        print('\n\tAVERAGE - SEMESTER')
        print('--------------------------------------------------------------------')
        print(average)

def load_grades(students_list, course_list):
    # Load grades from CSV file and assign them to students
    infile_grades = open('grades.csv', 'r')
    grades = infile_grades.readlines()
    
    for line in grades:
        grade = line.replace(';', ' ').replace('\n', '').split(' ')
        student = find_student(students_list, grade[1])
        crse_code = 1
        for grd in grade[3:]:
            if grd != 'na':
                crse = search_course_code(course_list, str(crse_code))
                student.add_course(crse)                
                student.get_course(crse.get_name()).set_grade(grd)
            crse_code += 1

    infile_grades.close()

# END OF COURSE OPERATIONS

def main():
    # Main function to drive the program
    load_students(students_list)  # Load students from CSV file and store in list
    load_courses(course_list)  # Load courses from CSV file and store in list
    load_grades(students_list, course_list)  # Load grades for students and courses
    
    while True:
        # Display the menu and prompt for user input
        print('-'*50)
        print("\t\t\tMENU:")
        print('-'*50)
        print("1: Add a student")
        print("2: Add a course")
        print("3: List all students")
        print("4: List all students alphabetically (A-Z)")
        print("5: List all courses")
        print("6: List all courses by semester")
        print("7: Search course by code")
        print("8: Search student by last name")
        print("9: Search student by phone")
        print("10: Search course by name")
        print("11: Update a student")
        print("12: List courses by student last name")
        print("13: Display student's average grade")
        print("14: List courses by semester (A-Z)")
        print("15: Display course average for a student")
        print("16: Exit and save")
        print('-'*50)
        option = input("Enter your choice: ")

        # Handle user input based on option chosen
        if option == '1':
            add_student(students_list, course_list)
        elif option == '2':
            add_course(course_list)
        elif option == '3':
            list_all_students(students_list)
        elif option == '4':
            list_all_students_alpha_az(students_list)
        elif option == '5':
            list_all_courses(course_list)
        elif option == '6':
            list_all_courses_semester(course_list, semester=input('Enter Semester: '))
        elif option == '7':
            search_course_code(course_list, course_code=input('Enter Course Code: ')).display_course()
        elif option == '8':
            student_search_lastname(students_list)
        elif option == '9':
            student_search_phone(students_list)
        elif option == '10':
            search_course_name(course_list, course_name=input('Enter Course Name: '))
        elif option == '11':
            update_student(students_list)
        elif option == '12':
            student_course_lastname(students_list)
        elif option == '13':
            student_average_grade(students_list)
        elif option == '14':
            list_all_courses_semester_az(course_list, semester=input('Enter Semester: '))
        elif option == '15':
            course_average_semester(students_list, lastname=input('Enter Lastname: '))
        elif option == '16':
            # Save to CSV and exit
            with open('students.csv', 'w') as infile:
                infile.writelines(
                    f"{student.get_id()};{student.get_lastname()};{student.get_firstname()};"
                    f"{student.get_phone()};{student.get_email()}\n"
                    for student in students_list
                )
                
            with open('courses.csv', 'w') as infile:
                infile.writelines(
                    f"{course.get_name()};{course.get_semester()};{course.get_code()};\n"
                    for course in course_list
                )
            
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid option. Please try again.")


main()
