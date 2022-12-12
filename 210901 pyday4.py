

# 리스트 for = 리스트 내포
# 리스트 안에 for 문이 내포된 형태
# 결과값으로 구성된 리스트가 생성된다.
# 리스트변수 = [결과값 for 명령문]

# 1~10으로 구성된 리스트 생성
# for 문 이용 방식
result = []
for i in range(1,11):
    result.append(i)
print(result)

# 리스트변수 = [결과값 for 명령문]
result2 = [i for i in range(1,11)]
print(result2)


# 3단의 결과값에서 1을 뺀 값으로 리스트 생성하기
# for 문을 이용한 리스트 생성 방식
result = []
for i in range(1,10):
    result.append(3*i-1)
print(result)

# 리스트 내포 방식
result2 = [3*i-1 for i in range(1,10)]
print(result2)


# 아래와 같은 형태로 리스트를 만들어라
# ['*', '**', '***' .... ,'**********']
# for 문
result = []
for i in range(1,11):
    result.append('*'*i)
print(result)

# 리스트 내포 방식
result2 = ['*'*i for i in range(1,11)]
print(result2)



## 퀴즈 ##
# for문과 리스트포 방식으로
# 아래와 같은 형태로 리스트를 만들어라
# ['column1', 'column2', 'column3' .... ,'column10']

# for문
result = []
for i in range(1,11):
    result.append('colum'+str(i))
print(result)

column = []
for i in range(1,11) :
    column.append((f'column{i}'))
print(column)


# 리스트 내포
result2 = ['colum'+str(i) for i in range(1,11)]
print(result2)

column = [f'column{i}' for i in range(1,11)]
print(column)



# 리스트 다중 for
# 리스트안에 이중 for문이 있는 형태
# 리스트변수 = [ 결과값 for 명령문 for 명령문 ]

# 구구단의 결과값을 리스트로 생성하여라.
# for 문을 이용한 리스트 생성 방식
result = []
for i in range(2,10):
    for j in range(1,10):
        result.append(i*j) # 2, 4, 6, ... 18, 3, 6 ... 27 ..... 81
print(result)

# 리스트 내포 방식
result2 = [i*j for i in range(2,10) for j in range(1,10)]
print(result2)


# 구구단을 리스트로 생성하여라.
# for 문을 이용한 리스트 생성 방식
result = []
for i in range(2,10):
    for j in range(1,10):
        result.append(f'{i}X{j}={i*j}')
        # result.append(str(i) + ' x ' + str(j) + ' = ' + str(i * j))
print(result)

# 리스트 내포 방식
result2 = [f'{i}X{j}={i*j}' for i in range(2,10) for j in range(1,10)]
print(result2)



## 퀴즈 ##
# 이중 리스트 내포 방식을 이용하여 다음과 같은 리스트를 생성하고 출력하여라.
# ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3',
#    '3 - 1', '3 - 2', '3 - 3', '4 - 1', '4 - 2', '4 - 3',
#    '5 - 1', '5 - 2', '5 - 3']
# for 문
result = []
for i in range(1,6):
    for j in range(1,4):
        # result.append(f'{i} - {j}')
        result.append(str(i) + ' - ' + str(j))
print(result)

# 리스트 내포
q = [f'{i} - {j}' for i in range(1,6) for j in range(1,4)]
print(q)



# 리스트 for + if
# 리스트안에 for 과 if 문이 있는 형태
# 리스트변수 = [ 결과값 for ~ if ~ ]

# 1~20 사이의 숫자중에서 3의 배수만 추가
# for문
result = []
for i in range(1,21):
    if i %3 == 0:
        result.append(i)
print(result)

# 리스트 내포
result2 = [i for i in range(1,21) if i %3 == 0]
print(result2)


# 9단의 결과값 중에서 짝수만 리스트에 추가하여라
# for 문
dan_9 = list(range(0,82,9))[1:]
print(dan_9)
result = []
for i in dan_9:
    if i %2 == 0:
        result.append(i)
print(result)

# 리스트 내포
result2 = [i for i in dan_9 if i %2 ==0]
print(result2)



