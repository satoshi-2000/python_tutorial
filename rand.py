# coding: utf-8

#Name : satoshi-2000
#Date : 2020/11/29
#Title:  rand

#random()
#uniform()

#この他にも
#seed()で乱数を固定
#random.gauss(),random,betavariate()
#一様分布以外の分布に従う乱数も生成
#などの機能がある

##### 乱数 #####

import random #乱数を扱う

print(random.random())
"""
[0,1}の乱数(float型)

"""

print(int(100 * random.random()))

"""
[0,100}の乱数(int型)
"""

#a,bに型指定はない
a = 5
b = 10
print(random.uniform(a,b))


"""
[5,10]の乱数(float型)
(a,b)は(b,a)でも良い()
"""
