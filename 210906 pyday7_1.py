
# 함수 < 클래스 < 모듈(파일) < 패키지 < 라이브러리
# 모듈 => 파일
# 패키지 => 폴더

# 패키지(Package)
# 모듈파일을 별도의 폴더에 저장하여 쓰는 기능
# 폴더는 패키지명으로 이용
# __init__.py => 이폴더는 패키지 용으로 정의
# 폴더(패키지) 안에 삽입

''' 모듈
import hello
hello.print_msg()
'''




# 파이참에서 패키지용도의 폴더만들기
# [Project] 창에서 작업 폴더(pythonclass) 마우스우측버튼
# [New]-[python package]
# 패키지폴더가 생성되고 자동으로 __init__.py 파일 생성
# __init__.py
# : 패키지폴더임을 알려주는 파일

# Step1)
# a 폴더 => 패키지로 정의

# Step2)
# a 폴더 안에 test.py 파일 생성

# Step3)
# test.py 파일안에 message() 함수 정의하고 Save

# Step4)
# pyday7.py에서 a 폴더 안의 test.py 파일의 message() 호출

# a 패키지안의 message 모듈 임포트
# 첫번째 방법
# import 패키지명.모듈
# 패키지명.모듈.함수(인자값)로 호출
import a.test
a.test.message('월요일화이팅','하연')
a.test.calculator(10,6)

# 두번째 방법
# import 패키지명.모듈 as 별칭
# 별칭.함수(인자값)로 호출
import a.test as t
t.message('월요일화이팅','하연')
t.calculator(5,11)

# 세번째 방법
# from 패키지명.모듈 import 함수1, 함수2
# 함수(인자값)로 호출
# from a.test import message
# from a.test import calculator

from a.test import message, calculator

# from a.test import *

# from a.test import calculator
# message('Hello ... ', '최길동')
# calculator(3, 4)

import a.test
a.test.calculator(3,4)  # import 랑 동시에 실행해야 오류 안남.



## 퀴즈
# 구구단를 특정 파일에 함수로 정의하고 패키지명을 생성한 후
# 파일에서 모듈로 임포트하여
# 함수를 호출하도록 하여라.

# Step0. g 패키지 폴더 생성
# Step1. gugu.py로 모듈파일 생성후
#        특정 n 단과 구구단 전체를 출력하는 함수 정의
# Step2. 별도의 파이썬 파일에서 패키지안의 모듈을 임포트 한 후
#        모듈의 함수가 실행되는지 확인

import g.gugu
g.gugu.gugudanPrint1(5)
g.gugu.gugudanPrint2()




# 퀴즈 10
# Step1.
# lotto.py로 모듈파일 생성후 로또 번호와 관련된 함수 정의
#  로또 번호를 n개 생성하는 함수 정의
#  로또 번호를 생성하고 파일로 저장하는 함수 정의
#  로또 번호는 1~46 범위에서 6개 중복없이 생성되도록 한다. (random 이용)

# Step2. 별도의 파이썬 파일에서 import lotto로 모듈을 임포트 한 후
# 모듈의 함수가 실행되는지 확인

import lotto
lotto.lottoNum(5)
lotto.lottoNumSave()




### 오류? ###
# 오류의 종류
# => 에러코드 + 에러메시지
# NameError: 함수이름, 변수, 리스트 이름등이 잘못된 경우
# IndexError :  튜플,리스트의 잘못된 인덱스 접근
# ZeroDivisionError : 0으로 나눈 경우
# FileNotFoundError : 잘못된 파일 경로
# TypeError
# ValueError
# SyntaxError 제외 => 예외처리 try: ~ Except 구문에서 제외


# 예시
# ZeroDivisionError: division by zero
# division by zero => e
# print(12/0)

# NameError: name 'a' is not defined
# print(a)

# ValueError:
# invalid literal for int() with base 10: '사십오'
# x = '사십오'
# print(int(x) + 100)




### 예외처리(Exception) 란? ###
# 오류가 발생을 하면
# 메세지를 출력하거나  오류를 무시하는 기능

# try..except 명령
# try..except..else 명령
# try..except..else..finally 명령
# raise Exception : 사용자정의 에러
#  ex) 금칙어, 특별한 값 지정. 데이타 유효성


# ---------------------------------
# 에러처리 문법 1
# ## try..except 명령1
# - 에러코드를 알고있어야 한다.
# try:
#   명령어
# except 에러코드 as e:
#   에러처리명령

# x,y =10,2
x,y =10,0
try:
    ans = x/y
    print(f'{x} 나누기 {y} 는 {x/y}')
except ZeroDivisionError as e:
    print(f'0으로 나눌 수 없습니다. => {e}' )
print('테스트 종료')

myList = list(range(1,11))
try:
    print(myList[0])
    print(myList[1])

except IndexError as e:
    print(f'에러발생 => {e}')
print('테스트 종료')


# 2가지 이상의 예외처리문이 있는 경우 =>
try:
    print(10/0)
    print(myList[20])
    print(f'{x} 나누기 {y} 는 {x/y}')
except ZeroDivisionError as e:
    print(f'0으로 나눌 수 없습니다. => {e}')
except IndexError as e:
    print(f'에러발생 => {e}')
print('테스트 종료')



