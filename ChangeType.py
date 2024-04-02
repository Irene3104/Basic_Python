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
 