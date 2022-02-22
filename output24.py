import datetime

now = datetime.datetime.now()

# 오전
if now.hour < 12:
    # format은 {} 과 1:1 대응
    print("현재 시간은 {}시로 오전입니다!".format(now.hour))
# 오후
if now.hour >= 12:
    print("현재 시간은 {}시로 오후입니다!".format(now.hour))