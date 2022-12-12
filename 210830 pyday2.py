# 문자열 함수

# 샘플 문자열 만들기
# http://www.lipsum.com 이용


sample = '''
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''


# 특정 문자열의 갯수 출력
# 문자열변수.count(찾고자하는문자열)

print(sample.count('Lorem'), sample.count('s'))  # 4 39

# 특정 문자열의 시작인덱스 위치 반환
# 문자열변수.find(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 -1 반환
# 문자열변수.index(찾고자하는문자열)
# 찾고자 하는 문자열이 없다면 에러 발생

print(sample.find('Lorem'), sample.find('홍길동'))  # 1 -1
print(sample.index('Lorem'), sample.index('홍길동'))  # ValueError: substring not found



# 문자열 교체하기

# 문자열변수.replace(찾고자하는문자열, 교체문자열)
# is => was
sample2 = sample.replace('is','was')
print(sample2)
print(sample2.count('was'))  # 4


# '연결문자'.join(문자열변수)
msg = '가나다라마바사'
print(msg)
print(' '.join(msg))


# 좌우 공백 제거하기
# 문자열변수.strip()
# 문자열변수.rstrip()
# 문자열변수.lstrip()
print('-'*50)
msg = '    가나다라마바사    '
print(f'$$${msg}$$$')
print(f'$$${msg.strip()}$$$')
print(f'$$${msg.rstrip()}$$$')
print(f'$$${msg.lstrip()}$$$')


# 대소문자 변환
# 문자열변수.upper()
# 문자열변수.lower()
# 문자열변수.title()
print(sample.upper())

# sample 텍스트에서 it + It 의 총 개수는?
print(sample.count('it'), sample.count('It'), sample.count('it')+sample.count('It'))  # 3 2 5
print(sample.upper().count('IT'))  # 5


# split() : 문자열에서 공백을 기준으로 분리 => 리스트
# split(구분자문자) : 문자열에서  구분자문자를 기준으로 분리 => 리스트
txt1 = "Life is too short"
txt2 = "Life,short,world,Hello"
print(txt1.split())  # ['Life', 'is', 'too', 'short']
print(txt2.split(','))  # ['Life', 'short', 'world', 'Hello']



# 자료형의 종류
# 기본 자료형 - 문자열, 정수, 실수, 불린형
# 집합형 자료형=콜렉션 : 여러개의 구성요소로 조직화
#       : 리스트 [], 튜플 (), 딕셔너리 { }, 집합{ }

# 생성1
# 초기값 설정 방식을 이용한 리스트 정의
# 리스트변수 = [값1, 값2...]

# 리스트 원소의 데이터형은 혼합이 가능
myList = [100, True, 'python', 3.14, '홍길동']
print(f'myList = {myList}, 총길이는? {len(myList)}, 데이터형은? {type(myList)}')


# 생성2
# 1) 빈 리스트를 이용한 리스트 정의
# 리스트변수 = []
# 2) 리스트에 원소 삽입
# 리스트변수.append(원소값)
# 리스트변수.insert(인덱스, 원소값)
# 리스트변수.extend([원소값...])

# 빈 리스트 생성 후 원소 삽입
fruitList = []
print(f'fruitList = {fruitList}, 총길이는? {len(fruitList)}')  # fruitList = [], 총길이는 0
# 한개씩
fruitList.append('수박')
fruitList.append('참외')
print(f'fruitList = {fruitList}, 총길이는? {len(fruitList)}')  # 확인
fruitList.insert(0, '오렌지')  # 숫자는 인덱스 넘버
print(f'fruitList = {fruitList}, 총길이는? {len(fruitList)}')  # 확인
# 여러개(리스트 형식으로 추가되어야 한다)
fruitList.extend(['자두','복숭아','포도'])
print(f'fruitList = {fruitList}, 총길이는? {len(fruitList)}')  # 확인



# 리스트 인덱싱
# 리스트이름[숫자] : 0부터 시작, 숫자값이 -1 마지막 요소 표시

numList = [100,200,3000,400,500,600,700]
print(f'numList = {numList}')
print(numList[0])
print(numList[-1], numList[6], numList[len(numList)-1])


# 리스트 슬라이싱
# 리스트이름[start:end:step]
# 리스트이름[start:end]
# 리스트이름[start:]
# 리스트이름[:end]
# 리스트이름[::step]
# 리스트이름[:] = 리스트이름[::] => 전체리스트

print(f'\n numList = { numList }')
print(f' numList = { numList[1:5] }')
print(f' numList = { numList[4:] }')
print(f' numList = { numList[:5] }')
print(f' numList = { numList[::2] }')
print(f' numList = { numList[1::2] }')
print(f' numList = { numList[::-1] }')
'''
 numList = [100, 200, 300, 400, 500, 600, 700]
 numList = [200, 300, 400, 500]
 numList = [500, 600, 700]
 numList = [100, 200, 300, 400, 500]
 numList = [100, 300, 500, 700]
 numList = [200, 400, 600]
 numList = [700, 600, 500, 400, 300, 200, 100]
