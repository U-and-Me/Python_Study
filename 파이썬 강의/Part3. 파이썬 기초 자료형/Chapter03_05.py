# Chapter03-5
# 딕셔너리

# 선언
a = {'name' : 'Kim', 'phone' : '01033337777', 'birth' : '040920'}
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name' : 'Niceman',
    'City' : 'Seoul',
    'Age' : 18,
    'Grade' : 'A',
    'Status' : True
}
e = dict([
    ('Name', 'Niceman'),
    ('City', 'Seoul'),
    ('Age', 18),
    ('Grade', 'A'),
    ('Status', True)
])

f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 18,
    Grade = 'A',
    Status = True
)

# 출력
print('a -', type(a), a)
print('b -', type(b), b)
print('c -', type(c), c)
print('d -', type(d), d)
print('e -', type(e), e)
print('f -', type(f), f)
print()

print('a -', a['name'])
print('a -', a.get('name')) # 키가 없을 경우 None 반환
print('b -', b[0])
print('b -', b.get(0))
print('f -', f.get('City'))
print('f -', f.get('Age'))
print()

# 딕셔너리 추가
a['address'] = "Seoul"
print('a -', a)
a['rank'] = [1, 2, 3]
print('a -', a)
print()

print('a -', len(a))
print('b -', len(b))
print('c -', len(c))
print('d -', len(d))
print()

# 관련 함수
print('a - ', a.keys()) # 키만 가져오기
print('b - ', b.keys())
print('c - ', c.keys())
print('d - ', d.keys())
print()

print('a - ', list(a.keys())) # 리스트 형변환
print('b - ', list(b.keys()))
print()

print('a - ', a.values()) # 값만 가져오기
print('b - ', b.values())
print('c - ', c.values())
print()

print('a - ', a.items()) # 키, 값 모두 가져오기
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items())) # 리스트 형변환
print('b - ', list(b.items()))
print()

print('a - ', a.pop('name'))
print('a -', a)
print('c - ', c.pop('arr'))
print('c -', c)
print()

print('f -', f.popitem()) # 랜덤으로 키, 값 빼기
print('f -', f)
print('f -', f.popitem())
print('f -', f)
print()

print('a -', 'birth' in a) # a에 해당 키가 있는지
print('d -', 'city' in d)

# 수정
a['test'] = 'test_dict'
print('a -', a)

a['address'] = 'Busan'
print('a -', a)

a.update(birth = '210721')
print('a -', a)
temp = {'address' : 'Jeju'}
a.update(temp)
print('a -', a)
