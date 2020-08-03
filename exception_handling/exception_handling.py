#异常处理

#  i=j  未定义错误
# print()) 语法错误
# a='123';print(a[3]) 下标越界
# doc = {'a':1,'b':1};print(doc['c'])

# year = int(input("输入年份："))
# try:
#     year = int(input("输入年份："))
# except ValueError:
#     print("输入数字！")

# a=123
# try:
#     a.append(1)
# except AttributeError:
#     print("Int无append()方法")

try:
    print(1/0)
except ZeroDivisionError as str:
    print("0不能做除数 %s" %str)

try:
    raise NameError("helloError")
except NameError:
    print("my custom error")