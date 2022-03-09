class student:
    def __init__(self, Name, F_name, Grade):
        self.Name = Name
        self.F_name = F_name
        self.Grade = Grade

student1 = student("John", "Smith", 10)
student2 = student("Singh", "Kumar", 12)
print(student2.F_name)
print(student1.Grade)