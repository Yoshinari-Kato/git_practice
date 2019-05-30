# coding: utf-8
# print('hello world')
# num=1
# name='Mike'

# print('Hi','',sep=',' ,end='.\n')

# print(r"C:\name\name")
# print("##############")
# print("""\
# LINE1
# LINE2
# LINE3\
# """)
# print("##############")
# print("Mike"+"idiot")
# word="python"
# print(word[0])
# print(word[-1])
# print(word[0:2])
# word="j"+word[1:]
# print(word)
# n = len(word)
# print(n)

# s= 'My name is Homare'
# print(s)
# is_start = s.startswith('My')
# print(is_start)
# print(s.find('Homare'))
# print(s.count('Homare'))
# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.replace("Homare","Yoshinari"))

# name = "Yoshinari"
# family = "Kato"
# print(f'My name is {name} {family}. 私は{family} {name}です')
# l = [1,2,3,4,5,6,7,8,9,10]
# print(l[::3])
# n=[1,2,3]
# m=["a",'b','c']
# p=[n,m]
# print(p[0][1])

# s = ['a','b','c','d','e','f','g']
# s[0]="yo"
# print(s)
# s[2:5]=['C','D','E']

# print(s)
# s[2:5]=[]
# print(s)
# print(len(s))

# n=[1,2,3,4,5,6,7,8,9,10]
# n.append(100)
# print(n)

# n.insert(0,90)
# print(n)

# n.pop()
# print(n)

# n.pop(0)
# print(n)

# n=[1,2,2,2]
# n.remove(2)
# print(n)

# a=[1,54,7,344476,21]
# b=[4,676,97997,4242425355,13]
# print(a+b)
# a+= b
# print(a)

# x=[12,4,76,32,6,97,98]
# y=[6,7,8,9,10]
# x.extend(y)
# print(x.index(6,6))
# print(x.count(6))
# if 76 in x:
#     print('exist')

# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)
# x.reverse()
# print(x)

# s = "My name is Mike"
# to_split = s.split(" ")
# print(to_split)
# x=" ".join(to_split)
# print(x)

# i=[1,2,3,4,5]
# j= i
# j[0]=100
# print('j=',j)
# print('i=',i)

# x=[1,2,3,4,5]
# # y=x.copy()
# y=x[:]
# y[0]=100
# print('y=',y)
# print('x=',x)

# X = 5
# Y = X
# Y = 50
# print(id(X))
# print(id(Y))
# print(X)
# print(Y)

# X = ['a','b']
# Y = X 
# Y[0]='p'
# print(id(X))
# print(id(Y))
# print(X)
# print(Y)

# seat = []
# min = 0
# max = 5
# print(min <= len(seat) <max)
# seat.append('p')
# seat.append('p')

# print(len(seat))
# print(min <= len(seat) <max)

# seat.append('p')
# seat.append('p')
# print(len(seat))
# print(min <= len(seat) <max)

# print(seat)
# seat.append('p')
# print(min <= len(seat) <max)

# seat.pop()
# print(min <= len(seat) <max)

# t=(1,2,3,4,5)
# print(type(t))
# print(t[0])

# t=([1,2,3],[4,5,6])
# print(t[0][0])
# t[0][0]=100
# print(t[0][0],t)

# num_tuple=(10,20)
# x,y=num_tuple
# print(x,y)

# i=10
# j=20
# tmp=i
# i=j
# j=tmp
# print(i,j)

# a=100
# b=200
# a,b=b,a
# print(a,b
# )

# d={"x":10,"y":20}
# d2={"x":500,"j":1000}
# print(d)
# print(type(d))
# print(d["x"])

# print(dict(a=10,b=50))
# print(d.keys())
# print(d.values())
# print(d2)
# d.update(d2)
# print(d)
# print(d["x"])
# print(d.get("x"))
# print(d.pop("x"))
# print(d)
# # del d
# # d.clear
# print("a"in d)
# print(d)

# x={"a":1}
# y=x.copy()
# y["a"]=1000
# print(x)
# print(y)

# fruits={
#     "apple":100,
#     "banana":150,
#     "orange":200
# }

