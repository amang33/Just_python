# n=2 >매개변수 기본값 설정(기본 매개변수)
# 기본 매개변수 뒤에는 일반 매개변수 올 수 없음
def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times("안녕하세요")
print()
# 기본값 설정을 해 줘도 값을 넣을 수 있음
print_n_times("안녕하세요", 4)