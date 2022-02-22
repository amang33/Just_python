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
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())

        # eq = equal(같다)
    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
        # ne = not equal(같지 않다)
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
        # gt = greater than(크다)
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
        # ge = greater than or equal(크거나 같다)
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
        # lt = less than(작다)
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
        # le = less than or equal(작거나 같다)
    def __le____(self, value):
        return self.get_sum() <= value.get_sum()
    
student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)

# 비교 연산자는 항상 왼쪽이 기준
print("student_a == student_b =", student_a == student_b)
print("student_a != student_b =", student_a != student_b)
print("student_a > student_b =", student_a > student_b)
print("student_a >= student_b =", student_a >= student_b)
print("student_a < student_b =", student_a < student_b)
print("student_a <= student_b =", student_a <= student_b)