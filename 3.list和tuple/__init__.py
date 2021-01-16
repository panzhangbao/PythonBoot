# coding=utf-8
#
#  list 和 tuple
#
# Created by Jason Pan on 2021-01-01 20:52:48
# Copyright © 2021 Jason Pan. All rights reserved.
#

if __name__ == '__main__':
# list是一种有序的集合，可以随时添加和删除其中的元素
    classmates = ["Michael", "Bob", "Tracy"]
print(len(classmates))  # 3

print(classmates)       # ["Michael", "Bob", "Tracy"]
print(classmates[-1])   # Tracy
# print(classmates[3])    # IndexError错误
# print(classmates[-4])       # IndexError错误

classmates.append("Neil")   # 新增元素
print(classmates[3])        # 新增指定索引元素
classmates.insert(0, "Dear")
print(classmates[0])

classmates.pop()    # 删除最后一个元素
print(classmates)
classmates.pop(0)   # 删除指定索引元素
print(classmates)

classmates[0] = "Bruce Lee"
print(classmates)

list = []
print(len(list))    # 0

########################### tuple   #################################
# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
tuple1 = ("a", "b", "c")
tuple1 = (1,2)

# 切片，前开后闭
print(tuple1[1:])
