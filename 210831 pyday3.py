'''2일차 리뷰
- 문자열 함수
                   CREATE         READ                UPDATE(수정)       DELETE
- 리스트            [값]         인덱싱, 슬라이싱            O                 O
- 튜플              (값)         인덱싱, 슬라이싱            X                 X
- 집합              {값}           X                      X                 O
- 딕셔너리          {키:값}       키인덱싱                   O                 O
'''





# 리터럴 값의 True / False
# False => 0 , '', "", [], {}, ()
# 숫자는 0을 제외하면 True로 변환
print(bool(0), bool(10), bool(-1), bool(3.14))  # False True True True
# 문자열은 '' "" '''''' """""" => False / 문자가 뭐라도 있으면 True
print(bool(''), bool(' '), bool('Hello world')) # False True True
# 집합형자료형(리스트/튜플/딕셔너리/집합)는 길이가 0이면 False
print(bool([]), bool([100, 200, 300])) # False True




# 파이썬 제어문
# 제어문의 종류
# - 조건문 : if / if ~ else / if ~ elif ~ else
# - 반복문 : for / while

# 파이썬 제어문의 특징 :
# {} 사용하지 않고 탭1개 나 공백4칸 으로 블록 지정
# 들여쓰기가 없는 경우 IndentationError: 에러 발생
# switch 문이 없다
# else if 대신 elif 문이 있다



# 단순 if 문
# if 문
# if True조건식:
#    실행할 문장

num1 = 500
num2 = 300
if (num1 > num2):
    print(f'{num1}이 {num2} 보다 크다')
print('='*50)
if num1 < num2:
    print(f'{num2}이 {num1} 보다 크다')
if num1 == num2:
    print(f'{num2}과 {num1} 값은 같다')
    print('$'*50)



# 짝수인지 홀수인지 판단 ?
# 숫자%2 == 0
num = int(input('숫자 입력 => '))
if (num%2 == 0):
    print("짝수")
if (num % 2 != 0):
    print("홀수")



# if 조건: - 2가지 조건이 있는 if문
#   명령문1
# else:
#   명령문2

num = int(input('숫자 입력 => '))
if (num%2 == 0):
    print("짝수")
else :
    print("홀수")


# money = 100
# money = '오만원'
# money = ''
# money = ['만원', '오천원', '500원']
money = []
if money:
    print("택시를 타고 간다")
else:
    print("걸어가야 한다.")



# 다중 if문
# else 문은 생략이 가능하다
# elif 문은 여러개 가능하다.
# if 조건1:
#   명령문1
# elif 조건2:
#   명령문2
# else:
#   명령문3


num1 = 100
num2 = 100
if (num1>num2) :
    print(f'{num1} 이 {num2} 보다 크다 ')
elif (num1<num2) :
    print(f'{num2} 이 {num1} 보다 크다 ')
elif (num1 == num2) :
    print(f'{num1} 과 {num1} 값은 같다')
# else:
#     print(f'{num1} 과 {num1} 값은 같다')



# 퀴즈 :
# 나이를 입력받는다.
# 나이에 따라서 서로 다른 메세지 출력
'''
당신의 나이를 입력해주세요? ...
~7 : 영유아
8 ~ 13 : 초등학생
14 ~ 16 : 중학생
17 ~ 19 : 고등학생
20 ~ : 성인
'''


age = int(input('당신의 나이를 입력해주세요? ...'))
if (age <= 7):
    print('영유아')
# elif (8 <= age <= 13):
elif (age <= 13):
     print('초등학생')
elif (age <= 16):
     print('중학생')
elif (age <= 19):
     print('고등학생')
else:
     print('성인')



# 띠 테스트
# 띠 = 태어난년도%12
# 원숭이, 닭, 개, 돼지, 쥐, 소, 범, 토끼, 용, 뱀, 말, 양
# (0  ........  11)
'''
태어난 년도를 입력하세요? 2009
당신은 소띠입니다.
'''




#  in / not in 연산자
# 아이템 in 그룹(튜플, 리스트, 문자열, 집합) => True / False
# 아이템 not in 그룹(튜플, 리스트, 문자열, 집합) => True / False

idol = ['블랙핑크','BTS','엑소']
print('블랙핑크' in idol)  # True
print('블랙핑크' not in idol)  # False




