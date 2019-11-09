# This is the student object with information that can be used to leverage a particular type of queue.
class Student:
    def __init__(self, name, year=None, class_grade=None):
        self.name = name
        self.year = year
        self.class_grade = class_grade

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_class_grade(self):
        return self.class_grade


