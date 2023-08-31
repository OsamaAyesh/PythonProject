# Importing the Course and Student classes from their respective modules
from course import Course
from student import Student


# Function to get student level from user input
def get_student_level():
    while True:
        try:
            level = input("Enter student level (A/B/C): ").upper()
            if level in ["A", "B", "C"]:
                return level
            else:
                print("Invalid input. Please enter A, B, or C.")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt detected. Exiting.")
            exit()


# Function to get a student by their ID from a list of students
def get_student_by_id(student_list, student_id):
    for student in student_list:
        if student.student_id == student_id:
            return student
    return None


# Function to get a course by its ID from a list of courses
def get_course_by_id(course_list, course_id):
    for course in course_list:
        if course.course_id == course_id:
            return course
    return None


# Example usage and menu loop
courses = []  # List to store created courses
students = []  # List to store created students

while True:
    try:
        print("\nMenu:")
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Edit Student")
        print("4. Display All Students")
        print("5. Create New Course")
        print("6. Add Course to Student")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_name = input("Enter student name: ")
            student_level = get_student_level()

            new_student = Student(student_name, student_level)
            students.append(new_student)

            print("Student saved successfully.")

        elif choice == "2":
            student_id = int(input("Enter student ID: "))
            student_to_remove = get_student_by_id(students, student_id)

            if student_to_remove:
                students.remove(student_to_remove)
                print("Delete done successfully.")
            else:
                print("User does not exist.")

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            student_to_edit = get_student_by_id(students, student_id)

            if student_to_edit:
                new_name = input("Enter new name: ")
                new_level = get_student_level()

                student_to_edit.student_name = new_name
                student_to_edit.student_level = new_level
                print("Edit done successfully.")
            else:
                print("User does not exist.")

        elif choice == "4":
            print("\nStudent Details:")
            for idx, student in enumerate(students, start=1):
                print(f"Student {idx} (ID: {student.student_id}):")
                print(student.display_details())
                print()

        elif choice == "5":
            course_name = input("Enter course name: ")
            course_level = input("Enter course level (A/B/C): ").upper()
            new_course = Course(course_name, course_level)
            courses.append(new_course)
            print("Course created successfully.")

        elif choice == "6":
            student_id = int(input("Enter student ID: "))
            student = get_student_by_id(students, student_id)

            if student:
                course_id = int(input("Enter course ID: "))
                course = get_course_by_id(courses, course_id)

                if course:
                    student.add_course(course)
                else:
                    print("Course does not exist.")
            else:
                print("User does not exist.")

        elif choice == "7":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting.")
        exit()
