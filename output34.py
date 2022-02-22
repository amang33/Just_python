array = [1, 2, 3]

# 리스트 뒤에 요소 추가
print("*리스트 뒤에 요소 추가하기*")
array.append(4)
array.append(5)
print(array)
print()

# 리스트 요소를 중간에 추가(인덱스, 요소)
print("*리스트 중간에 요소 추가하기*")
array.insert(0, 10)
print(array)
print()

list_a = [1, 2 ,3]
# extend 여러 요소를 한 번에 추가 (리스트 확장)
list_a.extend([4, 5, 6])
print("[1, 2, 3].extend([4, 5, 6]) : ", list_a)