from collections import Counter
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def __str__(self):
        return f"Name:{self.name},Roll_no:{self.roll_no},Marks:{self.marks}"
    def calculate_average_marks(self):
        all_result=list(self.marks.values())
        return sum(all_result)/len(all_result)
    def calculate_percentage(self):
        value_count = len(self.marks)
        return self.calculate_average_marks()/(50*value_count)*100    