## 퀴즈 ## 14
# 1~100 사이의 숫자 중 11의 배수이거나 7의 배수로 구성된 리스트를
# 리스트 내포 방식을 이용하여 출력하고 총 갯수도 함께 출력하여라.
'''
[7, 11, 14, 21, 22, 28, 33, 35, 42, 44, 49, 55, 56, 63, 66, 70, 77, 84, 88, 91, 98, 99]
 총 22 개
'''
# 일반 리스트 생성 후 for 문 이용
numList = []
for i in range(1, 101):
    if (i%11 == 0) or (i%7==0):
        numList.append(i)
print(numList)
print(f' 총 {len(numList)} 개')

# 리스트 내포1
q = [i for i in range(1,101) if i %11 == 0 or i %7 == 0]
print(q, f'\n 총 {len(q)}개')

# 리스트 내포방식2
q = [i for i in list(range(1,101)) if (i % 7 == 0) or (i % 11 == 0)]
print(q)
print(f' 총 {len(q)} 개')





#######################
### 사용자정의함수 정의 ###
#######################

# 함수정의 문법
'''
def 함수이름(인자1, 인자2...):
    명령문
    ...
    return 문
'''

# 호출시
# 함수명(값1, 값2 ...)



### 함수 정의 1 ###
# 인자도 없고 return문도 없음
# 함수 호출은?
# 함수()

# Hello world 를 5번 출력하는 함수 정의
def hello_world():
    for i in range(5):
        print(f' { i+1 } => Hello world')
    print('='*30)

# 함수 호출
hello_world()



### 함수 정의 2 ###
# 인자가 있다. return이 없다.
'''
def 함수명(인자1,인자2..):
    인자를 이용한 명령문
'''
# 호출
# 함수명(값1, 값2...)

# Hello future 를 n번 출력하는 함수 정의
# n울 인자로 정의
def hello_future(n):
    print(f' {n}번 출력')
    for i in range(n):
        print(f' { i+1 } => Hello future')
    print('='*30)

# 함수 호출
# hello_world2()  - TypeError남
hello_world2(2)
hello_world2(10)



# 메세지와 출력되는 횟수를 인자로 전달하여 출력하는 함수 정의
def hello_future2(n,msg):
    print(f' {n}번 출력')
    for i in range(n):
        print(f' { i+1 } => {msg}')
    print('='*30)

hello_future2(4,'nct dream')
# TypeError: 'str' object cannot be interpreted as an integer
# hello_world3('안녕하세요', 4)



### 함수 정의 3 ###
# 인자가 없다. return이 있다
# return 문은 함수를 탈출하는 용도로도 사용.
# return 문 아래의 명령은 실행이 되지 않는다.
'''
def 함수명():
    명령문...
    return 결과값/수식/명령문
'''
# 호출
# 함수명()


# 1~100 사이의 리스트 생성하고 튜플 형태로 변형해서 반환하는 함수 정의
def make_tuple():
    result1 = list(range(1,101))
    # result2 = tuple(result1)
    return result1  # return이 있으면 return 아래 명령은 실행X
    print('='*10)
    return result2

# 함수 호출
print(make_tuple())
print(f'함수 호출 결과 => {make_tuple()}')



# return 반환값이 여러개인 경우
# 인자 X, 다중 반환값
# 튜플 형태로 반환
def return_test():
    n1 = 100
    n2 = 45
    return n1+n2, n1-n2

print(f'다중 반환값이 있는 함수 호출 결과 => {return_test()} ')
print(f'두수의 합 => {return_test()[0]} ')
print(f'두수의 차 => {return_test()[1]} ')



### 함수 정의 4 ###
# 인자가 있다. return이 있다
# return 결과1, 결과2... => 튜플
'''
def 함수명(인자1, 인자2):
    명령문...
    return 변수/결과값/수식/명령문
'''
# 호출
# 함수명(값1, 값2....)


# 2개의 인자를 받아서 +,-,/,*,% 출력하기
'''
def cal(인자정의):
    ....

cal(2,3)

2 + 3 = ?
2 - 3 = ?
2 * 3 = ?
2 / 3 = ?
2 % 3 = ?
'''

