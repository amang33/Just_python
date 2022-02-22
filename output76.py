class Student:
    def study(self):
        print("공부를 합니다.")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

# 반복문과 조건문을 통해 인스턴스가 어느 클래스에 속해 있는지 확인
for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()