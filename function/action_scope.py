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