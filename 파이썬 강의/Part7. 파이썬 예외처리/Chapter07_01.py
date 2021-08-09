#Chapter07-1
# 예외처리

# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError, AttributeError
# FileNotFoundError, ZeroDivisionError

name = ['Kim', 'Lee', 'Park']

# 예제1
try :
    z = 'Kim'
    # x = 'Cho' => 에러발생
    x = name.index(z)
    print('{} Found it! {} in name.'.format(z, x + 1))
except ValueError :
    print('Not found it! - Occurred ValueError!')
else :
    print('Ok! else.')

print()

# 예제2
try :
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name.'.format(z, x + 1))
except Exception : # Exception 생략가능
    print('Not found it!')
else :
    print('Ok! else.')

print()

# 예제3
try :
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! {} in name.'.format(z, x + 1))
except Exception as e: 
    print(e) # 에러 내용 출력
    print('Not found it!')
else :
    print('Ok! else.')
finally : # 항상 실행
    print('Ok! finally!')

print()

# 예제4
# 예외 직접 발생 : raise
try :
    a = 'Park'
    if a == 'Kim' :
        print('Ok! Pass!')
    else :
        raise ValueError
except ValueError :
    print('Occurred! Exception!')
else :
    print('Ok! else.')
    
print()
