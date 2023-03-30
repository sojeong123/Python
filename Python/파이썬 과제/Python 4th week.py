# for i in range(3) :
#     print("안녕하세요.")

# for i in range(5):
#    print("*"*i)

# for i in range(1,31,1):
#     if i % 3 !== 0:
#         print(i)
#     else:
#         print("****")


#내가 한 것

# A = int(input("2이상의 숫자를 입력해주세요. : "))
# answer = 1

# for i in range(1,A+1,1):
#     answer = answer * i

# print(i*(i+1))


# A = int(input("2이상의 숫자를 입력해주세요. : "))
# answer = 1

# for i in range(1,A+1,1):
#     answer = answer * i

# print(answer7)

# sum = 0

# for i in range(1,11):
#     sum = sum + 1
# print(sum)

# sum = 0

# for i in range(1000,2001):
#     if i % 2 == 1:
#         sum = sum + i

# print(sum)


# 내가 한 것
# A = int(input("구구단 몇단을 계산할까요? : "))
# dan = 1

# for i in range(A+1,10,1):
#      dan = dan * i

# print("A * i = "A*i)

#미완성 교수
# A = int(input("구구단 몇단을 계산할까요? : "))

# for i in range(1,10):
#     print("%d * %d = %d" %(dan, i, dan*i))

# for i in range(3):
#     for j in range(2):
#        print(i,j)

#구구단
# for i in range(2,10):
#     for j in range(1,10):
#         print("%d * %d = %d" %(i, j, i*j))


# i = 0

# while i < 3 :
#     print("안녕하세요.")
#     i = i +1


# sum
# for i in range(1,11)
#     sum = sum + i

# print(sum)


# i = 0
# sum = 0

# while i < 11:
#     sum = sum + i
#     i = i + 1
# print(sum)

#미완성
# i = 0
# while i < 5:
#     print("*"*10)
#     i = i + 1


# i = 0
# while i < 5:
#     print("*"* 10)
#     i = i + 1
#     if i >2:    break

#1~100중에서 3의 배수는 제외하고 출력
# for i in range(100):
#     if i % 3 == 0:
#         continue        #3의 배수 제끼고 다시 위로 올라가서 출력
#     print(i)


#1~100까지 숫자를 모두 더한 값을 출력하세요. [5050]
# i = 1
# sum = 0

# while i < 101:
#     sum = sum + i
#     i = i + 1
# #    #print(sum)     이렇게 쓰면 중간값도 계속 같이 출력됨.
# print(sum)


# i = 1
# while i < 11:
#     if i % 3 == 0:
#         i = i + 1
#         continue

#     print(i)
#     i = i + 1


#복리이자율 7%로 1000만원 저금 시 
#2000만원이 되기까지 몇년이 걸리는가? (while문) [11년]

# money = 1000
# year = 0

# while money < 2000:
#     money = money + money*(0.07)
#     year += 1

# print(year)


#30과 75의 최대공약수를 출력해보세요. [15]
# i = 1
# while i < 31:
#      if (30 % i == 0):
#          i = i + 1
#      if (75 % i == 0):
#          i = i + 1
#          continue

#      print(i)
#      i = i + 1

#교수 For문 VER.
# gcm = 0
#
# for i in range(1,31):
#     if 30 % i == 0 and 75 % i == 0:
#         gcm = i
#print(gcm)

#교수 IF문 VER.
# i = 1
# while i < 31:
#    if 30 % i == 0 and 75 % i == 0:
#       gcm = i