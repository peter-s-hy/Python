# 将小说的人物写在文件中
# w 写 ，r 只读 （默认）,a 不换行追加
# file1 = open('name.txt','w')
# file1.write("蜀国--刘备")
# file1.close()
#
#
# #读取文件
# file2 = open('name.txt')
# str = file2.read()
# file2.close()
# #打印内容
# print(str)
#
# #文件追加
# file3 = open("name.txt","a")
# file3.write("\n蜀国--赵云")
# file3.write("\n蜀国--张飞")
# file3.write("\n蜀国--关羽")
# file3.close()
#
# #多行文件读取
# file4 = open("name.txt")
# print(file4.readlines())
# file4.close()
#
# flie5 = open("name.txt")
# for line in flie5.readlines():
#     print(line)
#     print("========")

file6 = open('name.txt')
print(file6.tell())
file6.read(1)
print(file6.tell())
file6.seek(0) #参数一:偏移量 参数二: 0,1,2 (0：从文件开头进行偏移，1:从文件当前位置开始偏移，2:从文件结尾进行偏移)
print(file6.tell())
file6.read(1)
print(file6.tell())
file6.read(1)
file6.read(1)
print(file6.tell())
file6.seek(10,0)
print(file6.tell())