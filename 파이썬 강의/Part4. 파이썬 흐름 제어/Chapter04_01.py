# Chapter04-1
# 제어문

# 기본 형식
print(type(True)) # 0이 아닌 수, "abc", [1, 2, 3..], (1, 2, 3..) ...
print(type(False)) # 0, "", [], (), {}...

# if
if True :
    print('Good')
if False :
    print('Bad')

# if ~ else
if False :
    print('Bad!')
else :
    print('Good!')
print()

# 관계연산자
x = 15
y = 10
print(x == y)
print(x != y)

# 예제1
city = ""
if city :
    print("You are in :", city)
else :
    print("Please enter your city")

# 예제2
city2 = "Seoul"
if city2 :
    print("You are in :", city2)
else :
    print("Please enter your city") 
print()

# 논리연산자
a = 75
b = 40
c = 10

print('and :', a > b and b > c) # a > b > c
print('or :', a > b or b > c)
print('not :', not a > b)
print('not :', not b > c)
print()

# 산술, 관계, 논리 우선순위
print('e1 :', 3 + 12 > 7 + 3)
print('e2 :', 5 + 10 * 3 > 7 + 3 * 20)
print('e3 :', 5 + 10 > 3 and 7 + 3 == 10)
print('e4 :', 5 + 10 > 0 and not 7 + 3 == 10)
print()

# 예제3
score1 = 90
score2 = 'A'
if score1 >= 90 and score2 == 'A' :
    print('Pass')
else :
    print('Fail')

# 예제4
id1 = 'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin' :
    print('관리자 입장')

if id2 == 'admin' and grade == 'platinum' :
    print('최상위 관리자')
    
# 예제5
num = 85

if num >= 90 :
    print('Grade : A')
elif num >= 80 :
    print('Grade : B')
elif num >= 70 :
    print('Grade : C')
else :
    print('Grade : D')
    
# 예제6
grade = 'A'
total = 95

if grade == 'A' :
    if total >= 90 :
        print('장학금 100%')
    elif total >= 80 :
        print('장학금 80%')
    else :
        print('장학금 50%')
else :
    print('장학금 없음')
print()
    
# in, not in
q = [10, 20, 30]
w = {70, 80, 90, 100}
e = {"name" : "Lee", "city" : "Seoul", "grade" : "A"}
r = (10, 12, 14)

print(15 in q)
print(90 in w)
print(12 not in r)
print("name" in e)
print("Seoul" in e.values())        