def calc(n1, n2):
    return n1+n2 , n1-n2, n1*n2, n1//n2, n1%n2

print(calc(2,3))  # (5, -1, 6, 0, 2)
print(calc(12, 5)) # (17, 7, 60, 2, 2)


n1 = 12
n2 = 5
result = calc(n1, n2)
print(f'{n1} + {n2} = {result[0]}')
print(f'{n1} - {n2} = {result[1]}')
print(f'{n1} X {n2} = {result[2]}')
print(f'{n1} // {n2} = {result[3]}')
print(f'{n1} % {n2} = {result[4]}')



### 함수 정의 5 ###
# 인자의 초기값 설정
# 모든 인자의 초기값이 있는 경우
# 일부 인자 초기값이 있는 경우
'''
def 함수명(인자1=값1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문
    
def 함수명(인자1, 인자2=값2):
    인자에 관련된 명령문...
    return 값/변수/수식/명령문    
'''
# 호출
# 함수명()
# 함수명(값1)
# 함수명(값1, 값2)


# 두수의 합 결과 출력
# 인자에 모두 초기값이 있다.
# return X
def add_n(n1=0, n2=0):
    print('='*50)
    print(f'{n1} + {n2} = {n1+n2}')

add_n() # 0 + 0 = 0
add_n(12) # 12 + 0 = 12
add_n(12, 24) # 12 + 24 = 36


# 세 수의 합 결과 출력
# 일부 인자에만 초기값이 있다
# return X
def add_n2(n1, n2, n3=100):
    print('='*50)
    print(f'{n1} + {n2} + {n3} = {n1+n2+n3}')

add_n2()  # TypeError: add_n2() missing 2 required positional arguments: 'n1' and 'n2'
add_n2(10)  # TypeError: add_n2() missing 1 required positional argument: 'n2'
add_n2(10,20)  #10 + 20 + 100 = 130
add_n2(10,20,30)  # 10 + 20 + 30 = 60

'''  # 초기값이 있는 경우 맨 뒤로 이동시켜야 함. - SyntaxError
def add_n3(n1, n2=100, n3): 
    print('='*50)
    print(f'{n1} + {n2} + {n3} = {n1+n2+n3}')
add_n3()
'''




## 퀴즈 1 ##
# 함수를 호출하면 각각의
# 구성 아이템이 다음과 같이 출력되도록 함수를 정의하여라
'''
# printList(['라면', '빙수'])

   오늘의 메뉴
1  :  라면
2  :  빙수

# printList(['모밀', '탕수육', '육계장'])
   오늘의 메뉴
1  :  모밀
2  :  탕수육
3  :  육계장
'''
def printList(foodList):
    print('\n\n   오늘의 메뉴   ')
    # for i in range(0, len(foodList)):
    #     print(i+1, ' : ', foodList[i])
    cnt = 1
    for item in foodList:
        print(cnt, ' : ' ,item)
        cnt += 1

printList(['모밀', '탕수육', '육계장'])
printList(['라면', '빙수'])



## 퀴즈 2 ##
# 아래의 예제를 참조하여 함수를 호출하면 메세지가 출력되도록
# 함수를 정의하여라
# 이때 함수 인자는 3개로 구성하며 마지막 man 만 True 형태로
# 초기값을 지정한다.
'''
# 함수 정의 
def say_myself(name, old, man=True):
    ?

# 함수 호출 1 
say_myself('김철수', 20)

# 결과값 1
나의 이름은 김철수 입니다.
나이는 20살입니다.
남자입니다.
--------------------------------------------------
# 함수 호출 2
say_myself('백설공주', 15, False)

# 결과값 2
나의 이름은 백설공주 입니다.
나이는 15살입니다.
여자입니다.

'''

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


say_myself('김철수', 20)
say_myself('백설공주', 15, False)



## 퀴즈 3 ##
# n1~n2까지의 모든합과 모든곱을 반환한다.
# 인자 O , return 값은 2개