# ## try..except 명령2
# 모든 예외의 에러 메시지를 출력할 때는 Exception 키워드
# 에러코드를 몰라도 된다. => Exception
# try:
#     명령
# except Exception as e:
#     print(e)

print('='*50)
myList = list(range(1,11))
try:
    print(45/3)
    print(myList[20])
    print(10/0)
except Exception as e:
    print(f'에러 발생 , 에러메세지 => {e}')
print('테스트 종료\n\n')


print('='*50)
myList = list(range(1,11))
try:
    print(45/3)
    print(myList[5])
    print(10/0)
except Exception as e:
    print(f'에러 발생 , 에러메세지 => {e}')
print('테스트 종료\n\n')


# try..except 명령3
# 에러 메세지를 사용할 수 없다.
# try:
#   명령어
# except:
#   에러처리명령`
print('='*50)
myList = list(range(1,11))
try:
    print(45/3)
    print(myList[5])
    print(10/0)
except:
    print(f'에러 발생 ')
print('테스트 종료\n\n')


# 명령 4
# try.. except [에러코드/Exception] else ...
# try:
#   명령어
# except [에러코드/Exception as e]:
#   e 출력 ,에러처리명령
# else:
#   에러가 발생하기 않은 경우 명령어

# 파일이 없다면 에러메시지 발생
# 파일이 있다면 파일을 읽은 후 첫행만 출력

try:
    # f = open('data/a.txt', 'r')
    f = open('data/yesterday.txt', 'r')
except Exception as e:
    print(f'에러발생 => {e}')
else:
    data = f.readline()
    print(data)
    f.close()


# 명령 5
# try ... except [에러코드/Exception] else ... finally ...
# try:
#   명령어1
# except [에러코드/Exception as e]:
#   e 출력 ,에러처리명령
# else:
#   에러가 발생하지 않을 경우 명령어
# finally:
#   명령어2
print('='*50)
try:
    # f = open('data/a.txt', 'r')
    f = open('data/Yesterday.txt', 'r')
except Exception as e:
    print(f'에러발생 => {e}')
else:
    data = f.readline()
    print(data)
    f.close()
finally:
    print('테스트 종료 :try ... except ... else ... finally ')



## 퀴즈: ValueError
# 2개의 숫자글자를 입력받아서 더한다.
# 입력된 글자가 숫자글자가 아니라면 에러 메세지 출력
# 입력된 글자가 숫자글자라면  더한후 출력한다.
try :
    num1 = int(input('첫번째 숫자를 입력해주세요... '))
    num2 = int(input('두번째 숫자를 입력해주세요... '))
except ValueError as e:
    print('숫자가 아닙니다.')
else:
    print(f'{num1} + {num2} = {num1+num2}')
finally:
    print('퀴즈 종료')





### 에러처리 문법 4 : 오류 회피
# 에러 무시 : pass 키워드 사용

# try:
#   명령어1
# except:
#   pass
# else :
#   명령어2
# finally:
#   명령어3


# 자료형이 섞여있는 경우 => 리스트의 모든 합
myList = ['사과', True, 123, 456, '포도', False, 45.125]
# TypeError:
# unsupported operand type(s) for +: 'int' and 'str'
# print(sum(myList))

sum = 0
for i in myList:
    # print(i)
    try:
        temp = int(i)
    except:
        pass
    else:
        sum += temp
print(f'{myList}의 모든 합은? {sum}')



### 사용자정의 에러
# 에러만들기 : raise 문 이용
# 일부러 에러 발생
# if 조건식:
#   raise Exception(오류 메세지)

# 입력값이 0이면 오류 메세지 출력
n = input('입력 데이터...').strip()
if n == '0':
    raise Exception('0은 입력할 수 없다...')
else:
    print('hello world'*int(n))


# 변수값이 음수이면 에러발생

try:
    x = int(input('숫자를 입력하세요'))
except:
    # 숫자가 아닌 경우 예외처리
    print('자료형을 변경할 수 없습니다.')
else:
    if x<=0:
        raise Exception('양수이어야 합니다.')
    else:
        print(x)



## 퀴즈
# 학생의 학년을 저장하는 변수 classYear값은
# 1학년, 2학년, 3학년, 4학년 이어야한다.
# 나머지 값은  raise Exception 을
# 이용하여 오류를 발생시켜라

# 결과>>
# classYear = '1학년'
# classYear = '8학년'   # Exception: 학년 정보가 올바르지 않습니다.
# classYear = '삼학년'   # Exception: 학년 정보가 올바르지 않습니다.
# classYear = '3학생'    # Exception: 학년 정보가 올바르지 않습니다.
# classYear = '356'      # Exception: 학년 정보가 올바르지 않습니다.
# print('학년 정보 - ', classYear)

# 방1
try:
    classYear = int(input('학년을 입력하세요...'))
except:
    print('Exception: 학년 정보가 올바르지 않습니다.')
else:
    if classYear > 4:
        raise Exception('Exception: 학년 정보가 올바르지 않습니다.')
    else:
        print('학년정보 - ', classYear, '학년')

# 방2
classlist = ['1학년', '2학년', '3학년', '4학년']

classYear = '5학년'
if classYear not in classlist :
    raise Exception('학년 정보가 올바르지 않습니다.')
print('학년 정보 - ', classYear)



























