# 
# 
# message = "abc efg qqq"
# print(message.split(' '))
# 
# 
# dic = {'name' : 'pey', 'phone' : '0119993323', 'birth': '1118'}
# print(dic['name'])
# print(dic['phone'])
# 
# s = "    abcd123    "
# 
# print(s.upper())
# print(s.capitalize())
# print(s.strip().capitalize())
# print(s.find('d'))
# print(s.strip().isalnum())
# print("123".isdigit())
# print("isupper".isidentifier())
# 
# firtst_name = "Seung Kyun"
# last_name = "Nam"
# full_name = firtst_name + " " + last_name # 문자열 연결은 +로
# 
# print(full_name)
# print(firtst_name +" "+ last_name)
# 
# laugh = "Ha"
# print(laugh * 3)
# 
# str = "안녕하십니까, 이름은 김귀수입니다."
# 
# print(len(str)) # len() : 시퀀스형의 길이를 반환
# print(str[2]) # 2번 인덱스의 문자를 반환
# print(str[0:11]) # 인덱스 0~10 사이의 문자열을 반환
# print(str[-7:-1]) # 음수 인덱스는 뒤로부터 계산
# print(str[5:]) #인덱스는 필요에 따라 생략 가능
# 
# palindrome = 'A man,\nAPlan,\nA canal:\nPanama'
# print(palindrome)
# 
# print('\tabc')
# print('a\tbc')
# print('ab\nc')
# print('\tabc')
# 
# s = "i like Python"
# 
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.capitalize())
# print(s.title())
# 
# testimony = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
# print (testimony)





# s = "I Like Python. I Like Java Also"
# 
# print(s.count("Like"))
# print(s.find("Like"))
# print(s.find("Like", 5))
# print(s.find("JS"))
# print(s.rfine("Like"))
# 
# print(s.rindex("Like"))
# print(s.startswith("I Like"))
# print(s.startswith("Like", 2))
# print(s.endswith("Also"))
# print(s.endswith("Java", 0, 26))

# s = 'Alice and the Heart Queen'
# print(s.)

# a = list('cat')
# print(a)
# 
# a_tuple = ('ready', 'fire', 'aim')
# print(list(a_tuple))
# 
# birthday = '1988/09/16'
# print(birthday.split('/'))
##################################### if 조건문 #####################################
# disaster = True
# if disaster :
#     print("Woe!")
# else :
#     print("Whee!")





# furry = False
# small = True
# if furry:
#     if small:
#         print("It's a cat.")
#     else:
#         print("It's a bear!")
# else:
#     if small:
#         print("It's a skink!")
#     else:
#         print("It's a human. Or a hairless bear.")

# color = 'Green'
# if color =="red":
#     print("It's a tomato")
# elif color == "Green":
#     print("It's a Green pepper")
# elif color == "bee purple":
#     print("I don't know what it is, but only bees can see it")
# else:
#     print("I've never heard of the color", color)
#################################################################################3


# l = [1, 2, 'python'] #리스트는 [] 기호를 이용하여 생성

# print(l[-2], l[-1], l[1], l[2])
# print(l [1:3])
# print(l * 2)
# print(l + [3,4,5])
# print(1 + len(l))
# print(2 in l)

# del l[0]
# print(l)



# a = [1,2,3]
# 
# a.append(5)
#  print(a)


# count = 1
# while count<10:
#     print(count)
#     count += 1

# while True:
#     stuff = input("String to capitalize [type q to quit]:")
#     if stuff == 'q':
#         break
#     print(stuff.capitalize())



# s1 = {1,2,3,4,5,6,7,8,9,10}
# s2 = {10, 20, 30}

# s3 = s1.union(s2) # 합집합
# print(s3)

# # s4 = s1.intersection(s2) # 교집합

# s4 = s1.difference(s2) # 차집합
# print(s4)

# s5 = s1.symmetric_difference(s2) #대칭자(둘 모두에 속하지 않은 원소 집합)
# print(s5)

# print(s1 & s2) #교집합
# print(s1 | s2) #합집합
# print(s1 - s2) #차집합


# t = (1,2,3)
# print(t, type(t))

