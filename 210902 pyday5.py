

# 시계열 데이터와 관련된 모듈 임포트
# import 모듈명
import time, datetime, random

# 현재 시간 출력
now = datetime.datetime.now()
print(now, type(now))  # 2021-09-02 10:24:15.308817 <class 'datetime.datetime'>
print(now.month, '월', now.day, '일')  # 9 월 2 일

now2 = time.localtime(time.time())
print(now2, type(now2))
'''
time.struct_time(tm_year=2021, tm_mon=9, tm_mday=2, tm_hour=10, tm_min=26, tm_sec=26, tm_wday=3, tm_yday=245, tm_isdst=0) <class 'time.struct_time'>
'''
print(now2.tm_mon,'월', now2.tm_mday,'일')  # 9 월 2 일




# 여러가지 출력 포맷 이용하기
# time.strftime('포맷코드1 포맷코드2', time.localtime(time.time()))
# 출력할 형식 포맷코드
# %a / %A  : 요일
# %b / %B  :  달
# %c : 날짜와 시간
# %d : 날(day)
# %H :24시간 기준의 시간
# %I :12시간 기준의 시간
# %j :1년중 누적 날짜 표시
# %x : 지역 기반 날짜 출력
# %X : 지역 기반 시간 출력
# %w : 숫자로된 요일 출력. 0은 일요일
# %Y : 년도 출력
# %Z : 시간대 출력
# %p : AM/PM


print(time.strftime('%c', time.localtime(time.time())))
today = time.strftime('%c',time.localtime(time.time()))
print(type(today))
print('요일은?', today[:3])

print(time.strftime('%p %I', time.localtime(time.time()))) # AM 10



## 퀴즈
# time 모듈에서 제공하는 함수를 이용하여 아래와 같이 오늘 날짜를 기준으로
# 출력되도록 하여라.
# tm_yday, time.strftime() 에서 %j  (str format time)
'''
오늘은 ? 월  ? 입니다.
1년을 기준으로 ? 번째 날이며 올해는 ? 일 남았습니다. 
'''

today = time.localtime(time.time())
days = time.strftime('%j',time.localtime(time.time()))
print(tod1ay)
print(f'오늘은 {today.tm_mon}월 {today.tm_mday}일 입니다.')
print(f'1년을 기준으로 {today.tm_yday}번째 날이며 올해는 {365-today.tm_yday}일 남았습니다.')
print(f'1년을 기준으로 {days}번째 날이며 올해는 {365-int(days)}일 남았습니다.')



# 문자열 날짜 데이터 => 시계열 데이터
# 년도-월-일 => 시계열 데이터
# time.strptime('년도-월-일', 포맷 '%y-%m-%d')
d_day1 = '2020-12-31'
d_day2 = time.strptime(d_day1, '%Y-%m-%d')
print('='*30)
print(d_day1, type(d_day1)) # 2020-12-31 <class 'str'>
print(d_day2, type(d_day2))
'''
time.struct_time(tm_year=2020, tm_mon=12, tm_mday=31, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=366, tm_isdst=-1) 
<class 'time.struct_time'>
'''



## 퀴즈 6 ##
# time 모듈에서 제공하는 함수를 이용하여
# 특정 날짜에 대한 요일을 출력하여라.

# 나는 무슨 요일에 태어났을까? ..... ? 요일

# 방법 1
b_day1 = '1997-04-11'
b_day2 = time.strptime(b_day1, '%Y-%m-%d')
week = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
print(f'나는 무슨 요일에 태어났을까? ..... {week[b_day2.tm_wday]}')

# 방법 2
def printWeekday(d_day):
    tm = time.strptime(d_day, '%Y-%m-%d')
    print(tm, type(tm))
    print(time.strftime('%A', tm)) # Thursday
    day_list = ['월', '화', '수', '목', '금', '토', '일']
    return day_list[tm.tm_mday]

print(f'나는 무슨 요일에 태어났을까? ..... {printWeekday("2009-12-03")}요일')




