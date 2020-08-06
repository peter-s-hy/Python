#迭代器

# list1 = [1,2,3]
# it = iter(list1)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) #StopIteration （停止迭代）

for i in range(10,20,2): #从10到20 步长为2
    print(i)

def frange(start,stop,step):
    x  = start
    while x<stop:
        yield x  #yieid x
        x+=step




