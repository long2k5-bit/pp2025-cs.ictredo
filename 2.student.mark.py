# FILE: 2.student.mark.py

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_mark(self, course_id, mark):
        self.marks[course_id] = mark

    def get_mark(self, course_id):
        return self.marks.get(course_id, None)

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

class StudentMarkManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = {}

    def input_number_of_students(self):
        return int(input("Enter number of students: "))

    def input_student_information(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = Student(student_id, name, dob)
        self.students.append(student)

    def input_number_of_courses(self):
        return int(input("Enter number of courses: "))

    def input_course_information(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        course = Course(course_id, name)
        self.courses[course_id] = course

    def select_course_and_input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        if course_id in self.courses:
            for student in self.students:
                mark = float(input(f"Enter mark for student {student.name} (ID: {student.student_id}): "))
                student.input_mark(course_id, mark)
        else:
            print("Course not found!")

    def list_courses(self):
        for course in self.courses.values():
            print(f"Course ID: {course.course_id}, Name: {course.name}")

    def list_students(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks_for_course(self):
        course_id = input("Enter course ID to show marks: ")
        for student in self.students:
            mark = student.get_mark(course_id)
            if mark is not None:
                print(f"Student ID: {student.student_id}, Name: {student.name}, Mark: {mark}")

    def run(self):
        num_students = self.input_number_of_students()
        for _ in range(num_students):
            self.input_student_information()

        num_courses = self.input_number_of_courses()
        for _ in range(num_courses):
            self.input_course_information()

        self.select_course_and_input_marks()
        self.list_courses()
        self.list_students()
        self.show_student_marks_for_course()

if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    system.run()