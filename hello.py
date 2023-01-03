# '변수'

a = 2
b = 3
print(a+b)

# '변수'

c = '대한'
d = '민국'

print(c+d)

# 자료형 (라이브러리)

e = ['사과', '배', '감']

print(e[0])

# 자료형 (딕셔너리)

f = {'name': '영수', 'age' : 24}

print (f['name'])

# 함수

def hey():
    print('헤이!')

hey()


def sum(a,b,c):
    return a+b+c


result = sum(1,2,3)

print(result)

# 조건문

age = 25

if age > 20 :
    print('성인입니다')
else:
    print('미성년자입니다')

# 반복문 (조건문 합침)

ages = [13,16,27,37,4,32,53]

for a in ages:
    if a > 20 :
        print('성인입니다')
    else:
        print('미성년자입니다')
