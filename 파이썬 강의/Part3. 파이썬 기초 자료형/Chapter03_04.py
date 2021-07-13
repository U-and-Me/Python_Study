# Chapter03-4
# 튜플

# 선언
a = ()
b = (1,)
print(type(a), type(b))

c= (11, 12, 13, 14)
d = (100, 1000, 'Ace', "Base", 'Captine')
e = (100, 1000, ('Ace', "Base", 'Captine'))

# 인덱싱
print('>>>>>')
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('d -', e[-1]) # 튜플 반환
print('d -', e[-1][1])
print('d -', list(e[-1][1])) # 리스트로 형변환

# 수정
#d[0] = 1500  => 오류

# 슬라이싱
print()
print('>>>>>')

print('d -', d[0:3])
print('d -', d[2:])
print('d -', e[2][1:3])

# 튜플 연산
print()
print('>>>>>')

print('c + d =>', c + d)
print('c * 3 =>', c * 3)

# 튜플 함수
print()
print('>>>>>')

a = (5, 2, 3, 1, 4)
print('a -', a)
print('a -', a.index(3))    # 숫자 3의 인덱스 위치
print('a -', a.count(2))    # 숫자 2의 개수

# 팩킹 & 언팩킹
print()
print('>>>>>')

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])
print(t[-1])
print()

# 언팩킹
(x1, x2, x3, x4) = t
print(x1, x2, x3, x4)
print(type(x1), type(x2), type(x3),type(x4))

print('>>>>>')
t2 = 1, 2, 3
t3 = 4,
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