'''



# Update : 리스트 값 변경하기
# 리스트변수[인덱스] = 값
numList[0] = '백'
print(f'\n numList = { numList }')

# 리스트변수[start:end] = [값...]
numList[1:4] = ['이백','삼백','사백']
print(f'\n numList = { numList }')

# TypeError: can only assign an iterable
# numList[4:] = 0
# print(f'\n numList = { numList }')




# 리스트 삭제와 관련된 함수와 명령어
# 리스트변수.remove(값) : 값으로 삭제하기
# 리스트변수.pop() : 마지막 요소가 삭제되면서 값이 반환된다.
# 리스트변수.pop(인덱스) : 위치에 해당하는 요소가 삭제되면서 값이 반환된다.
# 리스트변수.clear() : 리스트안의 값이 모두 삭제. 빈리스트로 된다.
# del 리스트변수 : 리스트 자체가 삭제된다.
# del 리스트변수[인덱스] : 리스트의 특정 위치가 삭제된다.

numList = [100, 200, 300, 400, 500, 600, 700]
print(f'\n numList = {numList}')
numList.remove(500)
print(f'\n numList = {numList}')  # 확인
del numList[0]
print(f'\n numList = {numList}')  # 확인
print(f'\n 삭제요소 => {numList.pop()}')
print(f'\n numList = {numList}')  # 확인
print(f'\n 삭제요소 => {numList.pop(0)}')
print(f'\n numList = {numList}')  # 확인
numList.clear()
print(f'\n numList = {numList}')  # 확인
del numList  # 리스트 삭제
print(f'\n numList = {numList}')  # 확인 - NameError: name 'numList' is not defined



# 리스트 연산
# 리스트1 + 리스트2 : 같이 표시
# 리스트이름*숫자 : 반복
# extend() 와 리스트 + 연산 테스트
list_a = ['강아지', 100]
list_b = ['고양이', 500]
list_c = list_a + list_b
# list_a.extend(list_b)
list_cc = list_a.copy() # 복사본 생성
list_cc.extend(list_b)
list_d = list_a*3
print(f'\n list_a = { list_a } \t list_b = { list_b }')
print(f'\n list_c= { list_c }')
print(f'\n list_cc= { list_cc }')
print(f'\n list_d = { list_d }')




# 리스트 값 정렬하기
# 리스트변수.reverse()
# 리스트변수.sort()
# 주의사항은 리스트변수.sort()의 경우
# 리스트를 이루는 구성요소의 데이터형은 같아야한다
# TypeError 발생

myList = ['사과', '강아지', '아리랑']
# myList = ['사과', '강아지', '아리랑', 100]  # sort() 에러
print(f'\n myList = { myList } ')
print(myList.sort())  # None
myList.sort()
print(f'\n myList = { myList } ')
myList.reverse()
print(f'\n myList = { myList } ')



# 문자열 => 리스트
# 문자열 변수.split(구분문자)
# list(문자열변수)
# : 공백도 모두 리스트화. 낱글자가 아이템요소로 변경
txt = 'a bcdefghij'
print(f'\n { list(txt)}, 길이는? {len(list(txt))} ')
print(f'\n { txt.split()}, 길이는? {len(txt.split())} ')



# 중첩 리스트 구조
# 리스트안에 리스트가 있다
# 중첩리스트의 인덱싱은?
# 리스트이름[index1][index2]

# 중첩 리스트 생성1
# 초기값으로 중첩 리스트 생성
# 리스트변수 = [ [값1, 값2...],[값1, 값2...]]


# 중첩 리스트 생성2
# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성

# 중첩 리스트 (3X3)
list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f' list_a = {list_a}')
print(f' list_a[0] = {list_a[0]}')
print(f' list_a[-1] = {list_a[-1]}')
print(f' list_a[0][0] = {list_a[0][0]}')
print(f' list_a[-1][-1] = {list_a[-1][-1]}')
'''
 list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 list_a[0] = [1, 2, 3]
 list_a[-1] = [7, 8, 9]
 list_a[0][0] = 1
 list_a[-1][-1] = 9
 list_a[1][1] = 5