# 함수 호출
# sum_multy(1,100)
# 결과
# 모든 합은 ... ?
# 모든 곱은 ... ?

def sum_multy(n1,n2):
    result1 = 0
    result2 = 1
    for i in range(n1, n2+1):
        result1 += i
        result2 *= i
    return result1, result2

print(f' 모든 합은 ... {sum_multy(1, 100)[0]}')
print(f' 모든 곱은 ... {sum_multy(1, 100)[1]}')


print(f' 모든 합은 ... {sum_multy(5, 10)[0]}')
print(f' 모든 곱은 ... {sum_multy(5, 10)[1]}')





### 함수 정의 6 ###
# 가변인자인 경우 : 인자의 갯수가 정해지지 않는 경우
# *args => arguments
# 인자가 args 튜플로 반환
'''
def 함수명(*args):
    args에 관련된 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(값1)
# 함수명(값1, 값2)
# 함수명(값1, 값2, 값3 ...)


# 모든 인자의 합을 출력하여라
# 가변인자 함수 정의
def add_all(*args):
    print(args)
    print(f' 모든 합은? {sum(args)}')

add_all()  # ()
add_all(10)  # (10,)
add_all(10, 20, 30)  # (10, 20, 30)
add_all(10, 20, 30, 40, 50)  # (10, 20, 30, 40, 50)



# 아래와 같은 함수를 호출하면 학생이름이 출력되도록 하여라
# 학생수가 없다면 수강생이 없습니다. 메세지 출력
# studentName('고길동')
# studentName('최길동', '박길동', '고길동',)
# studentName('김길동', '왕길동', '최길동', '박길동', '고길동',)
# studentName()

def studentName(*args):
    print('\n'*2)
    if args:
        for i in range(len(args)):
            print(f' 수강번호 { i+ 1} => {args[i]}')
    else:
        print('수강생이 없습니다.')

studentName('고길동')
studentName('최길동', '박길동', '고길동')
studentName('김길동', '왕길동', '최길동', '박길동', '고길동')
studentName()




### 함수 정의 7 ###
# 일반인자랑 가변인자랑 함께 있는 경우
# 주의 사항: 일반 인자는 앞쪽으로 배치. 가변 인자 *args는 뒷편에 배치
'''
def 함수명(인자, *args):
    인자와 args를 이용한 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(인자값, 가변값1)
# 함수명(인자값, 가변값1, 가변값2...)

'''
# 계산기호인자 값에 따라서 뒤의 가변인자값을 계산하여라

# 함수 정의
def calChoice(계산기호인자, *args) :
    명령문

# 함수 호출
# calChoice('*', 20,30)
# 계산결과 = 곱 : 600
# calChoice('+', 20,30,50)
# 계산결과 = 합 : 100

'''

def calChoice(symbol, *args):
    if len(args) == 0:
        print('계산을 완료할 수 없습니다.')
    elif symbol == '+':
        print(f' 계산결과 = 합 : {sum(args)} ')
    elif symbol == '*':
        temp = 1
        for item in args:
            temp *= item
        print(f' 계산결과 = 곱 : {temp} ')
    else:
        print('계산을 완료할 수 없습니다.')

calChoice('*', 20,30)
calChoice('+', 20,30,40)
calChoice('-', 20,30)
calChoice('+')
# calChoice() - TypeError




### 함수 정의 8 ###
# 딕셔너리 가변인자 **kwargs
# 가변인자는 키=값
# 결과 데이터형이 딕셔너리
# kwargs = Keyword Arguments

'''
def 함수명(**kwargs):
    kwargs를 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(키1=값1)
# 함수명(키1=값1, 키2=값3 ...)
# {키1:값1, 키2:값2 .... } => kwargs
# 키는 문자열로 지정

def make_dict(**kwargs):
    print(kwargs, type(kwargs))

make_dict(a=100,b=200)  # {'a': 100, 'b': 200} <class 'dict'>
make_dict()  # {} <class 'dict'>



# 나이, 이름, 성별 형태로 구성된 딕셔너리로 출력
'''
makePerson(age=33, name='Jackson', gender='M')
makePerson(age=22, name='Maria', gender='F')
'''
def makePerson(**kwargs):
    for key in kwargs:
        print(f' { key } => { kwargs[key] }')

makePerson(age=33, name='Jackson', gender='M')
makePerson(age=22, name='Maria', gender='F')



### 함수 정의 9 ###
# 일반인자 + 딕셔너리 가변인자 **kwargs
'''
def 함수명(인자, **kwargs):
    kwargs를 명령문...
    return 값/변수/수식/명령문
