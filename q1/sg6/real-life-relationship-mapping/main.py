# Write a short Python code snippet showing a Course adding a Student object to a list. 
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_details(self):
        return self.name

class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

student1 = Student("101", "S001")
student2 = Student("102", "S002")

course = Course("Course")

course.add_student(student1)
course.add_student(student2)

print(course.course_name)
print("Enrolled Students:")
for student in course.students:
    print(student.get_details())