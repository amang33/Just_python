dictionary = {
    "name" : "7D 건조 망고",
    "type" : "당절임"
}

print("요소 제거 이전 : ", dictionary)

#key 를 이용해서 요소를 제거
del dictionary["name"]
print(dictionary)
del dictionary["type"]

# 요소만 제거되며 구조는 파괴되지 않음
print("요소 제거 이후 : ", dictionary)