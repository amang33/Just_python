def test(a, b=10, c=100):
    print(a + b + c)

# 기본형태
test(10, 20, 30)
# 키워드로 매개변수를 지정한 상태
test(a= 10, b = 100, c = 200)
# 키워드로 지정시 순서 상관없음
test(c = 10, a = 100, b = 200)
# 일부 매개변수만 지정시 지정되지 않은 매개변수는 기본 매개변수 값 적용 b = 10
test(10, c = 200)