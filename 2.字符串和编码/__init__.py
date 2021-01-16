# coding=utf-8
#
#  2.字符串和编码
#
# Created by Jason Pan on 2021-01-01 20:18:22
# Copyright © 2021 Jason Pan. All rights reserved.
#
if __name__ == '__main__':
    # 如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
    print(b'ABC'.decode('ascii'))

# 如果bytes中包含无法解码的字节，decode()方法会报错
# print(b'\xe4\xb8\xad\xff'.decode('utf-8'))

# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 长度    bytes 1个字节  utf-8 3个字节
print(len(b'ABC'))                      # 3.list和tuple
print(len('中文'))                    # 2
print(len('中文'.encode('utf-8')))    # 6

# 格式化   在Python中，采用的格式化方式和C语言是一致的，用%实现
print('Hi, %s, you have $%.2f' % ('Michael', 100.345))
# 占位符	替换内容
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数

# 用%%来表示一个%
print('growth rate: %d %%' % 7)

# f-string
r= 30
s=3.1415
print(f'The area of a circle with radius {r} is {s:.2f}')


