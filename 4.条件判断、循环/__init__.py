# coding=utf-8
#
#  条件判断和循环
#
# Created by Jason Pan on 2021-01-11 22:12:05
# Copyright © 2021 Jason Pan. All rights reserved.
#

if __name__ == '__main__':
    age = 30
    if age > 18:
        print("成人")
    else:
        print("小孩")

    # for 循环
    list = [1,3,5]
    for e in list:
        print(e)

    # 字典
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d['Michael'])
    print(d['a'])