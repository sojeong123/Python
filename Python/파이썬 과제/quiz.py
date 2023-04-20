# ##### 2023-1학기 파이썬프로그래밍 (A0019 퀴즈) #####

# ##### 학번 : 20201012
# ##### 이름 : 임소정


# ##### 1번 문제 #####
# 1부터 10까지의 숫자를 각각 홀수와 짝수인지
# 파이썬을 이용하여 출력하자.

# ### coding here ###
# for i in range(1, 11):
#     if i % 2 == 0:
#         print(i, "는 짝수입니다.")
#     else:
#         print(i, "는 홀수입니다.")

# ##### 2번 문제 #####
# 30이하의 자연수 중
# 2,3의 배수를 제외한 수만 파이썬으로 출력해보자.

# ### coding here ###
# (ANSWER 1)
# i = 1
# while i <= 31:
#     if i % 2 == 0 and i % 3 == 0:
#         pass
#     else:
#         pass
#     i += 1


# (ANSWER 2)
# for i in range(1, 31):
#     if i % 2 == 0 or i % 3 == 0:
#         continue
#     print(i)


# (ANSWER 3)
# i = 1
# while i <= 31:
#     if i % 2 == 0 and i % 3 == 0:
#         print(i)
#     else:
#         pass
#     i += 1


# ##### 3번 문제 #####
# 1. 최대 숫자를 number라는 변수명에 입력받아 1부터 number까지 3.6.9게임을 올바르게 진행하였을 경우 박수를 총 몇 번 쳐야 하는지를 구해보자.
# 2. 1부터 시작합니다.
# 3. 한 사람 씩 차례대로 숫자를 1씩 더해가며 말합니다.
# 4. 말해야 하는 숫자에 3,6,9 중 하나라도 포함되어 있다면 숫자를 말하는 대신 숫자에 포함된 3,6,9의 개수만큼 박수를 칩니다.
# 5.예를 들어 33은 박수를 두 번 쳐야 합니다.

# ### coding here ###
# (ANSWER 1)
# number = int(input("숫자를 입력하세요: ")) 
# claps = 0  

# for i in range(1, number+1):  
#     count = 0  

#     for digit in str(i):
#         if digit in ['3', '6', '9']:
#             count += 1
    
#     if count == 0:
#         pass 
#     else:
#         claps += count 

# # print(claps)


# (ANSWER 2)
# number = int(input("최대 숫자를 입력하세요: "))
# clap_count = 0

# for i in range(1, number+1):
#     # i를 문자열로 변환한 후, '3', '6', '9' 중 하나라도 포함되어 있는지 확인
#     if '3' in str(i) or '6' in str(i) or '9' in str(i):
#         clap_count += str(i).count('3') + str(i).count('6') + str(i).count('9')

# print(clap_count)