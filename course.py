class Course:
    # Class variable to keep track of the next course ID
    next_course_id = 1

    def __init__(self, course_name, course_level):
        # Assign a unique course ID to each course and increment the next course ID for the next course
        self.course_id = Course.next_course_id
        Course.next_course_id += 1
        self.course_name = course_name
        self.course_level = course_level

    def __str__(self):
        # Return a string representation of the course, including its ID, name, and level
        return f"Course ID: {self.course_id}\nCourse Name: {self.course_name}\nCourse Level: {self.course_level}"