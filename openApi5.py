import re, usecsv

English = '''he is a vegetarian. she does not eat meat. she thinks that animals should not be killed.
It is hard for her to hang out with people. Many people like to eat meat.
she told his parents not to have meat. they laughed at her. She realized they couldn\t give up meat.'''

Korean = '''그녀는 채식주의자입니다. 그녀는 고기를 먹지 않습니다.
그녀는 동물을 죽이지 말아야한다고 생각합니다. 그녀가 사람들과 어울리는 것은 어렵습니다.
많은 사람들이 고기를 좋아합니다. 그녀는 부모에게 고기를 먹지 말라고 말했습니다.
그들은 그녀를 비웃었다. 그녀는 그들이 고기를 포기할 수 없다는 것을 깨달았습니다.'''

Korean_list = re.split('\.', Korean)
## split() 함수로 한글 문장을 나눠 Korean_list에 저장
English_list = re.split('\.', English)
## split() 함수로 영문을 나눠 English_list에 저장

print(Korean_list)

total = []
## ㅊㄴㅍ 형 자료를 저장할 빈 리스트를 하나 생성
for i in range(len(English_list)):
    total.append([English_list[i], Korean_list[i]])
## 첫 번째 열에 영어 문장, 두 번째 열에 한국어 문장이 들어 있는 리스트를 total추가
usecsv.writecsv('Korean_English.csv', total)