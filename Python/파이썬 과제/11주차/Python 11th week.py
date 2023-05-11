# # f = open("C:/Users/betty/Desktop/5/Github/파이썬/Python/파이썬 과제/11주차/score.txt", 'r')

# # lines = f.readlines()

# # print(len(data))

# # # print(lines)
# # # for line in lines:
# # #      a.append(line.strip())
# #     #  print(line.strip())

# # # print(a)
# # f.close()

# # # data = f.read()

# ## 11주차 6페이지 ##
# # dir_name = '/C:/disk/'
# # if os.path.isdir(dir_name): 
# #     os.makedirs()           #폴더 없다면 만들기

# # import os
# # filename = "/C:/Users/betty/Desktop/5/Github/파이썬/Python/파이썬 과제/11주차/score.txt"
# # if os.path.exists(filename):
# #     f = open(filename, 'r')
# #     lines = f.readlines()
# #     ...#생략
# #     f.close()
# # else:
# #     print("%s 파일이 없습니다." %filename)



# x = "python"

# f = open("xxx.txt", 'w')

# # f.write(x)
# for i in range(1, 4):
#     f.write(str(i) + '\n')

# f.close()

# # a는 시험문제에 나옴.


# f = open("result.txt", 'a')

# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()


## f.close()할 필요없음 ##
# with open("result.txt",'w') as f:
#     # for i in range...
#     f.write("땡땡땡")


## 11주차 예제2~3번 ##
# id = input("학번을 입력해주세요 : ")

# f = open("id.txt", 'a')

# f.write("\n임소정")
# f.close


## 예제4번 ##
# f = open("score.txt", 'r')
# sum = 0
# average = 0.0

# lines = f.readlines()

# for line in lines:
#     sum += int(line.strip())

# print(average)


## 예제5번 ##
f = open("score.txt", 'r')
sum = 0
average = 0.0

lines = f.readline()
print(lines)

print(average)