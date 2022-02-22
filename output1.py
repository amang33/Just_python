import os

print("현재 운영체제 :", os.name)
print("현재 폴더 :", os.getcwd())
print("현재 폴더 내부의 요소 :", os.listdir())

# # mkdir = 폴더 생성
# os.mkdir("hello")
# # rmdir = 폴더 삭제
# os.rmdir("hello")

# # 파일 생성(w = 입력)
# with open("original.txt", "w") as file:
# # 파일 내부 hello 입력
#     file.write("hello")
# os.rename("original.txt", "new.txt")

# os.remove("new.txt")
# # os.unlink("new.txt")

os.system("dir")