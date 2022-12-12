


# 필드 = 속성 = 변수
# 사각형과 관련된 필드 =>  가로, 세로, 색상, 무늬
# 빵과 관련된 필드 =>  재료, 브랜드, 칼로리, 생성날짜
# 수강생과 관련된 필드 =>  이름, 성별, 주소, 연락처, 나이 ...
'''
# 생성자 메서드 : 속성 정의
class 클래스이름:
    def __init__(self, 인자):
        self.필드 = 인자
'''

'''
# 생성자 메서드 호출 : 속성값 전달 
인스턴스명 = 클래스명(인자값...) 

# 인스턴스 속성 접근 
인스턴스명.속성 
'''

# 사각형 클래스 정의
# 속성 : 가로, 세로, 색상, 만든이(홍길동, 둘리)
# 메서드 (동작, 기능) => 사각형 정보, 사각형 넓이
class Square:
    # 생성자 메서드(=함수) 정의
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        # 초기값이 있는 속성
        self.maker = ('홍길동', '둘리')
    # 사각형 정보를 출력시키는 메서드 정의
    def info(self):
        print(f'가로: {self.width} 세로: {self.height}')
        print(f'색상: {self.color}')
        print(f'만든이: {self.maker[0]}과 {self.maker[1]}')

    # 사각형의 넓이값을 반환하는 메서드 정의
    def area(self):
        return self.width*self.height



# 클래스 => 인스턴스(객체화)
# 인스턴스명 = 클래스명(인자값...)
square1 = Square(30,30,'red')
square2 = Square(50,20,'blue')

# 인스턴스.속성명 탐색
print(f'square1 => 가로 {square1.width}  세로 {square1.height} 넓이 {square1.width*square1.height}')
print(f'square2 => 가로 {square2.width}  세로 {square2.height} 넓이 {square2.width*square2.height}')
print(f'square1 => 색상 {square1.color}  square2 => 색상 {square2.color}')
print(f'사각형 만든 사람 => {square1.maker}')

# 정의된 메서드 테스트
square3 = Square(100,200,'skyblue')
square3.info()
print('넓이는?',square3.area())




# Bread 클래스
# 속성 => 빵이름, 가격, 브랜드, 생성날짜
# 매서드 => 빵 정보 출력, 주문한 빵 갯수에 따라 가격이 출력

class Bread:
    # 생성자 메서드 정의
    def __init__(self, kind, price, make_date):
        self.brand = '뚜레쥬르'
        self.kind = kind
        self.price = price
        self.make_date = make_date

    # 정보 출력 메서드
    def info(self):
        print(f'이름: {self.kind}')
        print(f'가격: {self.price}')
        print(f'날짜: {self.make_date}')
        print(f'브랜드: {self.brand}')

    # 가격 출력 메서드 정의
    def price_info(self, n):
        print('=' * 30)
        print(f' 주문 정보 => {self.kind} 를 {n} 개 주문')
        print(f' 주문 가격 => {self.price * n} ')

# Bread 클래스의 객체화
bread1 = Bread('우유식빵', 3300, '2021-09-03 AM 10:30')
bread2 = Bread('모카빵', 1500, '2021-09-02 PM 8:30')

# 메서드 호출
bread1.info()
bread2.info()

bread1.price_info(6)
bread2.price_info(3)




## 퀴즈 2
# Cat 클래스를 만들고 인스턴스한 후 메서드를 호출하여라
# 속성 : kind, name, age, gender, animal_kind(고양이)
# 메서드 :  속성출력(print_info), 동작 : run, sleep(어디서), eat(무엇을)

# 인스턴스화 예)
# cat1 = Cat('코캣', '덩치', 1, '남')
# cat2 = Cat('러시안블루', '나비', 5, '여')
'''
# cat1.print_info()
 종류 = 러시안블루
 이름 = 나비
 나이 = 5
 성별 = 여

# cat1.run()
고양이 덩치 가 달린다.
# cat2.run()
고양이 나비 가 달린다.
# cat1.sleep('캣타워')
고양이 덩치가 캣타워에서 잔다.
# cat2.sleep('캣타워')
고양이 나비가 택배 박스에서 잔다.
# cat1.eat('사료')
고양이 덩치가 사료을(를) 먹는다.
# cat2.eat('춥스')
고양이 나비가 춥스을(를) 먹는다.

'''

