# Chapter02-2 변수

# 기본선언
n = 700

# 출력
print(n)
print(type(n)) # 타입 출력

# 동시선언
x = y = z = 700
print(x, y, z)

var = 75
var = "Change Value" # 재선언
print(var)
print(type(var))

# Object References
print(300)
print(int(300))

n = 777
print(n, type(n))

m = n
print(m, n)
m = 400
print(m, n)
print(type(m), type(n))

# id확인 : 객체의 고유값 확인
m = 800
n = 655

print()
print(id(m))
print(id(n))
print(id(m) == id(n))

# 같은 오브젝트 참조
m = 800
n = 800
print()
print(id(m))
print(id(n))
print(id(m) == id(n))

# 다양한 변수선언
# Camel Case -> Method / Pascal Case -> Class / Snack Case -> 변수
age = 18
Age = 19
aGe = 20
AGE = 21
a_g_e = 22
_age = 23

# 예약어
# for = 3 
# as = 4
# class = 5  => 에러 발생
