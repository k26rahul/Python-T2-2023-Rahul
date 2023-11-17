class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_info(self):
        print(f'{self.name}:{self.marks}')