class Cat:
    def __init__(self,kind, name, age, gender):
        self.kind = kind
        self.name = name
        self.age = age
        self.gender = gender
        self.animal_kind = '고양이'

    def print_info(self):
        print(f'종류: {self.kind}')
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')
        print(f'성별: {self.gender}')

    def run(self):
        print(f'{self.animal_kind} {self.name}가 달린다.')

    def sleep(self,n):
        print(f'{self.animal_kind} {self.name}가 {n}(에)서 잔다.')

    def eat(self,n):
        print(f'{self.animal_kind} {self.name}가 {n}을/를 먹는다.')

     # 기존에 정의된 메서드를 이용해서 새로운 메서드로 정의
    def action(self):
        print('=' * 50)
        print(f'{self.animal_kind} {self.name} 의 아침 ')
        self.eat('물')
        self.eat('사료')
        self.run()
        self.eat('통조림')
        self.eat('물')
        self.run()
        self.sleep('쇼파')


cat1 = Cat('코캣', '덩치', 1, '남')
cat2 = Cat('러시안블루', '나비', 5, '여')

cat1.run()
cat2.run()
cat1.sleep('캣타워')
cat2.sleep('캣타워')
cat1.eat('사료')
cat2.eat('춥스')

cat1.action()
'''
class Cat:
    # 생성자 함수 정의
    def __init__(self, kind, name, age, gender):
        self.animal_kind = '고양이'
        self.kind = kind
        self.name = name
        self.age = age
        self.gender = gender

    # 속성 출력 메서드
    def print_info(self):
        print(f'\n\n {self.animal_kind} 정보 출력 ')
        print('='*50)
        print(f' 종류 = {self.kind}')
        print(f' 이름 = {self.name}')
        print(f' 나이 = {self.age}')
        print(f' 성별 = {self.gender}')
        print()

    # 동작 메서드 정의
    def run(self):
        print(f'{self.animal_kind} {self.name} 가 달린다.')

    def sleep(self, where):
        print(f'{self.animal_kind} {self.name}가 {where}에서 잔다.')

    def eat(self, food):
        print(f'{self.animal_kind} {self.name}가 {food}을(를) 먹는다.')

# Cat 클래스의 인스턴스화
cat1 = Cat('코캣', '덩치', 1, '남')
cat2 = Cat('러시안블루', '나비', 5, '여')

# 메서드 호출
cat1.print_info()
cat2.print_info()
cat1.run()
cat2.run()
cat1.sleep('캣타워')
cat2.sleep('택배 박스')
cat1.eat('사료')
cat2.eat('춥스')

'''




### 클래스 변수 ###
# 클래스 정의시 사용되는 공용 변수
# 생성자 메서드 위에 보통 정의
# 인스턴스를 생성하지 않고 바로 사용
# 클래스명.클래스변수
# 인스턴스명.클래스변수

class Student:
    # 클래스 변수
    message = '개인 위생 주의...'

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def info(self):
        print('=' * 50)
        print(f' 학년 = {self.year}')
        print(f' 이름 = {self.name}')

student1 = Student('고길동',1)
student2 = Student('김철수',3)

student1.info()
student2.info()

print('student1의 이름은?', student1.name)

print('공지사항 => ', Student.message)  # 클래스명.클래스변수
print('공지사항 => ', student1.message) # 인스턴스명.클래스변수






### 클래스와 상속 ###
# 상속이란, 이미 정의되어 있는 클래스의 속성과 메서드를
# 정의하지 않고 사용할 수 있는 기능
# 다중 상속이 가능하다.
# class 클래스명(부모클래스1, 부모클래스2,...):
#          메서드
# 부모클래스 = 슈퍼클래스 = 조상클래스
# 자식클래스 = 서브클래스 = 파생클래스


# 부모 클래스 정의
class Papa:
    first_name = '김'

    def info1(self):
        print('아파트, 차')

    def city(self):
        print('서울')


class Mama:
#    def __init__(self, last_name):
#        self.last_name = last_name

    def info2(self):
        print('삼성 주식, 오피스텔')

    def city(self):
        print('부산')

    def hoometown(self):
        print('인천')