'''
# 호출
# 함수명(인자값, 키1=값1)
# 함수명(인자값, 키1=값1, 키2=값2 ...)
def makePerson2(cat, **kwargs):
    print('분류 => ', cat)
    for key in kwargs:
        print(f' { key } => { kwargs[key] }')
    print('='*50)

makePerson2('수강생', name='홍길동', year='A')
makePerson2('강사', name='김영희', gender='Female')




### 람다 함수 ###
# def 로 정의하지 않는다.
# 한줄로 정의한다.
'''
# 람다함수 정의
함수변수 = lambda 인자:명령

# 람다함수 호출
함수변수(인자)
'''

# 인자 1개인 형태
# 수의 제곱값을 반환

# 일반함수
def power(n):
    return f'{n}의 제곱값은 {n**2}'

print(power(5))

# 람다 함수
power2 = lambda n:f'{n}의 제곱값은 {n**2}'
print(power2(5))


# 인자 2개인 형태
# 두수의 합을 반환

# 일반 함수
def add(x, y):
    return f'{x} + {y} = {x+y}'

print(add(23, 66)) # 23 + 66 = 89

# 람다함수
add2 = lambda x,y : f'{x} + {y} = {x+y}'
print(add2(23,66))





# 함수의 변수 영역
# 스코프(Scope)
# 전역변수(문서 전체의 공통변수) ?
# 지역변수(함수내부에만 유효한 변수)?

# 함수내에서 지역변수를 전역변수로 정의
# global 변수명

def scope_test(n):
    global y  # 전역변수
    # 지역변수
    x = 100
    y = n
    print(f' 함수 안의 x = {x}')  # 100
    print(f' 함수 안의 y = {y}')  # n


# 함수 호출
scope_test(300)
'''
 함수안의 x = 100
 함수안의 y = 300
