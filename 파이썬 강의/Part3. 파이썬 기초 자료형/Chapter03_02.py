# Chapter03-2
# 문자형

# 문자열 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1), type(str2), type(str3), type(str4))
print(len(str1), len(str2), len(str3), len(str4)) # 문자열 길이 구하기
print()

str1_t1 = ''
str2_t2 = str()
print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))
print()

# 이스케이프 문자
print("I'm Boy")
print('I\'m Boy')
print('I\\m Boy')

print('a \t b')
print('a \"\" b')

escape_str1 = "Do you have a \"retro games\"?"
print(escape_str1)
escape_str2 = 'What\'s on TV?'
print(escape_str2)

t_s1 = "Click \t Start!"
t_s2 = "New Line \nCheck!"
print(t_s1)
print(t_s2)
print()

# Raw String
raw_s = r'D:\python\test'
print(raw_s)

# 멀티라인 - 역슬래시 사용
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""
print(multi_str)

# 문자열 연산
str_o1 = "python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('z' in str_o1)
print('P' not in str_o2)
print()

# 문자열 형변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))
print()

# 문자열 함수
print("Capitalize :", str_o1.capitalize()) # 첫글자를 대문자로 바꾸기
print("endswith :", str_o2.endswith("s")) # 마지막 문자가 무엇인지
print("replace :", str_o1.replace("thon", "Good")) # 일부 문자열 변경
print("sorted :", sorted(str_o1)) # 정렬
print("split :", str_o4.split(' ')) # 문자열 나누기
print()

# 반복(시퀀스)
im_str = "Good Boy!"
print(dir(im_str))

for i in im_str:
    print(i)
print()
    
# 슬라이싱
str_s1 = "Nice Python"
print(len(str_s1)) # str_s1의 길이
print(str_s1[0:3])
print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[1:9:2])
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])
print(str_s1[::-1]) # 역순으로 출력
print()

# 아스키 코드
a = 'z'
print("z :", ord(a))
print("122 :", chr(122))
