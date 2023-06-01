### 푸딩 5주차 ###

"""
#### 과제 ####
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
"""


"""
#### 문제 ####
## 1번 ##
# 어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다.
# 정수n이 매개변수로 주어질 때, 
# n이 제곱수라면 1을, 아니라면 2를 return하도록
# solution 함수를 완성해주세요.
# (단, 1<=n<=1000000)

def solution(n):
    if int(n**0.5)**2 == n:
        return 1
    else:
        return 2

        

## 2번 ##
# 0부터 9까지의 숫자중 일부가 들어있는
# 정수리스트 numbers가 매개변수로 주어집니다.
# numbers에서 찾을 수 없는 0~9까지의 숫자를
# 모두 찾아 더한 수를 return하도록
# soulution함수를 완성해주세요.

# <조건>
# 1<=numbers의 길이<=9
# 0<=numbers의 모든 원소<=9
# numbers의 모든 원소는 서로 다릅니다.

# <예시>
# print(solution([1,2,3,4,6,7,8,0]))
# 14

def solution(numbers):
    total_sum = 45  # 0부터 9까지의 숫자의 합은 0부터 9까지의 숫자의 총합인 45입니다.
    
    for num in numbers:
        total_sum -= num  # numbers에 있는 숫자를 총합에서 빼줍니다.
    
    return total_sum


    
## 3번 ##
# 다음과 같이 입력했을 때,
# 출력값이 아래와 같이 나오도록 만들어주세요.

# <입력값>
# def factorial(n):
# print("5!:", factorial(5))

# <출력값>
# 5!: 120

## 재귀함수를 사용해 팩토리얼 구하기 ##
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("5!:", factorial(5))



## 4번 ##
# 범위 내부의 정수를 모두 더하는 함수를 이용하여,
# 다음과 같은 출력결과가 나올 수 있도록 만들어주세요.
# 0 to 100: 5050

def sum_range(start, end):
    total_sum = 0
    for num in range(start, end+1):
        total_sum += num
    return total_sum

# start = 0
# end = 100
# result = sum_range(start, end)
# print(f"{start} to {end}: {result}")

print("0 to 100:", sum_range(0, 100))



# ## 5번 ##
# x만큼 간격이 있는 n개의 숫자

# <문제 설명>
# 함수 solution은 정수x와 자연수n을 입력 받아,
# x부터 시작해 x씩 증가하는 숫자를
# n개 지니는 리스트를 리턴해야 합니다.
# 다음 제한 조건을 보고,
# 조건을 만족하는 함수인 solution을 완성해주세요.

# <제한 조건>
# x는 -10000000이상, 10000000이하인 정수입니다.
# n은 1000이하인 자연수입니다.

# <입출력 예시>
# x       n       answer
# 2       5       [2, 4, 6, 8, 10]
# 4       3       [4, 8, 12]
# -4      2       [-4, -8]

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x * i)
    return answer

print(solution(2,5))

#for문 보다는 while문을 사용.
#for문은 음수 표현하기가 어려움.
"""


## 6번 ##
# 1차원 점들이 주어졌을 떄,
# 그 중 가장 거리가 짧은 것의 쌍을
# 출력하는 함수를 작성하시오.

# (단, 점들의 배열은 모두 정렬되어 있다고 가정합니다.)
# 예를 들어 S={1, 3, 4, 8, 13, 17, 20}이 주어졌다면,
# 결과값은 (3,4)가 될 것입니다.

def find_closest_pair(points):
    if len(points) < 2:
        return None

    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points) - 1):
        distance = points[i+1] - points[i]
        if distance < min_distance:
            min_distance = distance
            closest_pair = (points[i], points[i+1])

    return closest_pair

points = [1, 3, 4, 8, 13, 17, 20]
closest_pair = find_closest_pair(points)
print(closest_pair)
