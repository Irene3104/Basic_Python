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
