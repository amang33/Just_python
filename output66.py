def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#  n 이 1보다 크면 n * (n-1)!을 리턴
print("1! : ", factorial(1))
print("2! : ", factorial(2))
print("3! : ", factorial(3))
print("4! : ", factorial(4))
print("5! : ", factorial(5))