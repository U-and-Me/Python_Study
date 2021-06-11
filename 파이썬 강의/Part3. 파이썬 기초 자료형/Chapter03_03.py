# Chapter03-3
# 리스트

# 선언
a = []
b = list()
c = [70, 75, 80, 85]
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]

# 인덱싱
print('>>>')
print('d -', type(d), d)
print('d -', d[1])
print('d -', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1][1])
print('e -', list(e[-1][1]))

# 슬라이싱
print('>>>')
print('d -', d[0:3])
print('d -', d[2:])
print('e -', e[-1][1:3])

# 리스트 연산
print('>>>')
print('c + d =>', c + d)
print('c * 3 =>', c * 3)
print("'Test' + c[0] =>", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)
temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print('>>>')
c[0] = 4
print('c -', c)
c[1:2] = ['a', 'b', 'c']    # [['a', 'b', 'c']]
print('c -', c)
c[1] = ['a', 'b', 'c'] # 중첩리스트
print('c -', c)
c[1:3] = []
print('c -', c)

del c[2] # 삭제
print('c -', c)
print()

# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a -', a)
a.append(10) # 데이터 추가
print('a -', a)
a.sort() # 정렬
print('a -', a)
a.reverse() # 역순
print('a -', a)
print('a -', a.index(3), a[3]) # 인덱스 가져오기
a.insert(2, 7) # 데이터 삽입
print('a -', a)
a.reverse()
print('a -', a)

a.remove(10) #데이터 삭제
print('a -', a)
print('a -', a.pop()) # LIFO
print('a -', a)
print('a -', a.pop())
print('a -', a)
print('a -', a.count(4)) # 원하는 데이터 갯수 찾기

ex = [8, 9]
a.extend(ex) # 데이터 이어붙이기
print('a -', a)

# pop 반복문
while a:
    data = a.pop()
    print(data)