# if.. elif..else.. 문에 in/not in 연산자 사용하기
# if item in group(리스트,튜플,문자열,집합) :
#   명령문1
# elif item in group(리스트,튜플,문자열,집합) :
#   명령문2
# else:
#   명령문3


food = ['라면', '오므라이스', '고등어구이']
choice = input('주문 메뉴를 입력하여주세요...')
if choice in food:
    print('음식이 나왔습니다.')
else:
    print('메뉴 목록에 없습니다')



# pass 키워드
# 명령문의 일종으로 비실행
# 제어문, 함수, 클래스 생성시 등록만 시킬때 사용
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
# if 'zeropay' in pocket:
    pass
else:
    print("카드를 꺼내라")
print( 'pass 키워드 테스트 종료')


# if 문 안에 if문
user_id = 'asadal'
user_pwd = '1234'

if user_id == 'asadal':
    print('ID OK')
    if user_pwd == '1234':
        print('LOGIN OK')
    else:
        print('LOGIN FAIL')
else:
    print('ID FAIL')




# 퀴즈
# 입력받은 데이터에 따라 양수, 음수, 숫자가 아니다 출력
# 입력받은 데이타가 0인 경우에는 메세지를 출력하지 않는다.
# 문자열변수.strip() : 좌우공백 삭제
# 입력받은 데이타가 2글자 이상인 경우
# 첫번째 글자와 나머지 글자 찍기

myNum = int(input('숫자 입력...'))
print(myNum)



# 퀴즈
# 입력받은 데이터에 따라 양수, 음수, 숫자가 아니다 출력
# 입력받은 데이타가 0인 경우에는 메세지를 출력하지 않는다.
# 문자열변수.strip() : 좌우공백 삭제
# 문자열변수.isalpha() : 알파벳 또는 한글이면 True 반환
# 문자열변수.isdigit() : 숫자문자이면 True 반환
data1 = '12345'
data2 = '가나다라'
data3 = 'abcd1234'
print(data1.isalpha()) # False
print(data2.isalpha()) # True
print(data1.isdigit()) # True
print(data3.isdigit()) # False




data = input('데이타 입력 ...')
# 입력값이 숫자인지 문자인지 판독
if data.isdigit(): # 숫자인경우
    num = int(data)
    if num>0:
        print('양수')
    else:
        pass
else: # 숫자가 아닌경우
    if data[0] != '-':
        print('숫자가 아니다')
    elif data[1:].isdigit():
        print('음수')
    else:
        print('숫자가 아니다')




data = input('데이타 입력 ...').strip()
# 입력값이 숫자인지 문자인지 판독
if data.isdigit(): # 숫자인경우
    num = int(data)
    if num>0:
        print('양수')
    else:
        pass
else: # 숫자가 아닌경우
    if data[0] != '-':
        print('숫자가 아니다')
    elif data[1:].isdigit():
        print('음수')
    else:
        print('숫자가 아니다')






##### 반복문 #####

# 반복문 : while
# while whrjs:
#   실행명령
# 조건이 True면 명령을 실행해라.

# 특정 메시지를 n번 출력한다.
msg = 'Hello future'
cnt = 1  # 초기값
while cnt <= 10:
    print(cnt , msg)
    # 증감
    cnt += 1  # 이거 없으면 무한루프


# 10~1 까지 한줄에 출력하기
cnt = 10  # 초기값
while cnt>0:
    print(cnt, end = " ")
    cnt -= 1  # cnt 감소
print('\n테스트 종료')



# 퀴즈1 - 1~100까지의 합 출력하기
# 1~100까지의 합은?
cnt = 1
plus = 0
while cnt <= 100:
    # plus = plus + cnt
    plus += cnt
    cnt += 1
print(f'1 + 2 + 3 + 4 + ... + 100 = {plus}')



# 퀴즈2 : 1~50까지 짝수만 출력하기
# while 문 + if 문
# 2 4 6 8 ... 50
print('\n'*2)
cnt = 1
while cnt <= 50:
    if cnt % 2 == 0:
        print(cnt, end = ' ')
    cnt += 1



