def sum_all(start = 0, end = 100, step = 1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

# 기본 매개변수 사용으로 조금 더 편해짐(이전 코드 보다)
print("A. ", sum_all(0, 100, 10))
print("B. ", sum_all(end = 100))
print("C. ", sum_all(end = 100, step = 2))
