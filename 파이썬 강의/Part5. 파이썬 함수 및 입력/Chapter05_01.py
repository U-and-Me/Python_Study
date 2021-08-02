# Chapter05-1
# 함수식 및 람다

# 예제1
def first_func(w) :
    print("Hello,", w)

word = 'student1'
first_func(word)

# 예제2
def return_fuce(w) :
    return "Hello, " + str(w)

x = return_fuce('student2')
print(x) 

# 예제3 (다중반환)
def func_mul(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3
    
x, y, z = func_mul(10)
print(x, y, z)
    
# 튜플 리턴
def func_mul2(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)
    
q = func_mul2(20)
print(type(q), q, list(q))

# 리스트 리턴
def func_mul3(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]
    
p = func_mul3(30)
print(type(p), p, set(p))

# 딕셔너리 리턴
def func_mul4(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}
    
d = func_mul4(30)
print(type(d), d, d.get('v2'), d.items(), d.keys())
print()

# *args(언팩킹) - 튜플
def args_func(*args) :
    for i, v in enumerate(args) :
        print('Result : {}'.format(i), v)
    print('------')

args_func('Lee')
args_func('Lee', 'Park')
args_func('Lee', 'Park', 'Kim')
print()

# **kwargs(언팩킹) - 딕셔너리
def kwargs_func(**kwargs) :
    for v in kwargs.keys() :
        print("{}".format(v), kwargs[v])
    print('------')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park')
kwargs_func(name1 = 'Lee', name2 = 'Park', name3 = 'Kim')
print()

# 전체 혼합
def example(args_1, args_2, *args, **kwargs) :
    print(args_1, args_2, args, kwargs)
    
example(10, 20, 'Lee', 'Kim', 'Park', age1 = 20, age2 = 30, age3 = 40)
print()

# 중첩함수
def nested_func(num) :
    def func_in_func(num) :
        print(num)
    print('In func')
    func_in_func(num + 100)

nested_func(100)
print()

# 람다식 예제
def mul_func(x, y) :
    return x * y
print(mul_func(10, 50))
    
lambda_mul_func = lambda x, y : x * y
print(lambda_mul_func(50, 50))

def func_final(x, y, func) :
    print(x * y * func(100, 100))
func_final(10, 20, lambda x, y : x*y)