### enumerate(리스트/튜플/문자열 , 인덱스숫자 ) ###
# 인덱스숫자로 구성된 리스트/튜플/문자열
# => enumerate 객체 생성
# => for .. in 하나씩아이템 출력 가능
# => 각각 튜플아이템으로 생성 (인덱스, 값)
# dict(enumerate(리스트/튜플/문자열)


word_list = ['파이썬', 'MySQL', 'HTML']
word_e = enumerate(word_list, 11)
print('\n'*2,word_list)
print(word_e, type(word_e))
for i in word_e:
    print(i)

# 리스트안에 튜플 형태로 생성
word_e = enumerate(word_list, 1)
word_tuple_list = []
for i in word_e:
    word_tuple_list.append(i)
print(word_tuple_list)


# 딕셔너리 구조로 변경
word_e = enumerate(word_list)
word_dict = dict(word_e)
print(word_dict)  # {0: '파이썬', 1: 'MySQL', 2: 'HTML'}


# 튜플 변수로 출력
word_e = enumerate(word_list, 101)
for i,j in word_e:
    print(f'{i} => {j}')
'''
101 => 파이썬
102 => MySQL
103 => HTML
'''



### eval(문자열계산식) ###
exp = '12+67-89'
print(eval(exp)) # -10
print(type(eval(exp))) # <class 'int'>

# 입력받은 수식을 계산하여라
result = input('수식을 입력하세요? ... ')
print(result, ' = ', eval(result))




# 내장함수 : 아스키코드와 관련된 함수
# chr() , ord()
# chr(숫자) => 아스키코드값에 해당하는 문자나 숫자
# 문자의 아스키 코드 값을 돌려주는 함수
# 0에서 127 사이의 숫자를 각각 하나의 문자 또는 기호에
# ord(문자) => 아스키코드값 chr()과 반대되는 함수
# 대응시켜 놓은 코드표
# https://ko.wikipedia.org/wiki/ASCII

print(chr(65), ord('A'))  # A 65
print(ord('Z'))  # 90


## 퀴즈 ##
# 알파벳 대문자로 구성된 리스트를 생성하여라
# ['A', 'B', .... 'Z']
alpha_upper = []
for i in range(65, 91):
    alpha_upper.append(chr(i))
print(alpha_upper)

# 알파벳 소문자로 구성된 리스트를 생성하여라
# ['a', 'b', .... 'z']
alpha_lower = []
for i in range(ord('a'), ord('z')+1):
    alpha_lower.append(chr(i))
print(alpha_lower)

# 리스트 for 역순 z~a
alpha_lower2 = [chr(i) for i in range(ord('z'), ord('a')-1, -1)]
print(alpha_lower2)




### 유효성 검사 ###
# 데이터(숫자, 문자...)가 조건에 맞는지 검사하는 기능
# 문자열변수.isalpha()
# : 모두 문자(알파벳,한글..)인가? 숫자문자제외 , True/Fasle
# 문자열변수.isdigit() , 문자열변수.isnumeric()
# : 모두 숫자문자인가?  , True/Fasle
# 문자열변수.isalnum() : 문자열과 숫자로만 구성되어 있는가?
# islower(), isupper() : 대문자/ 소문자 검사
# isdecimal() : 모두 10진수인가?
str1 = 'fkfkfk'
str2 = '12345'
str3 = '1fdkjfsl2345'
str4 = 'BANANA'
str5 = '#&^=+'
print(str1.isdigit())  # F
print(str2.isdigit())  # T
print(str3.isdigit())  # F
print(str4.isupper())  # T
print(str5.isalnum())  # F



## 퀴즈 : 문자열에서 숫자와 숫자가아닌문자의 갯수를 출력하여라
# testWord = 'Python1234Java4774'
'''
결과 >>
숫자 갯수 : ?
문자 갯수 : ?
'''
testWord = 'Python1234Java4774'
count = 0
for i in testWord:
    if i.isdigit():
        count += 1
    # print(i)
print(f' 숫자개수 : {count}')
print(f' 문자개수 : {len(testWord)-count}')