# t = 1, 2, 'python' # ()를 생략해도 튜플을 생성할 수 있다.
# print(t, type(t))

# print(t[-2], t[-1], t[0], t[2])
# print(t[1:3]) #슬라이싱
# print(t[:])

# print(t * 2) #반복(*)
# print(t + (3, 4, 5)) #연결(+)

# t = 10, 20, 30, 'python'
# a,b,c,d = t
# print(a,b,c,d)

# t = (1,2,3,4,5,6)
# a,*b =t
# print(a,b)
# 
# *a, b =t
# print(a,b)
# 
# a, b, *c = t
# print(a, b, c)
# 
# a, *b, c = t
# print(a,b,c)

# dir = {'basketball' : 5, 'soccer ': 11, 'baseball': 9}
# print(dir, type(dir))

# print(dir['basketball'])

# dir['volleyball'] = 6
# print(dir)

# print(len(dir))
# print('soccer' in dir)
# print('volleyball' not in d)

# dir = dict() # empty dict
# print(dir)

# dir = dict(one = 1, two = 2) # keyword arguments
# print(dir)

# dir = dict([('one', 1),('two', 2)]) #tuple list
# print(dir)

# keys = ('one', 'two', 'three')
# values = (1, 2,3)
# dir = dict(zip(keys, values)) #키와 값을 별도로 선언 후 합침
# print(dir)

# print(list(zip([1,2,3],[4,5,6])))


# a = [1,2,3,4]
# 
# while
#     # print(a.pop())

# a = [1,2,3]
# b = [1,2,3]
# print(a is b)


# # 글로벌 변수 선언
# g_a = 1
# g_b = "symbol"

# def f(): #로컬 변수 확인을 위한 함수 선언
#     l_a = 2
#     l_b = "table"
#     print(locals()) #로컬 심볼테이블 확인
# f()



# import sys
# x = object()
# print(sys.getrefcount(x))

# y = x
# print(sys.getrefcount(x))

# print(sys.getrefcount(y))

# del(x)
# print(sys.getrefcount(y))



# import copy
# x = F
# }

# money = 8500
# print("by texi " if money > 10000 else "by bus")



# list 객체를 이용한 for 문
# ani = ['cat', 'cow', 'tiger']
# for ani in ani:
#     print(ani, end = ' \n')



# #ramge 객체를 이용한 for문
# for x in range(1, 10, 3):
#     print(x, end = '\n')


######################################################
#for ~ else 문의 활용
# data = 1,2,3,4,8

# for x in data:
#     if x > 10:
#         break
    

# print("10보다 큰수가 없음.")

######################################################


# print("★ 구구단을 출력합니다.\n")
# for x in range(2, 10):
#     print("------- [" + str(x) + "단] -------")
#     for y in range(1, 10):
#         print(x, "x", y, "=", x*y)
# print("---------------------")


# x = 0
# for y in range(0, 101):
#      x += y

# print(x)



# counter = 0
# while counter < 11:
    # print(counter, end = " ")
    # counter += 1
# else:
    # print("err")



# sum, i = 0,1
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)






# a = "Life is too short, you need python"

# if "wife" in a: print("wife") # "wife"라는 단어는 a 문자열에 없으므로 거짓이 된다.
# elif "python" in a and "you" not in a: print("python") #"Python"이라는 단어는 a 문자열에 있지만 "you"역시 a 문자열에 있으므로 거짓이 된다.
# elif "shirt" not in a: print("shirt") #"shirt"라는 단어는 a문자열에 없으므로 참이 된다.
# elif "need" in a: print("need") #"need"라는 단어는 a문자열에 있으므로 참이 된다.
# else:
#     print("none")
# 결괏값 = shirt가 출력됨(가장 먼저 참이 되는 조건이 shirt라서 출력이 됨)



# result = 0
# i = 1 
# while i <= 1000:
#     if i % 3 == 0:
#         result += i
#     i += 1
    
# print(result)




# i = 0
# while True:
#     i += 1
#     if i >= 6: 
#         break
#     print('*' * i)



# for i in range(0,101):
#     print(i)


a = [70,60,55,75,95,90,80,80,85,100]
total = 0 
for score in a :
    total += score
    average = total / 10
    
print(average)