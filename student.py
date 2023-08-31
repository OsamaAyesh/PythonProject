class Student:
    # Static variable to keep track of the next student ID to be assigned
    next_student_id = 1

    def __init__(self, student_name, student_level):
        # Assign a unique student ID to each student and increment the next student ID for the next student
        self.student_id = Student.next_student_id
        Student.next_student_id += 1
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = [] # Initialize an empty list to store enrolled courses

    def add_course(self, course):
        # Check if the course level matches the student's level before adding it to the student's courses
        if course.course_level == self.student_level:
            self.student_courses.append(course)
            print(f"Added course '{course.course_name}' to student '{self.student_name}'")
        else:
            print(f"Course level '{course.course_level}' does not match student level '{self.student_level}'")

    def display_details(self):
        # Construct a formatted string containing the student's information and enrolled course names
        course_names = ', '.join(course.course_name for course in self.student_courses)
        details = (
            f"Student Name: {self.student_name}\n"
            f"Student Level: {self.student_level}\n"
            f"Courses Enrolled: {course_names}"
        )
        return details
