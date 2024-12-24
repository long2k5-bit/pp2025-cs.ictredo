# FILE: 1.student.mark.py

def input_number_of_students():
    return int(input("Enter number of students: "))

def input_student_information():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    return (student_id, name, dob)

def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_information():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    return (course_id, name)
def select_course_and_input_marks(students, courses):
    course_id = input("Enter course ID to input marks: ")
    if course_id in courses:
        for student in students:
            mark = float(input(f"Enter mark for student {student[1]} (ID: {student[0]}): "))
            student_marks[student[0]][course_id] = mark
    else:
        print("Course not found!")

def list_courses(courses):
    for course_id, name in courses.items():
        print(f"Course ID: {course_id}, Name: {name}")

def list_students(students):
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks_for_course(students, course_id):
    for student in students:
        if course_id in student_marks[student[0]]:
            print(f"Student ID: {student[0]}, Name: {student[1]}, Mark: {student_marks[student[0]][course_id]}")

def main():
    students = []
    courses = {}
    global student_marks
    student_marks = {}

    num_students = input_number_of_students()
    for _ in range(num_students):
        student = input_student_information()
        students.append(student)
        student_marks[student[0]] = {}

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_id, name = input_course_information()
        courses[course_id] = name

    select_course_and_input_marks(students, courses)
    list_courses(courses)
    list_students(students)
    course_id = input("Enter course ID to show marks: ")
    show_student_marks_for_course(students, course_id)

if __name__ == "__main__":
    main()

