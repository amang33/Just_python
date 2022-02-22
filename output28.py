import datetime

now = datetime.datetime.now()
month = now.month

# 다중 if 구문을 사용시엔 elif 를 사용하면 됨
if 3 <= month <= 5:
    print("현재는 봄입니다")
elif 6 <= month <= 8:
    print("현재는 여름입니다")
elif 9 <= month <= 11:
    print("현재는 가을입니다")
else:
    print("현재는 겨울입니다")