class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    def get_average(self):
        return self.get_sum() / 4
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum, self.get_average)

student = Student("윤인성", 87, 98, 88, 95)

# 어떤 클래스의 인스턴스인지 확인
# isinstance(객체(인스턴스), 클래스)
print("isinstance(student, student) :", isinstance(student, Student))