# 파이참 단축키는 [Help]-[Key Reference] 참조
# Ctrl+D 한줄 복붙
# 여러줄 주석 기능 : 인용부호 3개 이용

'''
여러줄
    주석입니다.
'''
print('출력문')


# 출력문 1
# print(값/수식/변수, end='대체문자나 공백') 문
print('안녕하세요 ^^')
print(123)
print(100*45)

# 변수명=값
txt = '홍길동'

# 출력문 2 : end 옵션을 이용
# print(값/수식/변수, end='대체문자나 공백')
# 100 200 300
print(100, end=' ')
print(200, end=' ')
print(300)

print(100, end=' / ')
print(200, end=' / ')
print(300)


# 출력문 3 : 쉼표를 이용한 출력문
# print(값/수식/변수,값/수식/변수,값/수식/변수,...)
user1 = '영희'
user2 = '철수'
print()
print(user1,user2,'즐거운 하루!!!')


# 이스케이프 코드 : 특수문자
# \n 개행, \t 여백
# \\ (\표시)
# \', \" (인용부호표시)
user1 = '영희'
user2 = '철수'
print('\t\t',user1, '\n\n\t=======',user2,)
print('\'철수야 놀자\'')


# 변수 할당 방법
# 변수 = 수식 또는 값

# 변수로 사용할 수 없는 파이썬 예약어 확인하기
import keyword
print(keyword.kwlist)
print('키워드 갯수는? ', len(keyword.kwlist))


# 변수 할당 방법 2
# 쉼표(,)를 이용한 변수 할당
# 변수1, 변수2 = 값1, 값2
p1, p2, p3 = 'sql', 'python', 'html'
print(p1, p2, p3)


# 퀴즈 : user1, user2의 변수값을 서로 변경하여라
user1 = "영희"
user2 = "철수"
# 변수 교체 프로그래밍
# 방법 1: 중간변수 설정
temp = user1
user1 = user2
user2 = temp
print('============')
print(user1,user2) # 철수 영희

# 방법 2: 쉼표를 이용한 변수 교체
user1,user2 = user2, user1
print('============')
print(user1,user2) # 영희 철수


# 변수명 정의방식
# 카멜표기법 : 대문자소문자로 단어 분리
# userAge
# 스네이크 기법 : _, - 단어연결
# user_age

# 변수 < 집합형변수 < 함수 < 클래스 < 라이브러리 < 패키지
# 클래스명은 첫글자를 대문자로 표시
# 함수명은 소문자로 표시
# 변수명은 소문자로 시작
# 예약어는 변수명으로 사용할 수 없다


# 변수 삭제 del(변수명)
msg = '오늘도 좋은 하루'
print('msg =',msg)
del msg  # 변수삭제
# print('msg =',msg)  - 오류남 NameError: name 'msg' is not defined



# 데이터형 확인하기
# type(변수/값)

# 자료형의 종류

# 기본자료형
# : 숫자형(정수, 실수)
# : 문자열형
# : 논리형 Boolean - True / False

# 집합자료형
# : 리스트, 튜플, 딕셔너리, 집합

# 데이터형 확인하기
# type(변수/값)

a = 100
b = 3.14
c = 'Hello World'
d = True
e = '''
머신러닝
딥러닝
데이터분석
시각화'''
print('\n\n')
print(a, type(a))  # 100 <class 'int'>
print(b, type(b))  # 3.14 <class 'float'>
print(c, type(c))  # Hello World <class 'str'>
print(d, type(d))  # True <class 'bool'>
print(e, type(e))  # <class 'str'>


# 입력문
# 변수명 = input(메시지)
# 입력받은 변수의 데이터형은 문자열이다

myMessage = input('메세지를 입력하세요... ')
print('입력값 = ', myMessage)



# 자료형 변환 - Casting
# int(값/수식/변수) : 정수형 데이터형으로 변환
# float(값/수식/변수) : 실수형 데이터형으로 변환
# str(값/수식/변수)  : 문자열 데이터형으로 변환
# bool(값/수식/변수)  : 논리 데이터형으로 변환

v1 = 123.5678  # 실수 flot
v2 = 987  # int
v3 = '234678'  # str
print(v1, type(v1), int(v1), str(v1), bool(v1))  # 123.5678 <class 'float'> 123 123.5678 True
print(v2, type(v2), float(v2), str(v2)[0], bool(v2))  # 987 <class 'int'> 987.0 9 True
print(v3, type(v3), float(v3), int(v3)+100, bool(v3))  # 234678 <class 'str'> 234678.0 234778 True




