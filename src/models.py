from src.student import Student
import csv
class Student_Model:
    def __init__(self):
        self.students =[]
    
    def add_students(self,std):
        self.students.append(std)
    def show_student_details(self,name):
        for std in self.students:
            if std.name.lower()==name.lower():
                print(std.__str__())
    def save(self):
        with open("file.csv" ,"w" ,newline='') as f:
            fieldnames =  ['name', 'roll_no', 'marks','percentage']  
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            writer.writeheader()
            for std in self.students:
                writer.writerow({'name':std.name,
                              'roll_no':std.roll_no,
                              'marks':std.marks,
                              'percentage':std.calculate_percentage()})
    def load(self):
        with open("file.csv" ,"r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row['name']
                roll_no = row['roll_no']
                marks = eval(row['marks'])
                student = Student(name, roll_no, marks)
                self.students.append(student)
    def show_all_students(self):
        for std in self.students:
            print(std.__str__())
            


if __name__ == "__main__":
    std = Student("John", 101, {"Math": 90, "Science": 85})
    model = Student_Model()
    model.add_students(std)
    model.show_student_details("John")
    model.save()



    
    
    

    