# 퀴즈3 : 1~100까지 5의 배수의 합 구하기
# while 문 + if 문
# 5 + 10 + 15 + ... + 100 = ?
print('\n'*2)
cnt, sum = 1, 0
while cnt<= 100:
    if cnt % 5 == 0:
         # 0 + 5 + 10 .... + 100
        sum += cnt
    cnt += 1
print(f' 1~100 까지 5의 배수의 합 =  { sum }')



# 구구단 n단 출력하기
'''
3 X 1 = 3
3 X 2 = 6
...
3 X 9 = 27
'''
print('\n'*2)
n = int(input(' 구구단 입력 => '))
cnt = 1
while cnt <= 9:
    print(f' {n} X {cnt} = {n*cnt} ')
    cnt += 1



# 한글자씩 행 단위로 출력하기
print('='*50)
cnt = 0
while (cnt<len(txt)):
     print(txt[cnt])
     cnt += 1



# 짝수번째만 한글자씩 행 단위로 출력하기
print('='*50)
cnt = 0
while (cnt<len(txt)):
     if (cnt%2 != 0):
          print('   '*cnt, end=' ')
          print(txt[cnt])
     #print()
     cnt += 1



# 가장 큰 수를 삭제하여라
# myNumList = [100, 200, 50, -30, 999, 10]
# 리스트명.remove(값)

# 리스트의 원소를 한행에 하나씩 출력
myNumList = [100, 200, 50, -30, 999, 10, 1000, 6732]
cnt = 0
while (cnt<len(myNumList)):
     print(myNumList[cnt])
     cnt += 1

# 리스트의 요소중에서 최댓값 구하기
temp = myNumList[0]
cnt = 0
while (cnt<len(myNumList)):
     if myNumList[cnt] > temp:  # 100 200 999
         temp = myNumList[cnt]
     cnt += 1
print(f'리스트의 최댓값은? {temp}')

# 리스트의 요소중에서 최댓값을 삭제하기
temp = myNumList[0]
cnt = 0
while (cnt<len(myNumList)):
     if myNumList[cnt] > temp:  # 100 200 999
         temp = myNumList[cnt]
     cnt += 1
print(f'리스트의 최댓값은? {temp}')
myNumList.remove(temp)
print(f'리스트에서 최댓값 삭제 후 => {myNumList}')



### 퀴즈 ###
# 아래의 리스트에서 가장 큰 수와 가장 작은 수를 삭제하여라
# while 문 이용
myNumList = [100, 200, 50, -30, 999, 10, 1000, 6732 ]
temp = myNumList[0]
tem = myNumList[0]
cnt = 0
while (cnt<len(myNumList)):
     if myNumList[cnt] > temp:
         temp = myNumList[cnt]
     elif myNumList[cnt] < tem:
         tem = myNumList[cnt]
     cnt += 1
print(f'리스트의 최댓값은? {temp}')
myNumList.remove(temp)
print(f'리스트의 최소값은? {tem}')
myNumList.remove(tem)
print(f'리스트에서 최대,최소값 삭제 후 => {myNumList}')




### break ###
# 반복문 안에서 사용
# 명령문 실행시 제어문에서 탈출한다.
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.
# 무한루프의 종료 조건시 사용


# while 무한루프
# while True:
#   print('Hello Python')

# 1~10 까지 출력 (무한루프 + break)
cnt = 1
while True:
    print(cnt)
    if cnt >= 10:  # while 문 탈출 조건문
        break
    cnt += 1
print('무한루프 테스트 종료')



# X 또는 x 를 입력하면 종료
while 100:
    ans = input('입력 >> ').strip()
    if ans.lower() == 'x':
        print('입력종료합니다.')
        break
print('무한루프 테스트 종료')



### continue ###
# 제어문 안에서 사용
# 명령문이 실행되면 하단 명령문들은 실행되지 않는다.

# 1~10 사이의 숫자중에서 홀수만 출력하기
# while + continue
cnt = 0
while (cnt < 10):
    cnt += 1
    if cnt %2 == 0:
        continue
    print(cnt)
print('while + continue 무한루프 테스트 종료')



# 1~10까지 숫자중에서 5만 빼고 출력하여라
print('='*30)
cnt = 0
while (cnt < 10 ):
    cnt += 1
    if (cnt == 5):
         continue
    print(cnt, end = ' ')
print('\nwhile + continue 테스트 종료!!!!')