# 퀴즈 : 2개의 숫자값을 입력받은 후 사칙 연산을 수행하여라
# 입력문 + 형변환
'''
첫번째 숫자를 입력하세요... 10
두번째 숫자를 입력하세요... 20
---------
10 + 20 = ?
10 - 20 = ?
10 * 20 = ?
10 / 20 = ?
'''
fNum = int(input('첫번째 숫자를 입력하세요...'))
sNum = int(input('두번째 숫자를 입력하세요...'))
print('-------------')
print(fNum, '+', sNum,'=', fNum+sNum)
print(fNum, '-', sNum, '=', fNum-sNum)
print(fNum, '*', sNum, '=', fNum*sNum)
print(fNum, '/', sNum, '=', fNum/sNum)



# 연산자
# 산술연산자 : +, - , *, /, //(정수형 몫), %(나머지), **(제곱)
# 대입 연산자 : += , -= , *= , /=
# 비교(관계) 연산자 : ==, !=, >, <, >=, <=
# 논리 연산자 : and, or, not
# in, not in, ? 조건 연산자

n1,n2 = 100,3
print(n1,' 나누기', n2, ' 실수 몫', (n1/n2))
print(n1,' 나누기', n2, ' 정수 몫', (n1//n2))
print(n1,' 나누기', n2, ' 나머지는?', (n1%n2))
'''
100  나누기 3  실수 몫 33.333333333333336
100  나누기 3  정수 몫 33
100  나누기 3  나머지는? 1
'''


# 대입 연산자 : +=, -=, *=, /=
cnt = 1
print('------------')
print('1.. cnt = ', cnt)
cnt += 1  # cnt = cnt+1
print('2.. cnt = ', cnt)
cnt -= 5  # cnt = cnt-5
print('3.. cnt = ', cnt)
cnt *= -2  # cnt = cnt * -2
print('4.. cnt = ', cnt)
'''
1.. cnt =  1
2.. cnt =  2
3.. cnt =  -3
4.. cnt =  6
'''


# 비교(관계) 연산자 : ==, !=, >, <, >=, <=
n1 = 100
n2 = 50
print('\n\n')
print(n1 > n2, n1 == n2, n1 != n2)


# 논리 연산자
# 결과값이 True / False
# and, or, not
# 관계연산자를이용한수식1 논리 연산자 관계연산자를이용한수식2
# not(관계연산자를이용한수식)
# True and True => True
# True and False => False
# False or False => False
# True or False => True
# not(True) => False
# not(False) => True

n1 = 100
n2 = 50
print('\n\n')
print((n1 > n2) and (n1 == 100))  # T
print((n1 > n2) and (n1 != 100))  # F
print((n1 > n2) or (n1 == 100))  # T
print((n1 > n2) or (n2 == 100))  # F
print(not(n1==100))  # F



# is, is not 연산자
# 값이 같은지 비교한다.
# 결과값이 True/ False
pwd1 = '1234$$'
pwd2 = '1234$$'
print(pwd1 is pwd2)  # T
print(pwd1 is not pwd2)  # F



# in, not in 연산자
# 글자 in/not in 문자열
txt = '가나다라마바사'
print('$$$$$$$$$$$$')
print('가' in txt) # True
print('차' in txt) # False
print('차' not in txt) # True



# 문자열 연산자
# + 연결 : 문자열1 + 문자열2 => 문자열1문자열2
# * 반복 : 문자열*숫자 => 숫자만큼 문자열이 반복
lec1 = '파이썬'
lec2 = 'SQL'
print('='*30)
print(lec1 + lec2)
print(lec1 + ' / ' + lec2)



# 문자열 인덱싱
# 인덱싱이란?  문자열의 위치를 숫자로 표시
# 인덱싱의 첫 위치는 0
# 인덱싱의 마지막 위치는 -1
# 문자열변수[인덱스값]

# 문자열 전체길이는?
# len(문자열이나 문자열변수)

myText = '가나다라마바사아자차카타파하'
print('='*50)
print('myText= ',myText, len(myText))
print(myText[0],myText[1], myText[2])  # 가 나 다
print(myText[-1],myText[-3],myText[-5])  # 하 타 차



# 문자열 슬라이싱이란?
# 문자열의 일부를 잘라서 표시
# 문자열변수[start:end(인덱스는 end-1):step]
# 문자열변수[start:end(인덱스는 end-1)]
# 문자열변수[start:]
# 문자열변수[:end]
# start 부터 end-1 까지 step 수만큼 건너뛰기

myText = '가나다라마바사아자차카타파하'
print('\n'*3)
print(myText[0:5],myText[5:8],myText[5:],myText[:8])
# 가나다라마 바사아 바사아자차카타파하 가나다라마바사아
print(myText[-5:-2], myText[-2:-5])  # 차카타 / [-2:-5]는 안나옴
print(myText[-2:], myText[-5:-2],myText[-5:0])  # 파하 차카타 / [-5:0]은 안나옴
print(myText[::], myText[::2], myText[1::2])
# 가나다라마바사아자차카타파하 가다마사자카파 나라바아차타하
print('='*50)
# step 값이 음수이면 역순
print(myText[::], myText[::-2])  # 가나다라마바사아자차카타파하 하타차아바라나
print(myText[::], myText[::-1])  # 가나다라마바사아자차카타파하 하파타카차자아사바마라다나가



# 출력포맷 방식
# %를 이용한 포맷팅
# format()를 이용한 포맷팅
# f'를 이용한 포맷팅. 파이썬 3.6 이상에서 사용 가능

# %자료형
# %d(정수) / %s(문자열) / %전체자리수.소숫점자리이하숫자f(실수) / %o(8진수) / %x(16진수)
# print(' 문자열 %자료형 ' % 변수)
# print(' 문자열 %자료형1 %자료형2 ' % (변수1, 변수2))

# %전체자릿수.소수점 이하 자릿수 f
# %.소수점 이하 자릿수 f

num1 = 100
num2 = 7
user1 = '김과장'
user2 = '이대리'

# 100 나누기 7의 몫은 ? 이고 나머지는 ? 입니다.
print(num1, '나누기', num2, '의 몫은 ', (num1//num2), '이고 나머지는 ', (num1%num2), '입니다.')
print('%d 나누기 %d의 몫은 %d 이고 나머지는 %d 입니다.' %(num1, num2, (num1//num2), (num1%num2)))
print('10진수 %d  8진수 %o   16진수 %x' % (num1, num1, num1))
print('%s, %s 님 안녕하세요!!!' % (user1,user2))
print(' %d / %d = %.2f' % (num1,num2,(num1/num2)))
print(' %d / %d = %.5f' % (num1,num2,(num1/num2)))
print('%s, %s 님 안녕하세요! 영업률 상의 %d%%안에 진입하셨어요' % (user1,user2,10))



# format() 을 이용한 출력방식
# print(' 문자열1 {} {} 문자열2'.format(변수1, 변수2))
# print(' 문자열1 {인덱스1} {인덱스1} 문자열2'.format(변수1, 변수2))

num1 = 100
num2 = 7
user1 = '김과장'
user2 = '이대리'
print('\n\n {} 곱하기 {} ={}'.format(num1,num2,(num1*num2)))
print('{}님, {}님 안녕하세요! 영업률 상위 {}% 안에 진입하셨어요'.format(user1,user2,10))
print('영업률 상위 {2}% 안에 진입하셨어요. {1}님, {0}님 축하드려요!'.format(user1, user2, 10))



# format() 으로 소숫점 처리하기
# print("문자열 {위치인덱스:전체자릿수.소수점 이하 자릿수f}".format(값이나 변수))
pi = 3.14156748
print('pi 값은 {}'.format(pi)) # pi 값은 3.14156748
print('pi 값은 {0:10.3f}'.format(pi)) # pi 값은      3.142
print('pi 값은 {:.5f}'.format(pi)) # pi 값은 3.14157


# format 함수안에서 {} 표시하기
#  '{{ }}'.format()
print('{{ 오늘의 수익률은? }} => {} %'.format(14.3))


# format() + 변수 지정
print('value1 : {a} , value2 : {b}'.format(a='dog', b=20))


# f 문자열 포맷팅 : 3.6 이상 지원
# f' 문자열 {변수명이나 변수를이용한수식} '
# print(f' 문자열 ~~~ {변수/수식}')
num1 = 100
num2 = 7
print(f'\n\n {num1} 더하기 {num2} 는 {num1+num2}')


# f 포맷팅 소수점 처리
# f' 문자열 {변수명:전체자릿수.소숫점이하자릿수f} '
print(f'\n\n {num1} 나누기 {num2} 는 {num1/num2}')
print(f'\n\n {num1} 나누기 {num2} 는 {(num1/num2):.2f}')
print(f'\n\n {num1} 나누기 {num2} 는 {(num1/num2):20.5f}')


# 8진수, 16진수
# f' 문자열 {변수명:o} '
# f' 문자열 {변수명:x} '
print(f'\n\n 10진수 => {num1}     16진수 => {num1:x}      8진수 => {num1:o}')


# f' 문자열 공백, 대체문자여백 지정
# f' 문자열 {변수명:>숫자} : 왼쪽여백생성
# f' 문자열 {변수명:<숫자} : 오른쪽여백생성
# f' 문자열 {변수명:^숫자} : 좌우여백생성
# f' 문자열 {변수명:대체문자>숫자} : 왼쪽에 대체문자반복
# f' 문자열 {변수명:대체문자<숫자} : 오른쪽에 대체문자반복
# f' 문자열 {변수명:대체문자^숫자} : 좌우 대체문자 반복

msg = 'Hello World'
print(f'***{msg}***')
print(f'***{msg:>20}***')
print(f'***{msg:<20}***')
print(f'***{msg:^20}***')
print(f'***{msg:$^20}***')




















