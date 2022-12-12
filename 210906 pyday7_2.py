# 데이터 획득 방법
# 공공 데이터 - jsion, xml, csv, tsv, dat, xls
# 캐글 데이터 - csv
# WEB 스크래핑
# 유료 데이터 (X)

# csv, tsv, dat, xls, json, xml, html => 2차원리스트, 딕셔너리 리스트
# openAPI => json, xml
# 데이타수집 => 데이타가공 => 데이타분석 => 예측(머신러닝)






#############
### CSV란? ###
# Comma Seperate Value
# 콤마(,)로 데이타가 분리된 파일

### TSV란? ###
#############
# Tab Seperate Value
# 공백으로 데이터가 분리된 파일


# 관련 모듈 import
import csv
import os

# data.csv 파일이 data 폴더안에 있는지 확인
# print(os.getcwd())
# os.chdir('data') #cd data
# print(os.getcwd())
# print(os.listdir())
# print('data.csv' in os.listdir())
# os.chdir('../')
# print(os.getcwd())





# CSV 파일 읽기 1
# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.reader(파일변수)
# 파일변수.close()
import csv
f = open('data/data.csv','r')
csv_data = csv.reader(f)
# print(csv_data,type(csv_data))
# <_csv.reader object at 0x0000022E0FD28D00> <class '_csv.reader'>

# 리스트 구조로 변환
data_list = []
for i in csv_data:
    data_list.append(i)
f.close()

print(data_list)
print(len(data_list))  # 13
print(data_list[0])  # 컬럼의 제목
print(data_list[1:])  # 실제 데이터
print('='*50)
for ban, name, kor, eng, mat, bio in data_list[1:]:
    print(ban, name, kor, eng, mat, bio)

# 데이타는 모두 문자열 형태
print(data_list[-1][-1], type(data_list[-1][-1]))
# 78 <class 'str'>


# kor 과목의 총합과 평균을 구해라
kor_list = []
for ban, name, kor, eng, mat, bio in data_list[1:]:
    kor_list.append(int(kor))
print(kor_list)
print(f'kor 과목의 총점: {sum(kor_list)}, kor 과목의 평균 : {sum(kor_list)/len(kor_list)}')






# 퀴즈1 :
# 4과목('kor', 'eng', 'mat', 'bio')의 총점 구하기
sub_list = []
for ban, name, kor, eng, mat, bio in data_list[1:]:
    sub_list.append(int(kor))
    sub_list.append(int(eng))
    sub_list.append(int(mat))
    sub_list.append(int(bio))
print(sub_list)
print(f'4과목의 총점: {sum(sub_list)}')


# 퀴즈2 :
# 전체 평균 구하기
print(f'4과목의 평균: {sum(sub_list)/len(sub_list):.2f}')



# 퀴즈3 :
# 국어 점수의 최고점을 받은 학생의 이름은?
# 알고리즘
# 국어점수의 최고점을 구한다. max()
# 최고점의 인덱스를 구한다. 리스트이름.index()
# 인덱스를 학생이름인덱스에 삽입한다.


no1 = kor_list.index(max(kor_list))
print(data_list[no1+1][1])


print(f'국어 점수 최고점 : {max(kor_list)} \n최고점 학생 : {data_list[kor_list.index(max(kor_list))+1][1]}')



# CSV 파일 읽기 2
# with open('csv파일경로', 'r', encoding='utf-8/cp949') as 파일변수
#   csv객체변수 = csv.reader(파일변수)

with open('data/population.csv','r') as f:
    csv_data = csv.reader(f)
    # 리스트 구조로 변환
    data_list = []
    for i in csv_data:
        data_list.append(i)

print(data_list)
print(len(data_list))  # 52
f.close()

# 5개의 행만 출력
for s,p in data_list[1:6]:
    print(s,p)


# 퀴즈0. 인구컬럼만 정수리스트로 새로 만들어라
    # '4,780,131' => 4780131
# 문자열.replace(old,new)
pop_list = []
for s,p in data_list[1:]:
    pop_list.append(int(p.replace(',','')))
print(pop_list)

    # 퀴즈1 . 가장 많은 인구수는? max()
print(f'가장 많은 인구 수는? ... {max(pop_list)}')

    # 퀴즈2 . 가장 작은 인구수는? min()