# 다중 while 문
# while 조건1:
#   while 조건2:
#       명령문2
#   명령문1


# 점선 출력후 문단 3번찍기 n번 반복하기
# 점선 출력
cnt1 = 1
while cnt1 <= 5:
    print(cnt1, end = ' ')
    print('='*30)
    cnt1 += 1

# 점선 1번 출력시 문단은 3번 출력
cnt1 = 1
while ( cnt1 <= 5):
     print(cnt1, end = ' ')
     print('='*20)

     cnt2 = 1  # 내포된 while문의 초기화
     while ( cnt2 <= 3) :
         print(f'\t {cnt2} Hello world')
         cnt2 += 1

     cnt1 += 1




# 2~9단 출력하기
'''
   2 단 
2 X 1 = 2
..
2 X 9 = 18  
...


   9 단 
9 X 1 = 9
..
9 X 9 = 81 

'''

xx = 2
while xx <= 9:
    print(f'\n{xx} 단')

    x = 1
    while x <= 9:
        print(f'{xx} X {x} = {xx*x}')
        x += 1
    xx += 1
print("구구단 끝")

'''
i = 2
while(i <= 9):
    print(f'\n{i:>5} 단')
    print("="*10)
    j = 1
    while(j <= 9):
        print(f'{i} X {j} = {i*j}')
        j+=1
    i += 1

'''




### for 문 ###

# range(start, end , step)
# start~ (end-1)까지 step만큼 차례대로 숫자 생성
# range 객체로 생성되므로
# 실제 출력을 확인하려면 리스트, 튜플, 집합 형태로 자료형 변경

# list( range(start, end , step) )
# : 순차적으로 숫자로 구성된 리스트
# tuple( range(start, end , step) )
# : 순차적으로 숫자로 구성된 튜플
# set( range(start, end , step) )
# : 순차적으로 숫자로 구성된 집합



# 1~10 까지 숫자로 구성된 리스트 생성
# [ 1, 2, 3, ... , 10 ]
# range 객체
print(range(1, 11)) # range(1, 11)
print(list(range(1, 11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1, 101)))



# 15~1 까지 숫자로 구성된 튜플 생성
t1 = range(15, 1, -1)
print(t1, type(t1)) # range(15, 1, -1) <class 'range'>
t1 = tuple(range(15, 0, -1))
print(t1, type(t1)) # (15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1) <class 'tuple'>



# 20이하의 짝수로 구성된 집합 생성
s1 = range(2, 21, 2)
print(s1, type(s1)) # range(2, 21, 2) <class 'range'>
s1 = set(range(2, 21, 2))
print(s1, type(s1))



# for 문과 range
# for 인덱스변수 in range(start,end,step):
#   명령문


# 1~10까지 출력하기
for i in range(1,11):
    print(i)


# 1~10까지 홀수만 출력하기
for i in range(1,11,2):
    print(i, end = ' ')


# 1~20까지 짝수만 출력하기
for i in range(2,21,2):
    print(i, end = ' ')

for i in range(20,1,-2):
    print(i, end = ' ')


# 1~100사이의 합 구하기
# 1 + 2 + ... + 100
result = 0
for i in range(1, 101):
    # print(i)
    result += i # 1 + 2 + 3 ... +100
print(f' 1 + 2 + ... + 100 = {result}')


# 1~10 모두 곱한 값 구하기
# 1x2X...X10 = ?


# for + if 문
# 1~25 까지 한줄에 5개씩
for i in range(1, 26):
    print(i, end = '  ')
    if i %5 == 0:
        print()


# 1~20 사이의 숫자중에서 5의 배수만 제외하고 출력하기
# for .. in range + if + continue
for i in range(1,24):
    if i %5 == 0:
        continue
    print(i, end='  ')




# 다중 for문과 range()
'''
for i in range(start, end):
    명령문
    for j in range(start, end):
        명령문
'''


# 점선 출력후 문단 3번찍기 5번 반복하기
# 점선 1번 출력시 문단은 3번 출력
print('\n'*2)
# start 값이 0인 경우 생략 가능 : range(end)
for i in range(5):
    print(i+1, '='*15)
    for j in range(3):
        print('\t', j + 1, '안녕하세요')



