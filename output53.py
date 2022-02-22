numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
# continue 현재 반복 생략하고 다음 반복 실행 시 사용(현재 반복 건너뛰기)
    if number < 10:
        continue
    print(number)