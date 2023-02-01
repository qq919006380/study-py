print("hello",'word')

name = input('请输入名称：')
if name:
    print("name is :"+name)
else:
    print('请输入正确的名称')

# 多行
print("换行： line1 \n line3 \n line3")

print('''line1
 line2
 line3''')  

print(r"不转义： a\n \n b")

print(True and True) #true
print(True and False) #false
print(True or False) #true
print(False or False) #false
print(not True)#取反 false
print('隐式转换',not 1)

if  1>2:
    print(True)
else:
    print(False)

print("len",len('abc'))
array=[1,2,3,4,5]
array.append(0)
print(type(array),array,array[0])

t=(1) #小括号进行计算
t1=(1,) #表示tuple
print(type(t),type(t1))

for item in array:
    print("item",item)

n=0
while n<3:
    print(n)
    n=n+1

print(type(range(5)),list(range(5)))

obj={"a":"aaa","b":"bbb"}
print("obj",obj["a"])

print(type(obj),type([]),type((1,2)),type(1),type('str'),type(True))

def sum(x,y):
    return x+y

print('sum',sum(1,2))