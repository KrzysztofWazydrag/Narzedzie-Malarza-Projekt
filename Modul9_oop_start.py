class Student:
    def __init__(self, first_name: str, last_name: str, semester: int = 1):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = semester

    def __str__(self):
        return (f'His name is {self.first_name}, last name is {self.last_name} and he is on his {self.semester} semester.')

    def promote(self):
        self.semester += 1

george = Student('George', 'Jetson', 1)
print(george)
george.promote()
print(george.first_name, george.last_name, george.semester)
george.promote()
print(george.first_name, george.last_name, george.semester)