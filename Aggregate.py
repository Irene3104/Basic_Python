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
