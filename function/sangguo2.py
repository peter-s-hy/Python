import re


# 全本中去除回车换行
def find_time(hero):
    with open('resoursce/sgyy.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        hero_list = re.findall(hero, data)
        print("名字: %s 次数: %s" % (hero, len(hero_list)))
    return len(hero_list)

# 获取名字 去除|
name_list = {}
with open('resoursce/figure.txt', encoding='UTF-8') as i:
    for line in i:
        names = line.split('|')
        for name in names:
            name_num = find_time(name)
            name_list[name] = name_num
print(name_list)