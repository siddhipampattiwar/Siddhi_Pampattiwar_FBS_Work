print("Program Started")
from SY.SYMARKS import SYMARKS
from TY.TYMarks import TYMarks

class Student:
    def __init__(self, rollno, name, symarks, tymarks):
        self.rollno = rollno
        self.name = name
        self.symarks = symarks
        self.tymarks = tymarks

    def display(self):
        total = self.symarks.ComputerTotal + self.tymarks.Theory + self.tymarks.Practical

        percentage = total / 3

        if percentage >= 70:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        print("\n----- Student Result -----")
        print("Roll Number:", self.rollno)
        print("Name:", self.name)
        print("SY Computer Marks:", self.symarks.ComputerTotal)
        print("TY Theory Marks:", self.tymarks.Theory)
        print("TY Practical Marks:", self.tymarks.Practical)
        print("Total Marks:", total, "/ 300")
        print("Percentage:", percentage, "%")
        print("Grade:", grade)


# Creating objects
sy = SYMARKS(75, 80, 85)
ty = TYMarks(70, 80)

student1 = Student(101, "Siddhi", sy, ty)

student1.display()