## 퀴즈 : 입력 데이타를 이용하여 숫자로 구성된 리스트를 생성하여라 (길이는 3)
'''
입력 데이터 >> ??
입력 데이터 >> ??
입력 데이터 >> ??
..
입력 데이터 >> ??
........
결과 => [?, ?, ?]
'''
# 빈 리스트를 생성한다.
# 입력문이 실행된다.
# 입력값이 숫자이면 리스트에 추가한다.
# 입력값이 숫자가 아니면 다시 입력문이 실행된다.
# 리스트의 전체길이가 3이면 입력을 종료한다.
# 리스트를 출력한다.

def datata():
    dataList = []
    while len(dataList) < 3:
        data = input('입력 데이터 >> ')
        if data.isdigit():
            dataList.append(data)
    print(dataList)

datata()




### zip(리스트1, 리스트2 .. )
# zip 객체로 리턴 => for...in zip 문 이용해서 아이템 확인
# : 리스트의 각 아이템요소를 튜플화 구조로 묶어준다. => 튜플로 구성된 리스트
# list(zip 객체): [(아이템1,아이템2) ...]


p1_name = ['길동', '동미', '미영', '영철']
p1_gender= ['남','여','여','남']
p1_zip = zip(p1_name,p1_gender)
print(p1_zip, type(p1_zip))  # <zip object at 0x000001CC65D3B700> <class 'zip'>
for i in p1_zip:
    print(i)

p1_zip = zip(p1_name,p1_gender)
for i, j in p1_zip:
    print(i, ' - ', j)



# 2개의 리스트 => zip 객체 => 튜플 구조로 삽입된 리스트
p1_zip_list = list(zip(p1_name, p1_gender))
print('='*30)
print(p1_zip_list)


# 2개의 리스트 => zip 객체 => 딕셔너리
p1_zip_dict = dict(zip(p1_name, p1_gender))
print('='*30)
print(p1_zip_dict)



### random 난수 함수들
# 외장모듈 필요
# import random
# random.randint(start, end)
# : start~end 사이의 정수 난수
# random.choice(리스트)
# : 리스트에서 랜덤하게 뽑는다.
# random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다.

import random
# random.randint(start, end) : start~end 사이의 정수 난수
print(random.randint(1,10))



## 퀴즈 ##
# 로또 번호 뽑기 (1~46 숫자중에서 6개를 뽑아 로또 리스트를 생성한다.)
# 조건 - 로또 번호는 중복값이 없어야 한다.
lotto_list =[]
while len(lotto_list)<6:
    num = random.randint(1, 46)
    if num not in lotto_list:
        lotto_list.append(num)
    lotto_list.sort()
print(lotto_list)

# 함수 ver.
def make_lotto():
    lotto_list =[]
    while len(lotto_list)<6:
        num = random.randint(1, 46)
        if num not in lotto_list:
            lotto_list.append(num)
    lotto_list.sort()
    return lotto_list

print(f'로또 번호 : {make_lotto()}')
print(f'로또 번호 : {make_lotto()}')
print(f'로또 번호 : {make_lotto()}')



### random.choice(리스트)
# : 리스트에서 랜덤하게 1개만 뽑는다.
gift_list = ['초코파이', '미니쿠퍼', '32평 자이 아파트', '금 3돈', '신라면 1박스', '스타벅스 상품권 10만원', '새우깡']

print(' 상품 추첨 => ', random.choice(gift_list))
print(' 상품 추첨 => ', random.choice(gift_list))
print(' 상품 추첨 => ', random.choice(gift_list))
print(' 상품 추첨 => ', random.choice(gift_list))



### random.shuffle(리스트)
# : 리스트를 랜덤하게 섞는다.

## 퀴즈
# 오늘 청소 당번은? ?, ?
# 내일 청소 당번은? ?, ?

student_list = ['기대주', '하민수', '이동백', '김철수', '홍길동']
print(student_list)
random.shuffle(student_list)
print(student_list, '오늘 청소 당번은? ', student_list[:2])
random.shuffle(student_list)
print(student_list, '내일 청소 당번은? ', student_list[:2])



