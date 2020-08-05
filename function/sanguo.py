# 读取文件
# sanguotxt = open("resoursce/sgyy.txt",encoding='GB18030')
# data = sanguotxt.read()
# print(data)
# sanguotxt.close()

# 读取人物名字
# 读取人物名字figure  = open("resoursce/figure.txt",encoding='UTF-8')
# data = figure.read()
# print(data)
# figure.close()

# 异常处理
def read(file_path, encoding):
    try:
        txt = open(file_path, encoding=encoding)
        data = txt.read()
    except Exception as e:
       print("1 %s" %e)
    finally:
        txt.close()
    return data


data = read('resoursce/figure.txt', 'UTF-8')
data1 = read('resoursce/sgyy.txt', 'GB18030')
print(data, data1)

