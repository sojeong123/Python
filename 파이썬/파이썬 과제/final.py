##### 2023-1학기 파이썬프로그래밍 (A0019 기말고사) #####
# ----------------------------------------------------------------------------------------------------------
# 다음과 같은 행위를 부정행위로 간주하며, 온라인 시험 부정행위에 대해서는 관련자 모두를 0점(F)처리하고 학칙에 따라 징계처분 될 수 있으니 유념하시기 바랍니다.
# (1) 시험 중 문제나 답안을 전화, SNS, 단톡방, 문제풀이 사이트 등을 통해 공유하는 행위
# (2) 시험도중 시험화면을 이탈하거나 특수키(Ctrl, Alt, Window key 등) 사용, 다른 프로그램을 사용하는 행위
# (3) 오픈북 시험이 아닌데 교재나 시험관련 자료를 펴놓고 시험을 보는 행위
# ----------------------------------------------------------------------------------------------------------

# 본인은 온라인 시험 관련 모든 유의사항을 확인하였고 부정행위를 하지 않을 것이며, 부정행위를 하였을 경우에는 0점(F학점)을 감수하며 학칙에 따른 징계절차에 따르겠습니다.
# 위의 사항에 동의할 경우 아래 대답에 "동의합니다" 라고 작성해 주십시오.

##### 대답 : 네
##### 학번 : 20201012
##### 이름 : 임소정




"""
#### 1번 문제 #####
phone_number = input("당신의 휴대폰 번호를 입력해 주세요.")
modified_number = phone_number.replace("-","")
print(modified_number)
"""



"""
##### 2번 문제 #####
def addmul(a,b,c):
    res = (a+b)*c
    return res

result = addmul(1,3,-2)
print(result)
"""



"""
##### 3번 문제 #####
f = open('name.txt','w')

name = ['Alex','Emma','Smith','Jane','Ava','Charlotte','Evelyn']
for i in name:
    if len(i) == 4:
        f.write(i)
        f.write('\n')
    else:
        pass

f.close()
"""



"""
#### 4번 문제 #####
def find_character(string,k):
    print(string[k-1])

find_character("computer",2) # o 출력
find_character("happy",1) # h 출력
find_character("data",3) # t 출력
"""


"""
#### 5번 문제 #####
def sasp(n):
    s = "동덕" * n
    return s

print(sasp(4)) #출력: 동덕동덕
print(sasp(5)) #출력: 동덕동덕동
"""



##### 6번 문제 #####
string = "apple"
alphabet = {}

for i in string:
    if i not in alphabet:
        alphabet[i] = i
    else:
        pass
print(alphabet)



"""
#### 7번 문제 #####
class Fourcal :
    def sum(self,a,b):
        return a+b
    def mul(self,a,b):
        return a*b
    def subtract(self,a,b):
        return a-b
    def divisor(self,a,b):
        return a/b

a = Fourcal()
print(a.sum(4,2))
print(a.mul(4,2))
print(a.subtract(4,2))
print(a.divisor(4,2))
"""


"""
##### 8번 문제 #####
f = open('20201012.txt','w')

for i in range(6,0,-1):
    for j in range(i):
        f.write(str(i))
        f.write(" ")
    f.write('\n')

f.close()
"""



"""
##### 9번 문제 #####
def check_number(string):
    result = ""
    for i in string:
        if i == "3" or i == "6" or i == "9":
            result += "x"            
        else:
            result += i
    print(result)

check_number("010-9012-3569")
"""