## 퀴즈 11
# 다음 리스트를 이용하여 7개의 이름으로 구성된 리스트를 생성하여라.
# 이때 최종 리스트는 중복 이름이 없어야하며 가나다순으로 정렬되어야한다.
'''
first_name = ['박', '김', '이', '최', '신', '장', '윤']
last_name1 = ['은', '강', '종', '영', '준', '민']
last_name2 = ['철','수', '미', '원', '주', '혁', '희', '수']

>>> 생성된 이름 예시 
['박영수', '박준혁', '신영수', '신종주', '이민수', '이종혁', '최강철']

'''
first_name = ['박', '김', '이', '최', '신', '장', '윤']
last_name1 = ['은', '강', '종', '영', '준', '민']
last_name2 = ['철','수', '미', '원', '주', '혁', '희', '수']

new_name = []
for i in range(7):
    full = random.choice(first_name) + random.choice(last_name1) + random.choice(last_name2)
    if full not in new_name:
    new_name.append(full)
    new_name.sort()
print(f'생성된 이름 예시\n {new_name}')

# 함수 ver.
def make_name():
    first_name = ['박', '김', '이', '최', '신', '장', '윤']
    last_name1 = ['은', '강', '종', '영', '준', '민']
    last_name2 = ['철', '수', '미', '원', '주', '혁', '희', '수']
    name_list = []
    while True:
        x = random.choice(first_name)
        y = random.choice(last_name1)
        z = random.choice(last_name2)
        if len(name_list) >= 7:
            break
        if (x + y + z) not in name_list:
            name_list.append(x + y + z)
    name_list.sort()
    print(name_list)

make_name()
make_name()
make_name()




#-------------------------------------------------------------------
# filter(함수명/lambda 함수, 리스트/튜플),
# map(함수명/lambda 함수, 리스트/튜플),
# reduce(함수명/lambda 함수, 리스트/튜플)
# 정의된 사용자정의함수, 람다함수를  리스트 데이타 각각에 적용한다.




### filter()
# filter(함수명/lambda 함수, 리스트/튜플)
# 사용할 함수는 결과값이 True/False 여야 함.
# 함수를 적용하여 리스트/튜플의 data에서 True 인것만 Return
# => 참인조건의 리스트만 출력

# 리스트에서 짝수만 새로운 리스트로 생성
num_list = [1,100,56,89,90,234,-88]

# 일반 함수 이용
def filter_num(list):
    result = []
    for i in list:
        if i%2 == 0:
            result.append(i)
    return result

print(num_list, '=>', filter_num(num_list))

# filter() + 일반함수
# 1) 리스트요소 각각에 적용되는 함수 정의 => 결과값은 True/False

# 숫자가 짝수이면 true 반환
def odd_check(n):
    if n%2 ==0:
        return True

print(odd_check(1)) # none
print(odd_check(100)) # true

# 2) filter() 에 함수 적용
# filter(함수명/lambda 함수, 리스트/튜플) => filter 객체 => list(filter 객체)
print(filter(odd_check, num_list))  # <filter object at 0x000001CC65D393D0>
print(list(filter(odd_check,num_list)))  # [100, 56, 90, 234, -88]
print(num_list , ' => ' , list(filter(odd_check, num_list)))



# filter() + 람다함수
# 함수변수 = lambda 인자: 명령문
# 함수변수(인자)
'''
def odd_check(n):
    if n%2 == 0:
        return True
'''
odd_check2 = lambda n: n%2 == 0
print(odd_check2(100)) # True
print(odd_check2(1)) # False

# filter(lambda 함수, 리스트/튜플) => filter 객체 => list(filter 객체)
num_list = [ 1, 100, 56, 89, 90, 234, -88 ]
print(filter(lambda n: n%2 == 0, num_list ))
print(list(filter(lambda n: n%2 == 0, num_list )))  # [100, 56, 90, 234, -88]
print(num_list , ' => ' , list(filter(lambda n: n%2 == 0, num_list )))


## 퀴즈
# 음수만 출력하여라
# numList = [100, -45, 20, 40, -500]
# 결과
# [-45, -500]
numList = [100, -45, 20, 40, -500]

# 일반 함수 이용
def filter_negative(list):
    result = []
    for i in list:
        if i < 0:
            result.append(i)
    return result

print(numList, '=>', filter_negative(numList))

