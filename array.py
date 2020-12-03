# coding: utf-8

#Name : satoshi-2000
#Date : 2020/12/3
#Title: array

#よく使われるものとして, 純粋なlistとnumpyがある.
#多くのコードでは import numpy as np と略称される.

##### 配列 #####

import random #乱数を扱う
import numpy as np

#空の配列
array = []
array2 = []
print(array)

#配列に乱数を代入
for i in range(10):
    array.append(random.random())  #要素の追加にはappendメソッドが便利

#配列の表示
print(array,array2) #','区切りで配列を表示することも可能
#配列のコピー
array2 = array
print(array2)

"""
[](空白の配列)
[0,1}の要素を表示
[0.5446811278895243, 0.12997608414527262, 0.5652084149031175, 0.2696319771437381, 0.04763033185644083, 0.09912631980645925, 0.4514149540075483, 0.7129134683400777, 0.9249338773863957, 0.42680377419977533] []
コピーされた配列を表示
[0.5446811278895243, 0.12997608414527262, 0.5652084149031175, 0.2696319771437381, 0.04763033185644083, 0.09912631980645925, 0.4514149540075483, 0.7129134683400777, 0.9249338773863957, 0.42680377419977533]

"""

#numpy配列(ndarray)
a = np.array([1,2,3])
b = np.array([1,2,3])

#各要素について四則演算
print(a - b)    #[0,0,0]
print(a + b)    #[2,4,6]
print(a * b)    #[1,4,9]
print(a / b)    #[1.1.1.]

#ブロードキャスト
print(a - 2)    #[-1,0,1]
print(a + 2)    #[3,4,5]
print(a * 2)    #[2,4,6]
print(a / 2)    #[0.5 1. 1.5]

#形表示
print(a.shape)  #(3,)

#型表示
print(a.dtype)  #int32