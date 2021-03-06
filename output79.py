class Student:
    #클래스 변수는 클래스명 바로 아래다 선언해야 함
    count = 0
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92),
    Student("김미화", 82, 86, 98, 88),
    Student("김연화", 88, 74, 78, 92),
    Student("박아현", 97, 92, 88, 95),
    Student("서준서", 45, 52, 72, 78)
]

print()
print("현재 생성된 총 학생 수는 {}명 입니다.".format(Student.count))