# filter + 일반함수
def negative_check(n):
    if n <0:
        return True

print(numList , ' => ' , list(filter(negative_check, numList)))

# filter + lambda 함수
print(numList, '=>', list(filter(lambda n: n<0, numList)))



## 퀴즈 ##
# 아래 리스트에서 특수문자를 제외하고 모두 문자로 구성되어 있는 문자만 별도 리스트로 출력하여라.
# filter 이용
# pwd_list = ['CER9jvT3', 'QRUc!f^J', 'FQPtBKGZ', '8adlQIFb', 'j8Prk&l9', 'gfhsgefs', '67hdgsfeb$$', 'fsjhwety']
pwd_list = ['CER9jvT3', 'QRUc!f^J', 'FQPtBKGZ', '8adlQIFb', 'j8Prk&l9', 'gfhsgefs', '67hdgsfeb$$', 'fsjhwety']

# filter + lambda 함수
print(list(filter(lambda n: n.isalpha(),pwd_list)))

# 일반함수
def filter_pwd(list):
    result = []
    for i in list:
        if i.isalpha():
            result.append(i)
    return result
print(pwd_list , '\n => ' , filter_pwd(pwd_list))

# filter + 일반함수
def check_pwd(txt):
    return txt.isalpha()

print(pwd_list , '\n => ' , list(filter(check_pwd, pwd_list)))






### map() 함수 ###
# map(정의된함수나 lambda함수,데이타(리스트,튜플))
# -> map오브젝트 생성
# list(map(정의된함수나 lambda함수, 데이타(리스트,튜플)))
# 데이타 요소를 정의된 함수의 결과값으로 리턴한다.
# 결과값을 리스트 요소로 추가

# 아래 리스트의 제곱값으로 구성된 리스트를 출력하라
num_list = [1,2,4,5,7]

# 일반함수
def make_power(list):
    result = []
    for i in list:
        result.append(i**2)
    return result
print(num_list, '=', make_power(num_list))


# map + 일반함수
# 1) 리스트요소 각각에 적용되는 함수 정의 => 결과값 반환
def power_n(n):
    return n**2

# 2) map(일반함수, 리스트/문자열/튜플) => map객체 => list(map객체)
print(num_list, '=>',list(map(power_n, num_list)))


# map + lambda
# map(lambda 인자: 명령문, 리스트/문자열/튜플) => map객체 => list(map객체)
print(num_list, '=>', list(map(lambda n: n**2, num_list)))



# 각 위치 요소의 곱으로 구성된 리스트를 출력하여라
list1 = [23, 45, 66, -12, 56, 77, 89]
list2 = [4, 5, 23, 56, 67, 89, 12]

