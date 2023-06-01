# # ## 1. 교과목 정보 출력 ##
# # #### coding here ####
# # course_info = {
# #     '데사K0025': ['데이터사이언스를위한수학', '숭의관1호'],
# #     '문화A0019': ['파이썬프로그래밍', '인문관15호'],
# #     '문화A0007': ['데이터사이언스입문', '대학원4호']
# # }

# # while True:
# #     course_code = input("학수번호를 입력하세요: ")
# #     if course_code in course_info:
# #         course_name = course_info[course_code][0]
# #         classroom = course_info[course_code][1]
# #         print("입력하신 과목은", course_name, "이며, 강의실은", classroom, "입니다.")
# #     else:
# #         print("입력하신 과목은 정보에 없습니다.")



# # ## 2. 숫자 맞추기 게임 ##
# # # answer = 25
# # # ### coding here ####
# # answer = 25

# # while True:
# #     guess = int(input("숫자를 입력하세요 : "))
    
# #     if guess == answer:
# #         print("정답!")
# #         break
# #     elif guess < answer:
# #         print("UP!")
# #     else:
# #         print("DOWN!")


# ## 3. 각 자리의 합 계산하기 ##
# sum = 0

# for i in str(3**79):
#     sum += int(i)

# print(sum)


# ## 4. while문 출력 ## 
# #### coding here ####
# # num_stars = 7

# # while num_stars > 0:
# #     print('*' * num_stars)
# #     num_stars -= 2


# # ## 5. 리스트 데이터 확인 ##
# # # answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']

# # # A = ['hello', 62, 'umbrella', 145]
# # # B = ['September', 512.3, 'coffe', 39, 'keyboard','notebook', 0.5, 'f12']
# # # C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

# # # ### coding here ####
# # answer = ['apple', 39, 'music', 568.2, 'Dongduk', 145, 'hello']
# # A = ['hello', 62, 'umbrella', 145]
# # B = ['September', 512.3, 'coffee', 39, 'keyboard', 'notebook', 0.5, 'f12']
# # C = ['computer', 568.2, 39, 'aPple', 111, 'Dongduk', 'water']

# # input_list = input("리스트를 입력하세요 (예시: A 또는 B 또는 C): ")

# # if input_list == "A":
# #     for item in A:
# #         if item in answer:
# #             print("O")
# #         else:
# #             print("X")
# # elif input_list == "B":
# #     for item in B:
# #         if item in answer:
# #             print("O")
# #         else:
# #             print("X")
# # elif input_list == "C":
# #     for item in C:
# #         if item in answer:
# #             print("O")
# #         else:
# #             print("X")
# # else:
# #     print("리스트에 없습니다.")