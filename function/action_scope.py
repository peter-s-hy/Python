#可变长参数  *加函数名 实际数个元组
def foo(str,*str1):
    #打印可变长参数的长度，可以再调用方法时不传入
    print(len(str1))

foo('123')




# 函数内外 变量作用域

# 未在函数内str变量前加入 global关键字 输出结果 peter tom
str = 'tom'
def fun():
    str = 'peter'
    print(str,end= ' ')
fun()
print(str)
##在变量前加入 global关键字 使变量称为全局变量 输出结果 peter peter
str = 'tom'
def fun():
    global str
    str = 'peter'
    print(str,end= ' ')
fun()
print(str)

#print 文件用法
with open("file.txt",'w') as f:
    print(str,file=f)