list_a = [1, 2, 3]

# list_a 주소를 저장하는게 아니라 새로운 주소를 만들어서 저장
output = list_a + list_a
print("# 리스트 연결 연산자 사용")
print("원본 리스트 : ", list_a)
print("연산 결과 : ", output)
print()

# extend() 사용시 기존 주소에 요소 1, 2, 3 만 읽을 수 있고 확장된 인덱스 값은 읽지 못함
output = list_a.extend([1, 2, 3])
print("# extend() 함수 사용")
print("원본 리스트 : ", list_a)
print("연산 결과 : ", output)