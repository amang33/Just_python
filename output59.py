def print_n_times(*values, n = 2):
    for i in range(n):
        for value in values:
            print(value)
        print()

#기본 매개변수 명을 입력 해줘야 함 n = 3 > n
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n = 3)