'''

# 전역변수(scope_test함수) 내의 변수와 상관 없이 출력 / 전역변수 설정시 전역변수 설정 값으로 출력. 영향 받음.
x = 1
y = 1
print(f' 함수 안의 x = {x}')
print(f' 함수 안의 y = {y}')




### 함수의 종류 ###

# 사용자정의함수
# 빌트인 함수 => 파이썬에서 제공하는 함수

# import 명령의 유무
# 내장함수 : 별도의 import 명령이 필요없다
#           함수(옵션) ex) abs(), enumerate()...
# 외장함수
# : 별도의 import 명령이 필요
#           모듈명.함수(옵션) ex) datetime 함수
# 파이썬에서 제공하는 외장함수
# pip install 모듈명  별도의 설치가 필요한 외장함수
# conda install 모듈명 별도의 설치가 필요한 외장함수



### datetime 모듈 이용하기 ###
# 시간변수 = datetime.datetime.now()
# 시간변수.year
# 시간변수.month
# 시간변수.day
# 시간변수.hour


# 시간과 관련된 모듈 임포트
import datetime

# 시계열 변수 설정 - 현재 시간을 기준으로 년,월,일,시,분,초 변수 생성
now = datetime.datetime.now()
print(now, type(now))
# 2021-09-01 16:32:59.414326 <class 'datetime.datetime'>
print(now.year, type(now.year))  # 2021 <class 'int'>
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)



## 퀴즈1 : if문과 datetime 모듈 이용
# 현재 시간을 아래와 같이 출력한다.
# 현재 시간은 오후 3시 () 분입니다.

def print_time():
    # 시간 변수 설정
    now = datetime.datetime.now()
    if now.hour >= 12:
        print(f' 현재 시간은 오후 {now.hour-12}시 {now.minute}분입니다.')
    else:
        print(f' 현재 시간은 오전 {now.hour}시 {now.minute}분입니다.')

print_time()




## 퀴즈2 : if문과 datetime 모듈 이용
# 달을 추출 now.month
# 달에 따라 봄, 여름, 가을 ,겨울 메세지 출력
# 12, 1,2 : 겨울
# 3~5 : 봄
# 6~8 : 여름
# 9~11 : 가을
# 출력은 아래와 같이.
# 12월은 겨울입니다.

def print_W():
    now = datetime.datetime.now()
    if now.month in (12,1,2):
        print(f' {now.month}월은 겨울입니다.')
    elif 3 <= now.month <= 5:
        print(f' {now.month}월은 봄입니다.')
    elif 6 <= now.month <= 8:
        print(f' {now.month}월은 여름입니다.')
    elif 9 <= now.month <= 11:
    print(f' {now.month}월은 가을입니다.')

print_W()



# 요일 찍기
# 요일은 (월요일)0 ~ 6(일요일)
today = datetime.datetime.today().weekday()
today_list = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(today,type(today))  # 2 <class 'int'>
print(f' 오늘은 {today_list[today]} 입니다.')




### time 모듈 이용하기 ###

# time 모듈 임포트
import time

# time.time()
# : 현재 시간을 실수 형태로 리턴한다.

# time.localtime(time.time())
# : time.time()의 값을 년도, 월, 일, 시, 분, 초로 변경
# : 튜플 자료 구조 형태

print(time.time(), type(time.time())) # 1630484542.3691828 <class 'float'>
now = time.localtime(time.time())
print(now)
# time.struct_time(tm_year=2021, tm_mon=9, tm_mday=1, tm_hour=17, tm_min=23, tm_sec=27, tm_wday=2, tm_yday=244, tm_isdst=0)
print(type(now)) # <class 'time.struct_time'>


# 리스트로 변형
now_list = list(time.localtime(time.time()))
print(now_list)  # [2021, 9, 1, 17, 26, 41, 2, 244, 0]


## 퀴즈 : 리스트화 한 후 아래의 출력 형태로 출력하여라
# now_list = list(time.localtime(time.time()))
# resultFormat = ['년', '월', '일', '시', '분']

'''
???? 년 / ? 월 / ? 일 / ?요일  / ? 시 / ? 분 / 
'''

now_list = list(time.localtime(time.time()))
resultFormat = ['년', '월', '일', '시', '분']
# 방 1
print(str(now_list[0])+resultFormat[0], str(now_list[1])+resultFormat[1], str(now_list[2])+resultFormat[2], str(now_list[3])+resultFormat[3],str(now_list[4])+resultFormat[4])

# 방 2
for i in range(len(resultFormat)) :
    print(f' {now_list[i]}{resultFormat[i]}', end = '/')

# 방 3
now_list = list(time.localtime(time.time()))
now_format = ['년', '월', '일', '시', '분']
today_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
for i in range(5):
    print(now_list[i], now_format[i] , end=' ')

print(today_list[now_list[6]])

# 방 4
now = time.localtime(time.time())
print(now)
today_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
# 시계열변수.속성
print(f'{now.tm_year} 년 / {now.tm_mon} 월 / {now.tm_mday} 일 / {today_list[now.tm_wday]} /'
      f' {now.tm_hour-12} 시 / {now.tm_min} 분 /' )










# 모듈 설치하기1(예) pandas, numpy)
# [File]-[Settings] 메뉴 명령 실행
# [Python Interpreter] 화면에서 [+] 클릭
# [Available Package] 대화상자에서 설치하고자 하는 모듈명 입력 후
# 검색되면 [Install Package] 클릭
# 설치 완료되면 (하단 메세지 확인) 창을 닫고 설치 목록 확인

# 모듈 설치하기2
# 1) 화면 하단에 Terminal 탭 클릭
# 2) pip list 명령 실행 후
#  pandas, numpy 가 있는지 확인
# 3) 명령 실행
#  pip install numpy
#  pip install pandas
# 4) 설치 확인
# pip list













