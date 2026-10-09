# # 3. Create a class MedicalStudent inherited from Student with following:
# # i. Data members :Specialization
# # ii. MarksOfInternship
# # b. Add the following methods :
# # i. Parameterized constructor
# # ii. Display
# # iii. Accept
# # iv. override Method CalculateRank
# # v. Override __str__ Method

# class MedicalStudent(Student): 

#     def __init__(self, StudentId , Name , Age , Percentage , Specialization , MarksOfInternship):
#         super().__init__(StudentId,Name,Age,Percentage)
#         self.Specialization = Specialization
#         self.MarksOfInternship = MarksOfInternship

#     def Display(self):
#         super().Display()
#         print("Specialization =", self.Specialization)
#         print("Marks Of Internship =", self.MarksOfInternship)

#     def Accept(self):
#         super().Accept()
#         self.Specialization = input("Enter Specialization :")
#         self.MarksOfInternship = float(input("Enter Marks Of Internship :"))

#     def CalculateRank(self):
#         if self.Percentage >= 75 and self.MarksOfInternship >= 40:
#             return "Distinction"
#         elif self.Percentage >= 60 and self.MarksOfInternship >= 35:
#             return "First Class"
#         elif self.Percentage >= 50:
#             return "Second Class"
#         elif self.Percentage >= 35:
#             return "Pass"
#         else:
#             return "Fail"

#     # Override __str__
#     def __str__(self):
#         return f"StudentId={self.StudentId}, Name={self.Name}, Age={self.Age}, Percentage={self.Percentage}, Specialization={self.Specialization}, MarksOfInternship={self.MarksOfInternship}"


# m1 = MedicalStudent(101, "Siddhu", 22, 85.5, "Cardiology", 45)

# m1.Display()

# print("Rank =", m1.CalculateRank())

# print(m1)        