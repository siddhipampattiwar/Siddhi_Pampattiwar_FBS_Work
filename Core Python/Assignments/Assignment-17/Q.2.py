# # 2. Create a derived class from Student as EnggStudent with :
# # a. Data members as :
# # i. Branch
# # ii. InternalMarks
# # b. Add the following methods :
# # i. Parameterized constructor
# # ii. Display
# # iii. Accept
# # iv. override Method CalculateRank

# class EnggStudent(Student):
    
#     def __init__(self, StudentId, Name, Age, Percentage, Branch, InternalMarks):
#         super().__init__(StudentId, Name, Age, Percentage)
#         self.Branch = Branch
#         self.InternalMarks = InternalMarks

#     def Display(self):
#         super().Display()
#         print("Branch =", self.Branch)
#         print("Internal Marks =", self.InternalMarks)

#     def Accept(self):
#         super().Accept()
#         self.Branch = input("Enter Branch :")
#         self.InternalMarks = float(input("Enter Internal Marks :"))

#     def CalculateRank(self):
#         if self.Percentage >= 75 and self.InternalMarks >= 40:
#             return "Distinction"
#         elif self.Percentage >= 60 and self.InternalMarks >= 35:
#             return "First Class"
#         elif self.Percentage >= 50:
#             return "Second Class"
#         elif self.Percentage >= 35:
#             return "Pass"
#         else:
#             return "Fail"


# # Object should be outside the class
# e1 = EnggStudent(101, "Siddhu", 22, 85.5, "AI", 23)

# e1.Display()

# print("Rank =", e1.CalculateRank())