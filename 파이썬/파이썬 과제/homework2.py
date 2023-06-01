## 1. 약수 구하는 함수 ##
def divisor(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    pass

print(divisor(10))
print(divisor(7))



## 2. 수도 출력 ##
def find_capitalcity(capital, country):
    if country in capital:
        print(capital[country])
    else:
        pass

capital = {"대한민국": "서울", "미국": "워싱턴", "프랑스": "파리", "영국":"런던", "스위스":"베른", "베트남":"하노이","덴마크":"코펜하겐"}

print(find_capitalcity(capital, "대한민국"))
print(find_capitalcity(capital, "덴마크"))
print(find_capitalcity(capital, "일본"))



## 3. 파일쓰기 ##
# 중간고사 점수 생성
mid_test_scores = [random.randint(0, 100) for _ in range(50)]

# 기말고사 점수 생성
final_test_scores = [random.randint(0, 100) for _ in range(50)]

# 과제 점수 생성
homework_scores = [random.randint(0, 20) for _ in range(50)]

# 출석 점수 생성
attendance_scores = [random.randint(0, 10) for _ in range(50)]

# 생성된 점수들을 파일에 기록 (옵션이므로 제출할 필요 없음)
with open("mid_test.txt", "w") as file:
    for score in mid_test_scores:
        file.write(str(score) + "\n")

with open("final_test.txt", "w") as file:
    for score in final_test_scores:
        file.write(str(score) + "\n")

with open("homework.txt", "w") as file:
    for score in homework_scores:
        file.write(str(score) + "\n")

with open("attendance.txt", "w") as file:
    for score in attendance_scores:
        file.write(str(score) + "\n")



## 4. 파일 읽기 ##
def center(list):
    ## coding here ##
    


score = []

#### coding here ####

print(center(score)) # 1등 점수


## 5. 클래스 만들기 ##

class Student_DD:
    ## coding here ##
    pass

student1 = Student_DD("정영희", "데사", "1", "010-1234-5678")
student1.introduce()