# 퀴즈 : 다중 for 문을 이용하여 구구단 출력
'''
   2 단 
2 X 1 = 2
..
2 X 9 = 18  
...


   9 단 
9 X 1 = 9
..
9 X 9 = 81 

'''
print('=' * 30)
for i in range(2, 10):
    print(f'\n{i:>4}단')
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')





# 자료형의 각 요소 값을 순차적으로 출력
# for 인덱스변수 in 리스트,문자열,튜플:
#   명령문

# 동네 리스트를 생성하고 아이템을 출력하여라
cityList = ['구로동', '신림동', '서초동', '역삼동']
for item in cityList:
    print(item)

cnt = 0
while (cnt<len(cityList)):
    print(cityList[cnt])
    cnt += 1



# 동네 리스트를 생성하고 아래와 같은 형태로 출력하여라 (for ... in 이용)
cityList = ['구로동', '신림동', '서초동', '역삼동', '명동']
'''
1 구로동
2 신림동
3 서초동
4 역삼동
5 명동
'''
count = 1
for item in cityList:
    print(f'{count}. {item}')
    count += 1



# for ... in + 문자열
txt = '도래미파솔라시'
for c in txt:
    print(c)

count = 1
for c in txt:
    print(f'{count} : {c}')
    count += 1

# 사선출력
count = 1
for c in txt:
    print(" "*count, count, c)
    count += 1



# 퀴즈 : 다음 튜플의 평균과 합 구하기
t2 = (100, 56, 45, 89, 90)
total = 0
for item in t2:
    print(item)
    total += item
print(f' 총합은? {total}, 평균은? {total/len(t2):.2f}')



# for 를 이용한 딕셔너리 요소 출력
# for 키변수 in 딕셔너리:
#   명령문
myDict = {1:'일', 100:'백', 50:'오십', 1000:'천'}
# print(myDict[1]) # 1

for key in myDict:
    print(key)

for key in myDict:
    # 키와 값 출력
    print(key, ' => ', myDict[key])



# for ... in 리스트 + if 조건문
# 시험 점수에서 60점 이상이면 합격 그렇지 않다면 불합격
score = [ 55, 45, 65, 90, 77]
count = 1
for i in score:
    if (i >= 60) :
        print(f'{count} 번째 학생 :  {i} : 합격')
    else :
        print(f'{count} 번째 학생 :  {i} : 불합격')
    count += 1



# 퀴즈
# for key in ~ + if 조건문 + in 연산자
# 딕셔너리 값에 'a' 글자가 있는 아이템만 표시하고 총 갯수를 출력하여라
myDict = {'a': 'africa', 's': 'say','c': 'coffee', 'd': 'drama', 'y':'yes'}

for key in myDict:
    print(f'키값은? {key}   데이터 값은? {myDict[key]}')

for key in myDict:
    if 'a' in myDict[key]:
        print(f'키값은? {key}   데이터 값은? {myDict[key]}')
        count += 1
print(f' 총 개수는? {count}')



# 다중 리스트 / 다중 튜플 과 for
# 리스트/튜플 안에 삽입되어 있는 리스트의 갯수가 같아야 한다.
# for (i, j...) in 다중리스트:
#   명령문

List_2d = [[1, 2], ['a', 'b'], ['홍길동', '춘향이']]
print(List_2d)
print(list_2d[2][0]) # 홍길동
print(list_2d[-1][-1]) # 춘향이

for (i, j) in List_2d:
    print(f' i => {i}     j => {j}')



# 퀴즈
# 학생이름, 국어, 영어, 수학 으로 구성된
# 2차원 리스트를 생성한다.
# 출력형식은 아래와 같이 한다.
'''
학생이름  국어  영어  수학  합계  평균
김태희     30   40   100   ?     ?
...

'''

# 5행 4열의 리스트 정의
stGradeList = [['김태희', 30, 50, 55],
               ['신민아', 50, 90, 80],
               ['박지민', 50, 90, 40],
               ['김소희', 60, 50, 56],
               ['윤준희', 90, 88, 66]]

print('-'*40)
print(' 이름  국어  영어  수학   총점    평균')
print('-'*40)
for (stName, i, j, k) in stGradeList:
    print(f'{stName}  {i}   {j}    {k}   {i+j+k}   {((i+j+k)/3):.2f}')