print(f'가장 작은 인구 수는? ... {min(pop_list)}')

    # 퀴즈3. 가장 인구가 많은 주(State)는?
print(f'가장 인구가 많은 주는?... {data_list[pop_list.index(max(pop_list))+1][0]}')

    # 퀴즈4. 가장 인구가 적은 주(State)는?
print(f'가장 인구가 많은 주는?... {data_list[pop_list.index(min(pop_list))+1][0]}')






# ordered dict 형태로 데이터 불러오기

# 파일변수 = open('csv파일경로', 'r', encoding='utf-8/cp949')
# csv객체변수 = csv.DictReader(파일변수)
# 파일변수.close()

# with open('csv파일경로', 'r', encoding='utf-8/cp949') as 파일변수:
#   csv객체변수 = csv.DictReader(파일변수)

with open('data/data.csv', 'r') as f:
    csv_data = csv.DictReader(f)
    for row in csv_data:
        print(row)

# 2번째 부터의 실제 데이타행은 딕셔너리 형태로 입력된다.
# 1번째 행은 키가된다.
# {'class': '1', 'name': 'adam', 'kor': '67', 'eng': '87', 'mat': '90', 'bio': '98'}

# 딕셔너리 리스트 구조로 변경
with open('data/data.csv', 'r') as f:
    csv_data = csv.DictReader(f)
    data_list = []
    for row in csv_data:
        data_list.append(row)

print(data_list[:3])
print('*'*20)
for row in data_list[:5]:
    print(row)

print('*'*20)
for row in data_list[:5]:
    for key in row:
        print(key, '=>', row[key])
    print('='*20)

# bio 점수만 리스트로 생성하여라
print('*'*20)
bio_list = []
for row in data_list:
    for key in row:
        print(key, '=>', row[key])
    print('='*20)




# csv 파일 쓰기1
# 파일변수 = open('csv파일경로', 'w', encoding='utf-8/cp949', newline='')
# csv객체변수 = csv.writer(파일변수)
# csv객체변수.writerow(리스트/튜플...)
# 파일변수.close()

# csv 파일 쓰기2
# with open('csv파일경로', 'w', encoding='utf-8/cp949', newline='') as 파일변수:
    # csv객체변수 = csv.writer(파일변수)
    # csv객체변수.writerow(리스트/튜플...)


# 2차원 리스트 => output 폴더안에 csv 파일로 저장
# 폴더 생성
import os
import csv

try:
    os.mkdir('output2')
except:
    pass
else:
    print('폴더 생성완료')


# 2차원 리스트 => output 폴더안에 csv 파일로 저장
# 2차원 리스트
data_list = [ ['이름','주소','전화번호'],
['김영희','부산시','010-6374-90874'],
['홍길동','춘천시','010-5463-9403'],
['성은희','서울시','010-4646-9403'] ]

# 각 리스트가 셀 하나에 삽입된다.
f = open('output/address.csv', 'w', encoding= 'cp949')
csv_data = csv.writer(f)
csv_data.writerow(data_list)
f.close()

# newline='' 옵션을 제거할 경우 중간중간 빈 행이 삽입됨.
f = open('output/address.csv', 'w', encoding= 'cp949',newline='')
csv_data = csv.writer(f)
for row in data_list:
    csv_data.writerow(row)
f.close()



# 내용추가
f = open('output/address.csv', 'a', encoding= 'cp949',newline='')
csv_data = csv.writer(f)
csv_data.writerow(['은지원','서울시','010-1234-9999'])
csv_data.writerow(['고길동','서울시','010-1234-9999'])
f.close()





# csv 파일 쓰기
# 딕셔너리 => csv 파일
# with open('csv파일경로', 'w', encoding='utf-8/cp949', newline='') as 파일변수:
    # field_list = 리스트(딕셔너리의 키로 생성된 리스트)
    # csv객체변수 = csv.DictWriter(파일변수, fieldnames=field_list)
    # csv객체변수.writerheader()
    # csv객체변수.writerow(딕셔너리)
    # csv객체변수.writerows(딕셔너리 리스트)


