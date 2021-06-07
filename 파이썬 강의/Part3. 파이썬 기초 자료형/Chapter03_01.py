# Chapter03-1 

# 자료형
"""
int : 정수                flaot : 실수
complex : 복소수          bool : 불린
str : 문자열(시퀀스)      list : 리스트(시퀀스)
tuple : 튜플(시퀀스)      set : 집합
dict : 사전
"""

# 데이터 타입
str1 = "Python"
bool = False
str2 = 'Anaconda'
float_v = 10.0
int_v = 7
list = [str1, str2]
print(list)
dict = {
    "name" : "Machine Learning",
    "version" : 2.0
}
tuple = (7, 8, 9) # 괄호 생략 가능
set = {2, 3, 4}

print(type(str1))
print(type(bool))
print(type(float_v))
print(type(int_v))
print(type(dict))
print(type(tuple))
print(type(set))
print()

# 숫자형
i = 77
i2 = -14
big_int = 893893923903091990319034344932893209802349803248901309

print(i)
print(i2)
print(big_int)
print()

# 실수
f = 0.999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9

print(f)
print(f2)
print(f3)
print(f4)

# 연산
i1 = 39
i2 = 939
big_int1 = 4909328438938932402890248010
big_int2 = 6892083402934023480289784827
f1 = 1.234
f2 = 3.939

print()
print("i1 + i2 = ", i1 + i2)
print("big_int1 + big_int2 = ", big_int1 + big_int2)
print("f1 + f2 = ", f1 + f2)
print()
print("i1 * i2 = ", i1 * i2)
print("big_int1 * big_int2 = ", big_int1 * big_int2)
print("f1 * f2 = ", f1 * f2)

# 형변환
a = 3.
b = 6
c = .7
d = 12.7

print()
print(type(a), type(b), type(c), type(d))

print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1, False : 0
print(float(False))
print(complex(3))
print(complex('3'))
print()

# 수치연산함수
print(abs(-7))
x, y = divmod(100, 8)
print(x, y) # x : 몫, y : 나머지
print(pow(5, 3), 5**3)
print()

# 외부 모듈
import math
print(math.pi)
print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수
