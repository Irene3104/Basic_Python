
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

