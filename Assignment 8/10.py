class Student:
    def __init__(self, name):
        self.name = name
        
s = Student("John")

print("Class name:", s.__class__.__name__)
