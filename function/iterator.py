#迭代器
#方法: iter() next()
# list1 = [1,2,3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) #StopIteration （停止迭代）

# for i in range(10,20,2): #从10到20 步长为2
#     print(i)

#start 开始
#stop  结束
#step  步长

#关键字 yield 生成器
def frange(start,stop,step):
    x  = start
    while x<stop:
        yield x  #yieid x
        x+=step
for i in frange(10,20,0.5):
    print(i)





