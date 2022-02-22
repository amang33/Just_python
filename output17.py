# input 시 사용자가 숫자를 입력해도 문자열로 들어옴 > float 함수로 숫자로 변경해줌
input_a = float(input("첫 번째 숫자 > "))
input_b = float(input("두 번째 숫자 > "))

print("덧셈 결과 : ", input_a + input_b)
print("뺄셈 결과 : ", input_a - input_b)
print("곱셈 결과 : ", input_a * input_b)
# 실수형(소수 자리까지 지원함)
print("나눗셈 결과 : ", input_a / input_b)
print("몫 결과 : ", input_a // input_b)
print("나머지 결과 : ", input_a % input_b)