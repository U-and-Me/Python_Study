# Chapter02-1 Print 사용법

print('Python Start!')
print("Python Start!")
print('''Python Start!''')
print("""Python Start!""")

print() # 줄바꿈

# separator 옵션
print('P', 'Y', 'T', 'H', 'O', 'N', sep ='|')
print('010', '1234', '5789', sep ='-')
print('s2005', 'e-mirim.hs.kr', sep = '@')

print()

# end 옵션
print('Welcome to', end = ' ')
print('IT News', end = ' - ')
print('Web Site')

print()

# file 옵션
import sys
print('Learn Python', file = sys.stdout)

print()

# format 사용(d, s, f)
print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' %('nice'))
print('{:>10}'.format('nice'))

print('%-10s' %('nice'))
print('{:10}'.format('nice'))

print('{:~>10}'.format('nice'))
print('{:^10}'.format('nice')) # 가운데 정렬

print('%.5s' %('nice'))
print('%.5s' %('pythonstudy')) # 문자열 슬라이싱
print('{:10.5}'.format('pythonstudy'))

print()

# %d
print('%d %d' %(1, 2))
print('{} {}'.format(1, 2))
print('%4d' %(42))
print('{:4d}'.format(42))

print()

# %f
print('%f' %(3.14159265))
print('{:f}'.format(3.14159265))

print('%06.2f' %(3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))