'''



# 중첩 리스트 ( 구성 요소 리스트의 길이가 서로 다른 경우)
list_b = ['1-1', ['2-1', '2-2'], ['3-1', '3-2', '3-3', '3-4']]
print('='*50)
print(f' list_b = {list_b}')
print(f' list_b[0] = {list_b[0]}')
print(f' list_b[1][1] = {list_b[1][1]}')
print(f' list_b[2][1] = {list_b[2][1]}')



# 1차원 리스트 정의 후 1차원 리스트를 다시 리스트로 구성
# 1차원 리스트 정의
kor = [ 55, 66, 34, 60]
math = [ 78, 90, 45, 88]
eng = [ 56, 98, 78, 90]
# 2차원 리스트 정의 (3x4)
grade = [kor, math, eng]
print(f' grade = {grade}')
print(len(grade), len(grade[0]))



# 퀴즈 :
'''
아래의 리스트를 이용하여 grade 리스트를 생성하고 합계와 평균을
과목별로 출력한다. 평균은 소숫점 2번째 자리까지 출력한다.

kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]
------------
result
kor : 합계 = ? , 평균 = ?
math : 합계 = ? , 평균 = ?
eng : 합계 = ? , 평균 = ?
python : 합계 = ? , 평균 = ?
'''

kor = [100, 80, 85]
math = [55, 70, 35]
eng = [80, 80, 100]
python = [90, 70, 88]

grade = [kor, math, eng, python]
print('='*50)
print(f' grade 리스트는? {grade}')
kor_tot = grade[0][0] + grade[0][1] + grade[0][2]
print(f' kor : 합계 = {kor_tot} , 평균 = {(kor_tot/3):.2f} ')
# sum(리스트변수) : 리스트합
print(f' math : 합계 = {sum(grade[1])} , 평균 = {(sum(grade[1])/3):.2f} ')

print(f' eng : 합계 = {sum(grade[2])} , 평균 = {(sum(grade[2])/len(grade[2])):.2f} ')

print(f' python : 합계 = {sum(grade[3])} , 평균 = {(sum(grade[3])/len(grade[3])):.2f} ')



# 튜플
# CRUD : Create Read Update(Add)
# 튜플 생성1 (초기값 지정)
# 튜플변수 = (값1, 값2...)

# 튜플 생성2 (초기값 지정) - () 생략 가능
# 튜플변수 = 값1, 값2...

# 튜플 생성3 (빈 튜플)
# 튜플변수 = ()
# += 연산자를 이용하여 요소 추가

# 튜플 생성1 (초기값 지정)
t1 = (100, 200, 300)
print(f'\n\n t1 = {t1} 데이타형 { type(t1)}')

# 튜플 생성2 (초기값 지정)
t2 = '사과', True, 3.14
print(f' t2 = {t2} 데이타형 { type(t2)}')

# 튜플 생성3
t3 = ()
print(f' t3 = {t3} 데이타형 { type(t3)}')
# TypeError: can only concatenate tuple (not "str") to tuple
# t3 += ('한국')
# 한개씩 추가할 경우 쉼표 주의
t3 += ('한국',)
print(f' t3 = {t3} 데이타형 { type(t3)}')
t3 += ('독일', '싱가폴')
print(f' t3 = {t3} 데이타형 { type(t3)}')



# 튜플 인덱싱
# 튜플변수[인덱싱위치번호] , 0부터 시작
# 튜플 슬라이싱
# 튜플변수[start:end:step]
t1 = (100, 200, 300, 400, 500)
print(f'\n\n t1 = {t1} 데이타형 { type(t1)} 길이는? {len(t1)}')
print(t1[3] ,t1[-2])
print(t1[:3] ,t1[-3:]) #(100, 200, 300) (300, 400, 500)
print(t1[::2] ,t1[::-1])



# 튜플은 값을 수정할수 있을까?
# TypeError: 'tuple' object does not support item assignment
t1[0] = 0
print(t1)


# 튜플은 값을 삭제할 수 있을까?
# 전체 삭제만 가능
# TypeError: 'tuple' object doesn't support item deletion
# del t1[0]
del t1
# NameError: name 't1' is not defined
# print(t1)



# 튜플의 연산자 + : 튜플끼리 더하기
# 튜플의 연산자 * 숫자 : 튜플 요소 반복
t1 = (10, '파이썬')
t2 = (20, 'SQL')
print(t1+t2)
print(t1*5)



# 각각 튜플 변수 정의하기
# 튜플전체변수 = (변수1, 변수2...) = (값1, 값2...)
user1 = (name, age, gender, nation) = ('Maria', 28, 'female', 'USA')
print(user1)
print(name, age, gender, nation)
print(user1[0], user1[1], user1[2], user1[3])



# 리스트 튜플 : 리스트안에 튜플이 있는 형태
# 리스트안에 튜플이 삽입되어 있는 구조
myTuple = [('홍길동', 20), ('고길동', 25), ('최길동', 22)]
print(myTuple, type(myTuple)) # [('홍길동', 20), ('고길동', 25), ('최길동', 22)] <class 'list'>
print(myTuple[0], type(myTuple[0])) # ('홍길동', 20) <class 'tuple'>
print(myTuple[1][0], type(myTuple[1][0])) # 고길동 <class 'str'>



# 중첩 튜플 구조
myTuple2 = (('홍길동', 20), ('고길동', 25), ('최길동', 22))
print(myTuple2, type(myTuple2))



# 캐스팅
# 문자열 => 튜플 : tuple(문자열변수)
# 리스트 => 튜플 : tuple(리스트변수)
# 튜플 => 리스트 : list(튜플변수)
# 튜플 => 문자열 : str(튜플변수),  ''.join(튜플변수)

txt = '도레미파솔라시도'
myList = [100, 300, 500, 7, 99]
myTuple = ( 'True', 'False', '3.14')
print(txt, ' => ',  tuple(txt))
print(myList, ' => ',  tuple(myList))
print(myTuple, ' => ',  ' : '.join(myTuple))



# 퀴즈
# 튜플의 CRUD 각 단계로 튜플안에 데이타를 추가/삭제/변경하여 보세요
# 1) ('강아지','토끼','돼지','곰')
# 2) ('강아지','토끼','돼지','곰', '호랑이')
# 3) ('토끼','돼지','곰', '호랑이')
# 4) ('토끼','펭귄', '돼지','곰', '호랑이')

print('='*50)
animal = ('강아지', '토끼', '돼지', '곰')
print(animal) # ('강아지', '토끼', '돼지', '곰')
animal += ('호랑이', )
print(animal) # ('강아지', '토끼', '돼지', '곰', '호랑이')
animal = list(animal)
animal.remove('강아지')
animal = tuple(animal)
print(animal) # ('토끼', '돼지', '곰', '호랑이')
animal = list(animal)
animal.insert(1, '펭귄')
animal = tuple(animal)
print(animal) # ('토끼', '펭귄', '돼지', '곰', '호랑이')



# 딕셔너리
# CRUD : Create Read Update Delete


# 딕셔너리 생성(1) - 초기값 지정
# 딕셔너리변수 = {키1:값1, 키2:값2,...}
# 키값은 문자형, 숫자형 둘다 가능


# 딕셔너리 생성(2) - 빈 딕셔너리 생성 후 값 추가
# 딕셔너리 요소 추가
# 딕셔너리변수[키]=값


# 문자열키로 구성된 딕셔너리
dict1 = {'a':'apple', 'b':'banana', 'c':'cat', 'd':'dress'}
print(dict1, type(dict1), len(dict1))

# 중복키는 허용x, 중복값은 허용
dict2 = {'a':'apple', 'b':'banana', 'c':'cat', 'd':'dress', 'a':'apart', 'e':'dress'}
print(dict2, type(dict2), len(dict2))


# 빈 딕셔너리 생성
dict3 = {}
print(dict3, type(dict3), len(dict3)) # {} <class 'dict'> 0
# 딕셔너리 요소 추가 - 딕셔너리변수[키] = 값
dict3[1] = '하나'
dict3[100] = '백'
dict3[1000] = '천'
print(dict3, type(dict3), len(dict3))


# Update
# 딕셔너리 값 교체
# 딕셔너리[기존키]=값
dict3[100] = 'hundred'
print(dict3, type(dict3), len(dict3))



# Read
# 딕셔너리 요소 조회 : 키인덱싱
# 딕셔너리변수[키값] => 해당요소의 값 표시
# 리스트, 튜플 처럼 순차적인 숫자인덱싱 X , 슬라이싱 X
dict1 = {'a':'apple', 'b':'banana', 'c':'cat', 'd':'dress'}
print(dict1)
print(dict1['a']) # apple

# KeyError: 0
# print(dict1[0])
# print(dict1[-1])


# Delete
# 딕셔너리변수.clear() => {}
# 딕셔너리변수.pop(키값)
# del 딕셔너리변수[키값]
# del 딕셔너리변수 : 메모리에서 삭제

dict1 = {'a':'apple', 'b':'banana', 'c':'cat', 'd':'dress', 'e':'eat'}
print(dict1)
dict1.pop('c')
print(dict1) # {'a': 'apple', 'b': 'banana', 'd': 'dress', 'e': 'eat'}
del dict1['e']
print(dict1) # {'a': 'apple', 'b': 'banana', 'd': 'dress'}
dict1.clear()
print(dict1) # {}



# 딕셔너리 함수
# 딕셔너리변수.values() : 값 만 표시
# 딕셔너리변수.keys() : 키값만 표시
# 딕셔너리변수.items() : 튜플스타일로 표시 (키, 값)...
sports = {"축구":"박지성", "야구":"강정호", "체조":"손연제"}
print('='*50)
print(sports)
print(sports.values())
print(sports.keys())
print(sports.items())



# 집합
# 순서가 없다. 랜덤하게 출력된다.
# 인덱싱이 불가능하다. 슬라이싱 불가능하다.
# 중복값을 허용할까요? => 1개만 표시

# Create
# 집합변수 = {값1, 값2, 값3....}
# 집합변수 = set(리스트/문자열/튜플)

s1 = {10, 20, 30, 40}
s2 = set(['축구', '야구', '체조'])
s3 = set('anaconda')
print(s1, type(s1), len(s1))  # {40, 10, 20, 30} <class 'set'> 4
print(s2, type(s2), len(s2))  # {'체조', '축구', '야구'} <class 'set'> 3
print(s3, type(s3), len(s3))  # {'c', 'n', 'a', 'd', 'o'} <class 'set'> 5



# Read
# 인덱싱이 불가능하다. 슬라이싱 불가능하다.
# TypeError: 'set' object is not subscriptable
# print(s1[0])



# 집합의 요소 추가
# 집합변수.add(값)
# 집합변수.update([값1, 값2...])
# mySet = set(['축구', '야구', '체조', '탁구', '승마'])
mySet = {'축구', '야구', '체조', '탁구', '승마'}
print(mySet)
mySet.add('리듬체조')
print(mySet)  # 주머니 구조, 순서 상관 없이 담김

mySet.update(['육상','볼링'])
print(mySet)


# 집합의 요소 삭제
# 집합변수.remove(값)
# del 집합변수 => 메모리에서 삭제
mySet.remove('리듬체조')
print(mySet)
mySet.clear()
print(mySet)  # set()



# 집합 연산 및 함수
# +,-,*,/ 연산자 사용 불가능.
# 집합 합치기 = 합집합
# 집합변수3 = 집합변수1|집합변수2
# 집합변수3 = 집합변수1.union(집합변수2)

# 차집합
# 집합변수3 = 집합변수1-집합변수2
# 집합변수3 = 집합변수1.difference(집합변수2)
userSet7 = userSet1-userSet2

# 교집합
# 집합변수3 = 집합변수1&집합변수2
# 집합변수3 = 집합변수1.intersection(집합변수2)

# 대칭차집합 = 합집합-교집합
# 집합변수3 = 집합변수1^집합변수2
# 집합변수3 = 집합변수1.symmetric_difference(집합변수2)

set1 = {'강','선우','김','이','박'}
set2 = {'신','장','김','이','최'}
print(set1,set2)
print(f'합집합 => {set1|set2} {set1.union(set2)}')
print(f'교집합 => {set1&set2} {set1.intersection(set2)}')
print(f'차집합 => {set1-set2} {set1.difference(set2)}')
print(f'대칭차집합 => {set1^set2} {set1.symmetric_difference(set2)}')



# 자료형 변환
# list(), set(), tuple()
# str(), '구분자'.join(문자열 형태의 리스트/튜플/집합)
# 리스트/튜플/집합 => 딕셔너리화 (숫자인덱스가 키가 된다.)
# enumerate() : enumerate() 객체화
# dict()
myList = ['강','이','김','선우','박']
myDict = enumerate(myList)  # enumerate 객체화
print(myDict)  # <enumerate object at 0x00000181D4908600>
# 딕셔너리화
myDict = dict(enumerate(myList))
print(myDict, type(myDict))  # {0: '강', 1: '이', 2: '김', 3: '선우', 4: '박'} <class 'dict'>








