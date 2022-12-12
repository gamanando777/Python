

# 파일입출력함수
# data.zip 파일을 다운로드한 후
# 작업폴더(예:pythonClass)안에 data 폴더에 압축해제
# 하위 폴더 data 확인




import os

# 현재 작업폴더 표시
print(os.getcwd())  # 파일이 저장된 위치 표시

# 작업폴더 안의 파일과 목록
print(os.listdir())
# 디렉토리 위치 변경
os.chdir('data')
print(os.getcwd())
print(os.listdir())
# 상위 디렉토리 위치 변경
os.chdir('..')
print(os.getcwd())
print(os.listdir())





# 파일입출력
# 파일변수  = open(파일경로, 'r'/'w'/'a',
#                    encoding='utf-8/cp949')
# 파일변수.파일입출력함수(옵션)

# 파일읽기
# 파일변수 생성
# 파일변수  = open(파일경로, 'r',
#                     encoding='utf-8/cp949')
# 파일변수.read() : 파일전체 문자열 구조 =>  문자열
# 파일변수.readline() : 파일에서 첫줄만 읽기 => 문자열
# 파일변수.readlines() : 각행이 리스트 구조로 변경 => 리스트


# data/yesterday.txt
# 파일 변수 생성
f = open('data/Yesterday.txt','r',encoding='utf-8')
# 전체 파일을 읽어 data변수에 저장
data = f.read()
print(data)
# 파일 닫기
f.close()

print(os.getcwd())  # 현재 파이썬에서 인식하는 폴더 위치
print(os.listdir())  # 폴더 안의 data list확인

print(type(data))  # <class 'str'>


# data/coding.txt
f = open('data/coding.txt','r', encoding='utf-8')
data2 = f.readline()  # 첫번째 행만 읽어서 저장
f.close()
print(data2)
print(type(data2))  # <class 'str'>


# data/sample.txt
f = open('data/sample.txt','r', encoding='cp949')
data3 = f.readlines()  # 리스트로 불러오기
f.close()
print(data3)
print(type(data3))  # <class 'list'>

# 5행만 출력
for row in range(5):
    print(f'{row+1} => {data3[row]}')

# data3 리스트 안의 '\n' 삭제
result = []
for row in data3:
    if row != '\n':
        result.append(row.rstrip())
print(result)

for row in range(10):
    print(f'{row+1} => {result[row]}')




## 퀴즈 : 파일의 단어전체수와 3개의 단어만 출력하기
# ******************************
# 파일명 :  data/Yesterday.txt
# 단어 갯수 :  134
# 단어 3개 출력
# ['Yesterday', 'All', 'my']

f = open('data/Yesterday.txt','r',encoding='utf-8')
data = f.read()
print(data)
f.close()

result = data.split()  # 공백을 기준으로 단어  분리 => 리스트
print(result[:3])
print(f'단어 개수는? {len(result)}')
print(f'Yesterday ?  {result.count("Yesterday")}')

# 중복 단어는 제거
result2 = list(set(data.split()))
print(f'단어 개수는? {len(result2)}')
print(f'Yesterday ?  {result2.count("Yesterday")}')
result2.sort()
print(result2)






## 퀴즈
# data_eng.txt, data_kor.txt
# 파일안의 데이타의 합과 평균을 구하는
# 함수를 정의하고 아래와 같이 출력하여라
# 함수 정의 => 파일읽기 => 리스트화
# => 리스트의 값 더하기(숫자형데이터로 변환) : 합
# => 합 / 리스트갯수 : 평균

'''
# 함수 호출
sumAvr('data/data_eng.txt', 'cp949')
sumAvr('data/data_kor.txt', 'cp949')

>> 결과

파일명 =  data/data_eng.txt
데이터 수 =  12
합 =  933
평균 = 77.75

----------
파일명 =  data/data_kor.txt
데이터 수 =  12
합 =  892
평균 = 74.33

'''
def sumAvr(add,type):
    f = open(add, 'r', encoding = type)
    data = f.read()
    f.close()
    data2 = data.split()
    sa = []
    for score in data2:
        sa.append(int(score))
    print(f'파일명 = {add}')
    print(f'데이터 수 = {len(data2)}')
    print(f'합 = {sum(sa)}')
    print(f'평균 = {sum(sa)/len(sa):.2f}')


sumAvr('data/data_eng.txt', 'cp949')
sumAvr('data/data_kor.txt', 'cp949')



'''
import statistics

def sumAvr(file, op):
    f = open(file, 'r', encoding=op)
    data = f.readlines()
    f.close()

    scorelist = []
    for i in data:
        if i != '\n':
            scorelist.append(int(i))
    # scorelist = list(map(lambda n: int(n), data))

    print('='*30)
    print(f'파일명 = {file}')
    print(f'데이터 수 = {len(scorelist)}')
    print(f'합 = {sum(scorelist)}')
    # print(f'평균 = {sum(scorelist)/len(scorelist):.2f}')
    print(f'평균 = {statistics.mean(scorelist):.2f}')
sumAvr('data/data_eng.txt', 'cp949')
sumAvr('data/data_kor.txt', 'cp949')

'''

# 출력용 폴더 생성
# os.mkdir('폴더명')
# 명령 한번만 실행. 다시 실행하면 이미 동일한 이름의 폴더가 존재하기 때문에 오류남.
os.mkdir('output')
print(os.listdir())






### 파일 쓰기 ###
# 새로운 파일이 생성되면서 내용이 추가된다.
# 기존에 파일이 있다면 덮어쓰기된다.
# 파일변수 = open( 생성파일경로, 'w', encoding='cp949/utf-8')
# 파일변수.write(문자열)
# 파일변수.close()

