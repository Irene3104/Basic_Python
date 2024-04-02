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