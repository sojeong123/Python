"""""
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'cat', 'school', 'hotel', 'india']

for i in a: #for i in 리스트이름:
    if len(i) == 5 :
        b.append(i)

print (i)
"""""


"""""
x = [1,2,3,4,5]
y = (1,2,3,4,5)     #튜플은 ()을 사용
z = (1)
print(y)

x[0] = 10
print(x)

del(y)      #수정 불가, 아예 전체 다 지우는 것만 가능.

print(y)
"""""


"""""
x = (1,2,3,4)
y = list(x)
y.append(5)
x = tuple(y)
print(x)
"""""


#########딕셔너리는 중요#########
"""""
x = {'1교시':'파이썬', '2교시':'수학', '3교시':'영어'}

print(x)


# {중괄호}가 쳐져있으면 딕셔너리
# 꼭 쌍으로 존재함.
# 꼭 키랑 value랑 쌍으로 추가해야함.
# 딕셔너리는 키값만 중요, 순서는 안 중요함.

professor = {'학번':'20231234', '이름': '김철수','부서':'컴퓨터학과'}
professor ['나이'] = 99
professor['이름'] = '홍길동'        #key값 덮어쓰기

del(professor['나이'])             #key값 지우기

print(professor)
"""""

"""""
professor = {'학번':'20231234', '이름': '김철수','부서':'컴퓨터학과'}
professor ['나이'] = 99
professor['이름'] = '홍길동'        #key값 덮어쓰기

print(  list(professor.keys())  )

#del(professor['나이'])             #key값 지우기
"""""


"""""
professor = {'학번':'20231234', '이름': '김철수','부서':'컴퓨터학과'}
professor ['나이'] = 99
professor['이름'] = '홍길동'        #key값 덮어쓰기

print(professor['학번'])            #get과의 차이점 없음
print(professor.get('학번'))        #굳이 get 사용하지 말 것.
"""""


"""""
professor = {'학번':'20231234', '이름': '김철수','부서':'컴퓨터학과'}
professor ['나이'] = 99
professor['이름'] = '홍길동'        #key값 덮어쓰기

print('전화번호', in professor)
print('학번', in professor)
print(      list(professor.values())    )
"""""


##### page 20 [중요] #####
"""""
professor = {'학번':'20231234', '이름': '김철수','부서':'컴퓨터학과'}
professor ['나이'] = 99
professor['이름'] = '홍길동'        #key값 덮어쓰기

# for i in professor:               
#     print(i, professor[i])           

# for i in professor.keys():
#     print(i, professor[i])

# for k, v in professor.items():      #k는 key, v는 value
#     print(k,v)

### 주석처리 된 3가지 중 하나만 외우기[중요] ###
"""""


"""""
# 05의 예제 #
foods = {"떡볶이":"김밥", "자장면":"단무지","라면":"파김치","치킨":"맥주","삼겹살":"소주"}
print(list(foods.keys()))

while True:
    # name = input(list(foods.keys()))          도 가능
    name = input(str(list(foods.keys())) + "중 좋아하는 음식은?")
    if name == '끝' or name not in foods : break        
    print(name + '궁합 음식은' + foods[name] + '입니다.')

    # if구문을 마지막줄에 넣으면 절대 안됨. 코드의 순서가 중요한 파이썬.
"""""


"""""
### 딕셔너리로 성적 합계/평균 구하기 ###

scores = {'김예진':90, '박영진':95, '김소희':84}
sum = 0

for key in scores:
    sum += scores[key]
    print('%s : %d' % (key, scores[key]))

avg = sum/len(scores)

print('합계 : %d, 평균 : %.2f' % (sum, avg))
#아까 언급한 3가지 중 첫번째 방법 사용
"""""



### 딕셔너리로 영단어 퀴즈 만들기 ###
words = {'사과':'apple', '컴퓨터':'computer', '학교':'school', '책상':'desk', '의자':'chair'}

for i in words.keys():
    name = input(i + '에 해당되는 영어를 입력해주세요: ')
    
    if name == words[i]:
        print("정답")
    elif name == "끝"