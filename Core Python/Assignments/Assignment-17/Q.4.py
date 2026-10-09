# 4. Create a class College which has collection of students. Add the
# following methods :
# a. Parameteried constructor for number of students.
# b. AddStudent
# c. GetStudent
# d. RemoveStudent
# e. Override __str__ Method

# class College:

#     # Parameterized Constructor
#     def __init__(self, n):
#         self.students = []
#         self.n = n

#     # Add Student
#     def AddStudent(self, student):
#         if len(self.students) < self.n:
#             self.students.append(student)
#             print("Student Added Successfully")
#         else:
#             print("College is Full")

#     # Get Student
#     def GetStudent(self, StudentId):
#         for student in self.students:
#             if student.StudentId == StudentId:
#                 return student

#         return None

#     # Remove Student
#     def RemoveStudent(self, StudentId):
#         student = self.GetStudent(StudentId)

#         if student != None:
#             self.students.remove(student)
#             print("Student Removed Successfully")
#         else:
#             print("Student Not Found")

#     # Override __str__
#     def __str__(self):
#         result = "College Students:\n"

#         for student in self.students:
#             result = result + str(student) + "\n"

#         return result


# # Create Student objects
# # s1 = Student(101, "Siddhu", 22, 85.5)
# # s2 = Student(102, "Rahul", 21, 72.5)
# # s3 = Student(103, "Priya", 22, 91.0)


# # Create College with capacity of 3 students
# c1 = College(3)

# # Add students
# c1.AddStudent(s1)
# c1.AddStudent(s2)
# c1.AddStudent(s3)

# # Get Student
# print("\nGet Student:")
# print(c1.GetStudent(102))

# # Display all students
# print("\nAll Students:")
# print(c1)

# # Remove Student
# print("\nRemoving Student:")
# c1.RemoveStudent(102)

# # Display after removing
# print("\nAfter Removing:")
# print(c1)