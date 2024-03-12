# ----------------------------- Data type: 숫자 ---------------------------- # 
print(5)
print(-10)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))


# ----------------------------- Data type: 문자열 ----------------------------- # 
print('풍선')
print("butterfly")
print("ㅋ"*9)  # 문자열과 정수 계산해서 출력 가능


# ----------------------------- Data type: Bool ----------------------------- # 
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not(5<10))


# ----------------------------- Variable ----------------------------- # 
animal = "강아지"
name = "해피"
age = 2
hobby = "먹기"
is_adult = age >= 3

print("우리집 " + animal + " 이름은 "+ name + "예요")
# print(name + "는" + str(age) +"살이며, " + hobby + "을 아주 좋아해요")
print(name, "는", age, "살이며, ", hobby, "을 아주 좋아해요")
print(name + "는" + " 어른일까요? " + str(is_adult))

'''주석처리'''

# # Quiz 1 ) 변수를 이용하여 다음 문장을 출력하시오.
# 변수명 : Station
# 변수값 : "사당", "신도림", "인천공항" 순서대로 입력
# 출력 문장 : XX행 열차가 들어오고 있습니다.

# answer)
station = "사당"
print(station+"행 열차가 들어오고 있습니다.")

station = "신도림"
print(station+"행 열차가 들어오고 있습니다.")

station = "인천공항"
print(station+"행 열차가 들어오고 있습니다.") 


# ----------------------------- Aggregate ----------------------------- # 
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) # 2^3
print(5%3)  # 2
print(10%3) # 1
print(5//3) # 몫 1
print(10//3) # 3
print(10 > 3) # True
print( 4 >= 7) # False
print (10 < 3) # False
print (5 <= 5) # True

print(3==3) # True
print(4==2) # False
print(3 + 4 == 7) # True

print(1 != 3) # True
print(not (1 != 3)) # False

print((3 > 0) and (3 < 5)) # True
print((3 > 0) & (3 < 5)) # True

print((3 > 0) or (3 > 5)) # True, False 둘 중 하나라도 True면 True
print((3 > 0) | (3 > 5)) # True

print(5 > 4 >3) # True
print(5 > 4 >7) # False

print(2 + 3 * 4) # 14
print((2+3) * 4) # 20

number = 2 + 3 * 4 # 14
print(number)
number = number + 2 # 16
print(number)
number += 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number -= 2
print(number)
number %= 5
print(number)


# ----------------------------- 숫자 처리 함수 ----------------------------- # 
print(abs(-5)) # 절대값 의미함 absolute = 5
print(pow(4, 2)) # 4^2 = 16
print(max(5, 12)) # 최대값 = 12
print(min(5, 12)) # 최소값 = 5
print(round(3.14)) # 반올림 = 3
print(round(4.99)) # 반올림 = 5

# math library에 있는 모든 함수 활용
from math import * 

print(floor(4.99)) # 내림 = 4
print(ceil(3.14)) # 올림 = 4
print(sqrt(16)) # 제곱급 = 4


# ----------------------------- random function ----------------------------- #
from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
# print(int(random() * 10)) # 정수로 출력
# print(int(random() * 10)) # 정수로 출력
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 정수로 출력
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 정수로 출력
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 정수로 출력
# print(int(random() * 10)+1) # 1 ~ 10 이하의 임의의 정수로 출력

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 정수로 출력
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 정수로 출력
print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 정수로 출력

print(int(randrange(1, 46))) # 1 ~ 46 미만의 임의의 값 생성
print(int(randrange(1, 46))) # 1 ~ 46 미만의 임의의 값 생성
print(int(randrange(1, 46))) # 1 ~ 46 미만의 임의의 값 생성

print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성
print(randint(1,45)) # 1 ~ 45 이하의 임의의 값 생성

# Quiz 2 ) 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건1 : 랜덤으로 날짜를 뽑아야 함        
# 조건2 : 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함    
# 조건3 : 매월 1~3일은 스터디 준비를 해야하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

# answer)
from random import *

offlineDate = int(randint(4,28))
print(f"오프라인 스터디 모임 날짜는 매월 {offlineDate}일로 선정되었습니다.")


# ----------------------------- 문자열 ----------------------------- #  
sentence = "나는 소년입니다."
print(sentence)
sentence2 = 'Python is easy'
print(sentence2)
sentence3 = '''
I am a boy and 
Python is easy
'''
print(sentence3)


# ----------------------------- Slicing ----------------------------- #  
jumin = "991023-1234589"

print("성별 : " + jumin[7]) # 1
print("연 : " + jumin[0:2]) # 실제 자리수보다 1자리 더해서 범위 적어주기[0:2] = 0~1자리 가져옴 = 99
print("월 : " + jumin[2:4]) # 2,3 자리에 있는 수 출력 = 10
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6자리수 직전까지 값
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지 값
print("뒤 7자리(뒤에서부터) : " + jumin[-7:])


# ----------------------------- 문자열 처리함수 ----------------------------- #  
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # True
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index+1)
print(index)

print(python.find("Java")) # -1 : 원하는값이 포함되어있지 않을 때 -1 반환 그리고 이어지는 메소드 실행
# print(python.index("Java")) # error : index의 경우는 해당값이 없을 때 error 내고 이어지는 메소드 실행 안함
print("hi")

print(python.count("n"))


# ----------------------------- 문자열 포맷 ----------------------------- #  
print("a" + "b")
print("a","b")

# 방법1 
print("나는 %d살입니다." %20)
print("나는 %s을 좋아해요." %"파이썬")
print("Apple은 %c로 시작해요" %"A")

# %s
print("나는 %s살입니다." %20)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간",age = 20))

# 방법4
age = 30 
color = "보라"
print(f'나는 {age}살이며, {color}색을 좋아해요.')


# ----------------------------- 탈출 문자 ----------------------------- #  
print("백문이 불여일견 \n백견이 불여일타") # \n: 줄바꿈
print('저는 "나도코딩"입니다.')
print("저는 '나도코딩'입니다.")
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서는 \ 
print("C:\\Users\\")

# \r: 커서를 맨 앞으로 이동
print("Red Apple\rPine")

# \b : backspace(한글자 삭제)
print("Redd\bApple")

# \t : tap기능과 같이 스페이스 넓게 줌
print("Red\tApple")

# Quiz 3) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!"로 구성
#             (nav)         
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"
password = url[7:]
password = password.split(".")[0]
password = str(password[:3])+str(len(password))+str(password.count("e"))+"!"
print(f'{url}의 비밀번호는 {password} 입니다.')

# answer)
url = "http://daum.com"
my_str = url.replace("http://","") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2 첨부터 .이 나오기 직전까지 출력
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))


