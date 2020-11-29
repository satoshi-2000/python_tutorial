# coding: utf-8

#Name : satoshi-2000
#Date : 2020/11/29
#Title:  repe_statement

#while  -break,continue
#for -range,array

##### 繰り返し文 #####

a = 3
list = ["札幌","横浜","さいたま","那覇","沼田"] #配列
tmp = 0

#5回繰り返し
while(tmp < 5):
    print(tmp)
    tmp += 1
"""
0
1
2
3
4
"""

#5回繰り返し(break)
tmp = 0
while(tmp < 5):
    if(tmp == a): #a=3の時にループを抜ける
        break
    print(tmp)
    tmp += 1
"""
0
1
2
""" 
 
#5回繰り返し(continue)
tmp = 0
while(tmp < 5):
    if(tmp == a): #a=3の時に処理を飛ばす
        continue
    print(tmp)
    tmp += 1

"""
0
1
2
4
"""

#for
for i in list:
    print(i)

"""
札幌
横浜
さいたま
那覇
沼田
"""


for i in range(5):
    print(i)

"""
0
1
2
3
4
"""