#오늘 3월 9일 수업 !!
print('hello')
print("안녕하세요")

print("%d"%10)

print("/\\")

#int, float, string, bool

var1 = 100
var2 = 3.14
var3 = "파이썬"
var4 = True

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))

x = 5
y = 10

print(y/x)

a = "데이터 사이언스"
b = "datascience"

print(a)

c = "동덕" + "여대" + "데이터" + "사이언스!"
print(c)

#bool
d = (100 > 10)
print(d)

e = (2<1)
print(e)

f = True
print(f)

#//////////////////////////
g = 10
h = 2
i = g + h
print("%d"%(i))

#/////////////////////////
name = input("당신의 이름을 입력해주세요: ")
print("당신의 이름은 %s입니다."%name)

x = input("숫자하나만 입력해주세요:")
#int
print(int(x)+3)

name ="777"
num_name = int(name)

print(num_name+3)

#///////////////////////////
name = input("이름 : ")
univ_id = input("학번 : ")
print("제 이름은 %s", name, "이고, 제 학번은 %s", univ_id "입니다.")


a = 200
b = 600
c = a + b
print(a, "+", b , "=", c)

#몫
print(5//3)
#나머지
print(5%3)

a = 1
a = a+1
a += 2
print (a)

#복합대입연산자
a = 10
a+=5
print(a)

#복합대입연산자 예시
a = int(input("나눠지는수 ==> "))
b = int(input("나누는수 ==> "))

n_a = int(a)
n_b = int(b)

mok = a//b
rem = a%b

print("%s을(를) %d(으)로 나눈 몫은 %d입니다."%(a,b,mok))
print("%s을(를) %d(으)로 나눈 나머지는 %d입니다."%(a,b,rem))

a = (100==100)
print(a)

#ha....jip gago shipda...
#jip ganeun gilae takoyaki meokeoyaji heuiheui~

password = "2023"
xin = input("암호를 입력하세요: ")

print(password == xin)

#//////////////////////////
x = 1
y = 10

z = not(x>0)