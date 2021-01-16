#coding=utf-8
#
#  1.数据类型和变量
#
# Created by Jason Pan on 2021-01-01 19:50:34
# Copyright © 2021 Jason Pan. All rights reserved.
#

# 为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：

if __name__ == '__main__':
# 字符串
# 多行字符串'''...'''
    print('''line1
line2
line3''')

# 布尔值   只有True、False两种值
#           布尔值可以用and、or和not运算
print(not True)
#布尔值经常用在条件判断中
age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

# 空值 None

# 变量
a = '你好'
b = 3.5
c = True
d = None
print(d)

# 常量    通常用全部大写的变量名表示常量，实质上还是变量
PI = 3.14

# 3.list和tuple.3333333333333335
print(10 / 3)
# 3.list和tuple     //除法只取结果的整数部分
print(10 // 3)
# 1
print(10 % 3)

s1 = 'abc'
s2 = s1
# True
print(s1 == s2)



