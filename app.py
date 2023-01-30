print("hello",'word')

name = input('请输入名称')

print("name is :"+name)
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