# 자식 클래스 정의
class Child(Papa, Mama):
    def __init__(self,name):
        self.name = name

    def info3(self):
        print('스쿠터')

    # 메서드 오버라이딩
    # => 부모클래스의 정의된 메서드를 재정의
    def hometown(self):
        print('의정부')

    # 부모클래스의 메서드를 사용하고 싶다면?
    # super().부모클래스메서드
    def hometown_mom(self):
        super().hometown()


# 객체화
child1 = Child('철수')
child2 = Child('영희')

print(child1.first_name, child1.name)
child1.info1()
child1.info2()
child1.info3()


# 부모클래스에서 같은 이름의 메서드가 존재한다면?
# class 선언부에서 먼저 지정한 클래스에 우선순위가 있음.
child1.city()  # 서울 - 상위 상속 클래스가 우선 상속됨.


# 부모클래스와 동일한 메서드명이 자식클래스에 존재한다면?
# 자식클래스의 우선순위가 높다.
child1.hometown()  # 의정부



# 상속관계를 확인하는 메서드
# issubclass(자식클래스명, 부모클래스명 ...)
print(issubclass(Child, Papa)) # True
print(issubclass(Child, Mama)) # True
print(issubclass(Mama, Child)) # False
print(issubclass(Mama, Papa)) # False

# 상속관계를 확인하는 속성
# 클래스명.__bases__
print(Child.__bases__)
# (<class '__main__.Mama'>, <class '__main__.Papa'>)




## 퀴즈 : 상속
# 부모 클래스 : Tiger, Lion
# 자식 클래스 : Liger

# Tiger
# 속성 : kind(호랑이)
# 메서드 : jump(점프하기), cry(어흥~)

# Lion
# 속성 : kind(사자)
# 메서드 : bite, cry(으르렁~)

# Liger
# 속성 : kind(라이거)
# 메서드 : play, jumnp(달리면서점프하기)


'''
예시>>

kind =>  라이거
라이거 : 어흥 ~
라이거 처럼 사육사와 놀기
라이거 처럼 한입에 꿀꺽하기
라이거 처럼 달리면서 점프하기~
호랑이 처럼 점프하기
'''

class Tiger:
    kind = '호랑이'
    def jump(self):
        print(f'{self.kind}처럼 점프하기')
    def cry(self):
        print(f'{self.kind} : 어흥~')


class Lion:
    kind = '사자'
    def bite(self):
        print(f'{self.kind}처럼 한입에 꿀꺽하기')
    def cry(self):
        print(f'{self.kind} : 으르렁~')



class Liger(Tiger,Lion):
    kind = '라이거'
    def __init__(self, name):
        self.name = name

    def play(self):
        print(f'{self.kind}처럼 사육사와 놀기')

    # 메서드 오버라이딩
    def jump(self):
        print(f'{self.kind} 처럼 달리면서 점프하기~')

    def jump_papa(self):
        super().jump()


'''
class Tiger:
    kind = '호랑이'
    def jump(self):
        # print(f'{self.kind} 처럼 점프하기')
        # 클래스명.변수 형태로 사용
        print(f'{Tiger.kind} 처럼 점프하기')
    def cry(self):
        print(f'{self.kind} : 어흥 ~')

class Lion:
    kind = '사자'
    def bite(self):
        print(f'{self.kind} 처럼 한입에 꿀꺽하기')
    def cry(self):
        print(f'{self.kind} : 으르렁 ~')


# class Liger(Lion, Tiger):
class Liger(Tiger, Lion):
    kind = '라이거'
    def __init__(self, name):
        self.name = name
    def play(self):
        print(f'{self.kind} 처럼 사육사와 놀기')
    # 메서드 오버라이딩
    def jump(self):
        print(f'{self.kind} 처럼 달리면서 점프하기~')

    def jump_papa(self):
        super().jump()




'''

# 인스턴화
liger1 = Liger('덩치')
print('\n'*2, liger1.name) # 덩치
print('kind => ', liger1.kind) # 라이거
liger1.cry()  # 라이거 : 어흥 ~
liger1.play()
liger1.bite()
liger1.jump() # 라이거 처럼 달리면서 점프하기~
liger1.jump_papa() # 호랑이 처럼 점프하기