# 딕셔너리 리스트 정의
dict_list = [ {'name':'김영희','address':'부산시','mobile':'010-6374-90874'},
{'name':'홍길동','address':'춘천시','mobile':'010-5463-9403'},
{'name':'성은희','address':'서울시','mobile':'010-4646-9403'} ]

# 한줄
with open('output/address2.csv','w',newline='') as f:
    csv_data = csv.DictWriter(f,fieldnames=['name','address','mobile'])
    csv_data.writerow({'name':'김영희','address':'부산시','mobile':'010-6374-90874'})

# 여러줄
with open('output/address2.csv','w',newline='') as f:
    csv_data = csv.DictWriter(f,fieldnames=['name','address','mobile'])
    for row in dict_list:
        csv_data.writerow(row)

with open('output/address3.csv', 'w', newline='', encoding='utf-8') as f:
    csv_data = csv.DictWriter(f, fieldnames=['name','address', 'mobile'])
    # 제목행  저장
    csv_data.writeheader()
    csv_data.writerows(dict_list)



##################################
### pandas를 이용한 csv 파일 읽기 ###
##################################

import pandas as pd
import numpy as np

# csv파일 읽어서 데이터프레임으로 저장
# 데이터프레임이란?
# pandas에서 제공하는 테이블 구조
# 판다스에서 제공하는 테이블 구조
# 데이타프레임변수 = pd.read_csv(csv파일경로, encoding='cp949/utf-8')

df = pd.read_csv('data/data.csv')
print(df)


# 행단위로 read
# 데이타프레임.head(n)
# 데이타프레임.tail(n)

# 3개의 행만 출력
print(df.head(3))

# 마지막행 출력
print(df.tail(1))

# 컬럼단위로 read
# 컬럼 1개만
# 데이터프레임명[컬럼명] : 컬럼명이 문자열이면, 따옴표 사용
# 데이터프레임명.컬럼명
print(df['name'])
print(df.kor)

# 2개 이상인 경우 컬럼 위주로 추출
# 데이터프레임명[[컬럼명1, 컬럼명2...]]
print()
print(df[['name','kor','eng']])

# 영어점수만 => 리스트로 저장
eng_list = df['eng']
print(list(eng_list))



# 행단위
# 데이타프레임.loc[start:end]
# : 행이름 접근. start~end
# 데이타프레임.iloc[startIndex:endIndex]
# : 행인덱스로 접근. start~end-1 인덱스까지
print()
print(df)
print()
#
print(df.loc[1:3])
print()
print(df.iloc[1:4])



# 컬럼단위
# 데이타프레임.loc[start:end, start:end]
# 데이타프레임.loc[:, start:end]
# : 행이름, 컬럼이름 접근. start~end

# 데이타프레임.iloc[startIndex:endIndex, startIndex:endIndex]
# : 행인덱스 또는 컬럼인덱스로 접근. start~end-1 인덱스까지

# 행에 상관없이 특정컬럼을 추출해서 출력
print(df.loc[:,'kor':'mat'])
print(df.iloc[:,2:5])

# 특정행의 특정컬럼을 추출해서 출력
print(df.loc[6:8,'name':'eng'])
print(df.iloc[6:9,1:4])


# 데이터프레임 => csv로 저장
# name, kor, eng => output/data2.csv
# 데이타프레임.to_csv(파일경로, header=None, index=False)
df[['name','kor','eng']].to_csv('output/data2.csv', header=None, index=False)


###############
### 엑셀 활용 ###
###############
import pandas as pd
import numpy as np
import openpyxl

# 엑셀 파일 => 데이터프레임
# data/TrafficAccident2019.xlsx
# 데이터프레임 변수 = pd.read_excel(파일경로,encoding='cp949'/'utf-8')
df = pd.read_excel('data/TrafficAccident2019.xlsx')
df = pd.read_excel('data/TrafficAccident2019.xlsx',skiprows=3,header=None) # 실제 데이터 시작은 4행부터
print(df)

# 컬럼명 재설정
df.columns = ['시도','발생건수','대형사고','여객건','화물건','사망자수','치사율']
print(df)


# 엑셀 파일로 저장
# 데이터프레임.to_excel(파일명, index=False)
print(df[['시도','발생건수']])

import xlwt
df[['시도','발생건수']].to_excel('output/traffic.xls', index=False)