# 1~10 까지 숫자 저장 => output/number.txt
f = open('output/number.txt', 'w', encoding='utf-8' )
f.write('='*30)
for i in range(1, 11):
    f.write('\n'+str(i))
f.close()



# 구구단을 파일로 저장하기 => output/gugudan.txt
f = open('output/gugudan.txt','w',encoding='utf-8')

for i in range(2,10):
    f.write('\n')
    f.write('=' * 30)
    f.write(f'\n\n {i:>5}단')
    for j in range(1,10):
        f.write(f'\n {i}X{j}={i*j}')
f.close()






# 내용추가하기
# 기존 파일에 내용이 추가된다.
# 파일변수 = open( 생성파일경로, 'a', encoding='cp949/utf-8')
# 파일변수.write(문자열)
# 파일변수.close()

# 빈파일 생성하기 => output/test.txt
f = open('output/test.txt','w', encoding='utf-8')
f.close()

f = open('output/test.txt','a', encoding='utf-8')
f.write('테스트 시작')
f.close()

f = open('output/test.txt','a', encoding='utf-8')
for n in range(1,6):
    f.write(f'\n {n} 행입니다')
f.close()





### with 문과 파일 입출력
# 파일.close() 를 사용할 필요가 없다.
# with open(파일경로, 'a'/'w'/'r', encoding='uft-8/cp949') as 파일변수:
#   명령문


# data/national_anthem.txt => 리스트 저장
with open('data/national_anthem.txt', 'r', encoding='cp949') as f:
    data = f.readlines()
print(data[:5])
print(len(data))

# 리스트 저장 => output/anthem.txt
with open('output/anthem.txt', 'w', encoding='utf-8') as f:
    for row in data[:10]:
        f.write(row)

# 내용 추가 => output/anthem.txt
with open('output/anthem.txt', 'a', encoding='utf-8') as f:
    for row in data[15:]:
        f.write(row)




## 퀴즈 8
# 파일읽기, 쓰기, 추가 기능을 이용하여 다음과 같은 프로그램을 작성하여라.
# 파일에 추가되는 단어의 글자수는 2글자로 제한한다.

'''
# 프로그램 예시 
------------------------------
메뉴 번호를 입력하세요. 1.단어추가 2.모두읽기 3.모두삭제 4.종료 ...  1

[단어 추가]
두 글자로 구성된 단어를 입력하세요... 송아지
두글자가 아닙니다.
두 글자로 구성된 단어를 입력하세요... 사과
단어가 저장되었습니다.

------------------------------
메뉴 번호를 입력하세요. 1.단어추가 2.모두읽기 3.모두삭제 4.종료 ...  1

[단어 추가]
두 글자로 구성된 단어를 입력하세요... 자두
단어가 저장되었습니다.

------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료  ...  2

[단어 모두 출력]
총 단어 수 ... 2 
사과
자두


------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료  ...  3

[파일 내용 모두 삭제]
단어 목록을 모두 삭제하였습니다.


메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료  ...  2

[단어 모두 출력]
총 단어 수 ... 0 

------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료  ...  4

프로그램을 종료합니다.
'''

# 예제를 위한 파일 생성
with open('output/word.txt', 'w', encoding='utf-8') as f:
    f.write('')


while True:
    print('='*50)
    choice = input('메뉴 번호를 입력하세요 \n'
                   '1. 단어추가 \n'
                   '2. 모두 읽기 \n'
                   '3. 모두 삭제\n'
                   '4. 종료').strip()
    if choice == '1':
        print('[단어 추가]')
        while True:
            word = input('두 글자로 된 단어를 입력하세요...').strip()
            if len(word) == 2:
                with open('output/word.txt','a',encoding='utf=8') as f:
                    f.write(word+'\n')
                    f.close()
                print('단어가 저장되었습니다.')
                break
            elif len(word) != 2:
                print('두글자가 아닙니다.')


    elif choice == '2':
        print('[단어 모두 출력]')
        with open('output/word.txt','r',encoding='utf=8') as f:
            data = f.readlines()
        print(f'총 단어 수... {len(data)}')
        for i in data:
            print(i.rstrip())

    elif choice == '3':
        print('[파일 내용 모두 삭제]')
        with open('output/word.txt','w',encoding='utf=8') as f:
            data = f.write("")
        #print(f'총 단어 수... {len(data)}')
        print('단어 목록을 모두 삭제하였습니다.')

    elif choice == '4':
        print('프로그램을 종료합니다.')
        break






### 모듈이란? ###
# 파이썬 파일 단위
# 다른 파일안에 저장된 변수나 함수를 사용하는 기능
# 사용자정의 모듈
# 빌트인 모듈, install 해서 사용하는 모듈

# 모듈의 호출방법 1
# import 모듈이름
# 모듈이름.함수(인자)

# 모듈의 호출방법 2
# import 모듈이름 as 별칭
# 호출된 모듈의 함수 호출방법2
# 별칭.함수(인자)

# 모듈의 호출방법 3
# from 모듈이름 import 모듈함수
# 호출된 모듈의 함수 호출방법3
# 모듈함수(인자)


# import 모듈이름
# 모듈이름.함수(인자)
import math
print(math.pi) # 3.141592653589793

# import 모듈이름 as 별칭
import math as m
print(m.pi) # 3.141592653589793

# from 모듈이름 import 모듈함수나속성
# 모듈함수(인자) 나 속성
from math import pi
print(pi) # 3.141592653589793



# 함수 < 클래스 < 모듈 < 패키지
# 사용자 정의 모듈 만들기
# 별도 파일에 함수를 정의한다.
# 함수를 사용할 파일에서 import 파일명 연결

# import 파일명
import hello
hello.print_msg()


