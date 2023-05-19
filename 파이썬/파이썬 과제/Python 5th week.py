# score = [30, 40, 60, 80, 100, 70, 40]

# print(score[1])


# b = [10, 20, 30]
# b.append("alpha")
# b.append("bravo")

# print(b)

#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]출력
# x = []

# for i in range(1, 11):
#     x.append(i)

# print(x)

#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]출력
# x = []
# for i in range(0, 10):
#     x.append(i)

# y = []
# for i in range(0, 10):
#     y.append(x[9-i])

# print(y)

#420 출력
# x = [100, 80, 60, 30, 20, 10, 50, 70]

# sum = 0

# for i in range(len(x)):
#     sum = sum + x[i]

# print(sum)


#420 출력
# x = [100, 80, 60, 30, 20, 10, 50, 70]

# sum = 0

# for i in range(len(x)):
#     sum = sum + x[i]

# average = 0.0
# average = sum / len(x)
# print(sum)

#[100, 80, 70, 60, 50, 30, 20, 10] 출력
# x = [100, 80, 60, 30, 20, 10, 50, 70]

# x.sort(reverse=True) #True는 내림차순 / False는 오름차순
# print(x)

#[70, 50, 10, 20, 30, 60, 80, 100] 출력
# x = [100, 80, 60, 30, 20, 10, 50, 70]

# y = x.copy()
# y.reverse()

# print(y)


#greetings = ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']와 
#파이썬의 반복문을 이용하여,
#<안녕 니하오 하이 곤니찌와 올라 싸와디캅 봉쥬르>를 한번씩만 출력하시오.

# greetings = ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']

# for i in range(len(greetings)):
#     print(greetings[i])


#교수.VER
# greetings = ['안녕', '니하오', '하이', '곤니찌와', '올라', '싸와디캅', '봉쥬르']

# for i in greetings:
#     print(i)


#a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot',
#'golf', 'cat', 'school' 'hotel', 'india’]를 이용하여
#a리스트 값 중에서 길이가 5인 값들만
#파이썬을 이용하여 출력하시오.

# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']

# for word in a:
#     if len(word) == 5:
#         print(word)

#교수.VER
# a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']
# b = [] ##매우 중요##

# for i in a:
#     if len(i) == 5:
#         b.append(i)
# print(b)