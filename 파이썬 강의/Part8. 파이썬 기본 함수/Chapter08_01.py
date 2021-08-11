#Chapter08-1
# 파이썬 내장함수

# 절대값 abs()
print(abs(-3))

# all, any : iterable 요소 검사(참, 거짓)
print(all([1, 2, 3])) # and
print(all([1, 2, 3, '']))
print(any([1, 2, 0])) # or

# chr : 아스키 -> 문자, ord : 문자 -> 아스키
print(chr(44))
print(ord('T'))

# enumerate : 인덱스 + iterable 객체 생성
for i, name in enumerate(['abc', 'bcd', 'efg']) :
    print(i, name)
    
# filter : 반복가능한 객체 요소를 지정한 함수 조건에 맞는 값을 추출
def conv_pos(x) :
    return abs(x) > 2
    
print(list(filter(conv_pos, [1, -3, 2, 0, -5, 6])))
print(list(filter(lambda x : abs(x) > 2, [1, -3, 2, 0, -5, 6])))

# id : 객체의 주소값(레퍼런스) 반환
print(id(int(5)))
print(id(4))

# len : 요소의 길이 반환
print(len('abcdefg'))
print(len([1, 2, 3, 4, 5, 6, 7]))

# max, min : 최대값, 최소값
print(max([1, 2, 3]))
print(max('python study'))
print(min([1, 2, 3]))
print(min('python study'))

# map : 반복가능한 객체 요소를 지정한 함수 실행 후 추출
def conv_abs(x) :
    return abs(x)
    
print(list(map(conv_abs, [-3, 2, 0, 1, -5, 6])))
print(list(map(lambda x : abs(x), [-3, 2, 0, 1, -5, 6])))

# pow : 제곱값 반환
print(pow(2, 10))

# range : 반복가능한 객체(Iterable) 반환
print(range(1, 10, 2))
print(list(range(1, 10, 2)))
print(list(range(0, -15, -1)))

# round : 반올림
print(round(6.5781, 2))
print(round(5.6))

# sorted : 반복가능한 객체(Iterable) 정렬 후 반환
print(sorted([6, 7, 4, 3, 2, 1])) # 오름차순
print(sorted(['p', 'y', 't', 'h', 'o', 'n']))

# sum : 반복가능한 객체(Iterable) 합 반환
print(sum([6, 7, 8, 9, 10]))
print(sum(range(1, 101)))

# type : 자료형 확인
print(type(3))
print(type({3, 4})) # set
print(type({})) # dict
print(type(()))
print(type([]))

# zip : 반복가능한 객체(Iterable)의 요소를 묶어서 반환
print(list(zip([10, 20, 30], [40, 50, 60])))
print(list(zip([10, 20, 30], [40, 50])))

print(type(list(zip([10, 20, 30], [40, 50, 60]))[0]))
