### 푸딩 5주차 ###

## 1번 ##
apart = [[101, 102], [201, 202], [301, 302]]

for floor in apart:
    for room in floor:
        print(str(room) + "호")



## 2번 ##
score = int(input("점수를 입력하세요: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(grade + "학점입니다.")



## 3번 ##
N = int(input("숫자 N을 입력하세요: "))

# 위쪽 삼각형 출력
for i in range(1, N+1):
    # 공백 출력
    for j in range(N-i):
        print(" ", end="")
    # 별 출력
    for j in range(2*i-1):
        print("*", end="")
    print()

# 아래쪽 삼각형 출력
for i in range(N-1, 0, -1):
    # 공백 출력
    for j in range(N-i):
        print(" ", end="")
    # 별 출력
    for j in range(2*i-1):
        print("*", end="")
    print()



## 4번 ##
count = 0

for number in range(10000):
    if '8' not in str(number):
        count += 1

print("8을 포함하지 않는 수의 개수:", count)



## 5번 ##
count = 0

for number in range(1, 101):
    count += str(number).count('8')

print("8이 나오는 횟수:", count)



## 6번 ##
decimal = int(input("정수를 입력하세요: "))
binary = ''

while decimal > 0:
    binary = str(decimal % 2) + binary
    decimal = decimal // 2

print("2진수로 변환된 값:", binary)