# ----------------------------- List ----------------------------- #  
# 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20켱, 30명있음.
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

# 조세호씨가 몇번째 칸에 타고 있는가?
subway = ["유재석", "조세호" , "박명수"]
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# 정현돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway.pop())
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [4,2,3,5,1]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형과 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)


# ----------------------------- Dictionary ----------------------------- #  
# key, value 존재
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])   # 5라는 key가 없기 때문에 에러 발생시키고 끝냄
# print("hi")

print(cabinet.get(5)) # 5라는 key가 없지만 None출력시키고 다음 문장 실행
print(cabinet.get(5, "사용가능")) # 5라는 key가 없지만 None출력시키고 다음 문장 실행
print("hi")

print(3 in cabinet) # True
print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님
del cabinet["A-3"]
print(cabinet)

# key들만 출럭 
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# key, value쌍으로 출력 
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)


# ----------------------------- Tuple ----------------------------- #
# 리스트보다 빨고 변경되지 않는 목록 사용할 때 사용.
# 값 추가 변경 불가, 고정된 값에 쓸 수 있음

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

(name, age, hobby) = ("김종국", 30, "코딩")
print(name, age, hobby)


# ----------------------------- 집합 (Set) ----------------------------- #
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석","김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java할 줄 알지만 Python 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남 
python.add("김태호")
print(python)

# java를 까먹었어요
java.remove("김태호")
print(java)


# ----------------------------- 자료구조의 변경 ----------------------------- #
menu = {"커피","우유","쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# Quiz 4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다. 
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1 ~ 20이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가 
# 조건3 : random모듈의 shuffle과 sample활용 

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1 
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

from random import *

commenter=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(commenter)
chickenOne = sample(commenter, 1)
coffeeOne = sample(commenter, 3)
print(f"-- 당첨자 발표 -- \n치킨 당첨자 : {chickenOne} \n커피 당첨자 : {coffeeOne} \n -- 축하합니다 --")

# answer)
import random

# 댓글 작성자 아이디 리스트 생성
commenters = list(range(1, 21))
# 전체 당첨자 추첨
all_winners = random.sample(commenters, 4)
# 당첨자 분류
chicken_winner = all_winners[0]
coffee_winners = all_winners[1:]
# 결과 출력
print("-- 당첨자 발표 --")
print(f"치킨 당첨자 : {chicken_winner}")
print(f"커피 당첨자 : {coffee_winners}")
print("-- 축하합니다 --")
 
 
# ----------------------------- 분기: if ----------------------------- #  
weather = input("오늘 날씨는 어때요? ")
# if weather== "비" or weather == "눈":
if weather in ["비", "눈"]:  # or 대신 in 연산자 활용하여 리스트나 튜플에 넣고 사용 가능
    print("우산을 챙기세요")
elif weather== "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요.나가지 마세요")