# 일반 함수 이용
def multy_list(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append(list1[i]*list2[i])
    return result
print(list1, list2, '=>', multy_list(list1,list2))

# map + 일반함수
def mul_idx(n1,n2):
    return n1*n2
print(list1,list2, '\n =>', list(map(mul_idx, list1,list2)))

# map + lambda
print(list1,list2, '\n =>', list(map(lambda n1,n2: n1*n2, list1,list2)))





### reduce() ###
# 리스트의 요소에 함수를 적용해 1개의 결과를 리턴한다.
# reduce(람다함수나 정의한 함수, 리스트나 튜플)

# 외장함수로 import functools 모듈 임포트 명령 필요
# 모듈내의 함수 사용1?
# import functools
# functools.reduce(옵션)
# 모듈내의 함수 사용2? = 별칭 지정
# import functools as f
# f.reduce(옵션)

import functools as f

# 리스트의 모든 곱 구하기
# 1~10으로 구성된 리스트 생성 : range()
num_list = list(range(1,11))
print(num_list)

# 일반함수
def multy_all(list):
    result = 1
    for item in list:
        result *= item
    return result
print(num_list, '=>', multy_all(num_list))

# reduce + 일반함수
# 1) 리스트의 2요소에 적용할 함수 정의 => 결과값 반환
def multy_n(x,y):
    return x*y

# 2) 모듈명.reduce(일반함수, 리스트/문자열/튜플) => reduce 객체
# print(f.reduce(multy_n, num_list))
print(num_list, '=>', f.reduce(multy_n, num_list))

# reduce + lambda
print(num_list, '=>', f.reduce(lambda x,y: x*y , num_list))





## 퀴즈 1
# 리스트를 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경되도록 프로그래밍하여라.
# 이때 딕셔너리 키는 'class숫자' 형태이며
# map 함수를 이용해야한다.
'''
 map함수와 lambda 이용 결과 >> 
 class_list = ['python', 'mySQL', 'HTML', 'CSS', 'scrapping', 'kaggle']
[{'class_1': 'python'}, {'class_2': 'mySQL'}, {'class_3': 'HTML'}, {'class_4': 'CSS'}, {'class_5': 'scrapping'}, {'class_6': 'kaggle'}]
'''
class_list = ['python', 'mySQL', 'HTML', 'CSS', 'scrapping', 'kaggle']

# 내 풀이
class_n = []
for i in range(1,len(class_list)+1):
    class_n.append('class_'+str(i))
print(class_n)

print(list(map(lambda x,y:{x:y},class_n,class_list )))

# 일반함수
def make_dict(list):
    result = []
    for i in range(len(list)):
        temp = {}
        temp['class_'+str(i+1)] = list[i]
        result.append(temp)
    return result

class_list = ['python', 'mySQL', 'HTML', 'CSS', 'scrapping', 'kaggle']
print(make_dict(class_list))

# map 함수 적용
print(list(map(lambda k,v:{'class_' + str(k): v}, list(range(1,len(class_list)+1)), class_list)))

print(list(map(lambda x, y:{f'class_{x+1}': y}, range(len(class_list)), class_list)))





## 퀴즈 2
# 5~10 까지의 모든 수의 곱이 출력되도록 프로그래밍하여라.
# lambda 함수, reduce()를 이용해야한다.

# reduce() 함수 임포트 명령어는?
# import functools as f

'''
5 ~ 10 까지의 곱 >> 
numList = [5, 6, 7, 8, 9, 10]
5 X 6 X 7 X 8 X 9 X 10  =  151200
'''
numList = [5, 6, 7, 8, 9, 10]

print(" X ".join([str(i) for i in numList ]) , ' = ', f.reduce(lambda x,y:x*y , numList))




## 퀴즈 3
# 아래 리스트에서 정수의 합구하기
# reduce() 이용, filter() 이용
numlist10 = [True, 1, 'Yes', 2, 3, 5, 6, 'a']
print(numlist10, '=>', f.reduce(lambda x,y: x+y,list(filter(lambda x:type(x)== int, numlist10))))


def add_n(x, y):
    return x+y
print(list(filter(lambda x:type(x)==int, numlist10)))
print(numlist10, ' => ' , f.reduce(add_n, list(filter(lambda x:type(x)==int, numlist10))))





# --------------------------------------------------------------------
# 프로그래밍 언어 분류
# 인터프리터(파이썬, JS...) VS 컴파일러(JAVA, C, C#, C++ ...)
# 절차지향(C..) VS 객체지향(파이썬, JAVA ...)

# 객체지향의 특징
# 클래스 => 특별한 자료구조 (변수 + 함수) , 설계도
# 클래스 => 인스턴스(객체)

# 기본자료형(정수, 실수, 논리, 문자열) < 집합자료형(튜플, 리스트, 딕셔너리, 집합...) => 변수
# 함수

# 클래스의 구성 요소 => 속성 + 메서드

# 클래스 생성
'''
class 클래스명:
    명령문
클래스명은 첫글자는 대문자로 시작
'''

# 자동차 클래스
class Car:
    pass
print(Car, type(Car)) # <class '__main__.Car'> <class 'type'>

# 객체화
'''
인스턴스명 = 클래스명()

# 인스턴스명은 소문자로 지정 
'''
bus = Car()
sports_car = Car()
print(bus, type(bus))
print(sports_car, type(sports_car))
'''
<__main__.Car object at 0x00000236656D8FD0> <class '__main__.Car'>
<__main__.Car object at 0x00000236656780A0> <class '__main__.Car'>
'''




















































