# FILE: 3.student.mark.oop.math.py

import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.credits = {}

    def input_mark(self, course_id, mark, credit):
        self.marks[course_id] = math.floor(mark * 10) / 10  # Round down to 1-digit decimal
        self.credits[course_id] = credit

    def get_mark(self, course_id):
        return self.marks.get(course_id, None)

    def calculate_gpa(self):
        if not self.marks:
            return 0.0
        total_credits = sum(self.credits.values())
        weighted_sum = sum(self.marks[course_id] * self.credits[course_id] for course_id in self.marks)
        return weighted_sum / total_credits if total_credits != 0 else 0.0

class Course:
    def __init__(self, course_id, name, credit):
        self.course_id = course_id
        self.name = name
        self.credit = credit

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
        credit = float(input("Enter course credit: "))
        course = Course(course_id, name, credit)
        self.courses[course_id] = course

    def select_course_and_input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        if course_id in self.courses:
            for student in self.students:
                mark = float(input(f"Enter mark for student {student.name} (ID: {student.student_id}): "))
                student.input_mark(course_id, mark, self.courses[course_id].credit)
        else:
            print("Course not found!")

    def list_courses(self):
        for course in self.courses.values():
            print(f"Course ID: {course.course_id}, Name: {course.name}, Credit: {course.credit}")

    def list_students(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, DoB: {student.dob}")

    def show_student_marks_for_course(self):
        course_id = input("Enter course ID to show marks: ")
        for student in self.students:
            mark = student.get_mark(course_id)
            if mark is not None:
                print(f"Student ID: {student.student_id}, Name: {student.name}, Mark: {mark}")

    def calculate_average_gpa(self):
        for student in self.students:
            gpa = student.calculate_gpa()
            print(f"Student ID: {student.student_id}, Name: {student.name}, GPA: {gpa:.2f}")

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.calculate_gpa(), reverse=True)

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
        self.calculate_average_gpa()
        self.sort_students_by_gpa()
        print("Students sorted by GPA:")
        self.list_students()

if __name__ == "__main__":
    system = StudentMarkManagementSystem()
    system.run()