# print(fruits["apple"])

# # 集合{}
# a={1,2,2,3,3,4,4,4,5,6}
# print(a,type(a))
# b={2,3,3,6,7}
# print(a-b,a&b,a|b,a^b) 
# # a^bはどちらかにあって重複していないもの

# s={1,2,3,4,5}
# s.add(6)
# s.remove(6)
# s.clear()
# print(s)

# my_friends={"a","b","c"}
# A_friends={"b","d","e","f"}
# print(my_friends&A_friends)

# f=["apple","banana",'apple','banana']
# リストから集合へ型を変換
# kind=set(f)

# """
# これでも
# コメントになるよ！
# s='aaaaaaaaaaa'\
# +'bbbbbbbbb'
# 長い行を二つに分けて計算を行う際にはバックスラッシュ！！！
# ()でもOK　改行の目安は80文字
# """
# print(kind)

# x=12

# if x<0:
#     print('negative')
# elif x==12:
#     print('12')
# else:
#     print('positive')

# a=10
# b=5

# if a >0:
#     print('a is positive')
#     if b >0:
#         print('b is positive')

# 論理式
# 「かつ」はandを使う。
# 「または」はorを使う

# y=[1,2,3]
# x=1

# if x in y:
#     print('in y')

# if 100 not in y:
#     print('not')

# is_ok = True
# if not is_ok:
#     print('hello')

# 変数に値が入っているかを確認するテクニック
# 値がなければはfalse  値が入っている場合ははtrueとして判定される
# is_ok = 'asjail'
# if is_ok:
#     print('OK')
# else:
#     print('NO')

# is_empty = None
# print(is_empty)

# if is_empty == None:
# if is_empty is not None:
#     print('None!!!')

# ちょっと難しい話するよ。
# is は同じオブジェクトかどうかを判定するNoneの時は基本的にisを使うよ

# print(1==True)
# print(1 is True)
# print(True is True)

# while文だぞ
# count = 0

# while count < 5:
#     print(count)
#     count += 1

# continueはスキップして次のループに行ってくださいという意味
# count2 = 0
# while True:
#     if count2 >= 5:
#         break

#     if count2 ==2:
#         count2 += 1
#         continue
        
#     print(count2)
#     count2 += 1

# count = 0
# while count < 5:
#     print(count)
#     count += 1
# else:
#     print('done')

# input関数 コンソール上に入力できるよう表示する
# while True:
#     word = input('Enter:')
#     if word == 'ok':
#         break
#     print('next')

some_list=[1,2,3,4,5]
# i=0
# while i <len(some_list):
#     print(some_list[i])
#     i+= 1

# for i in some_list:
#     print(i)

# for s in 'abcde':
#     print(s)
# for word in ['My','name','is','Yoshi']:
#     print(word)

# for fruits in ['apple','orange','banana']:
#     if fruits == 'banana':
#         print('stop eating')
#         break
#     print(fruits)
# else:
#     print('I ate all')

# レンジ関数 range(開始位置,表示するかず,飛ばす間隔)
# num_list = [0,1,2,3,4,5,6,7,8,9]
# for i in num_list:
#     print(i)   古い古い！！

# for i in range(1,10,3):
#     print(i)

#for _ in range(10):
#     print('Hello')

# indexを使わない場合は _

# enumerate関数 index番号を表示してくれる関数
# for i, fruits in enumerate(['apple','banana','grape']):
#     print(i,fruits)

# #zip関数
# days=['Mon','Tue','Wed']
# fruits=['apple','banana','orange']
# drinks=['coffee','greantea','milk']


# for day,fruit,drink in zip(days,fruits,drinks):
#     print(day,fruit,drink)

# 辞書型をforで処理
# d = {'x':100,'y':200}
# for v in d:
#     print(v)

# この場合はxとyが表示されて終了する。なので辞書型のメソッドを使う

# d = {'x':100,'y':200}
# print(d.items())
# for key, value in d.items():
    # print('{}:{}'.format(key,value))

# 関数定義
def say_something():
    # print('hi')
    s = 'hi,Mike'
    return s
result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'qucamber'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)
