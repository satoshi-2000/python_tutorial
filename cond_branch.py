# coding: utf-8

#Name : satoshi-2000
#Date : 2020/11/29

#pythonにはswitch文が存在しないため, if,elif,elseによって条件分岐を行う

##### 条件分岐 #####

a = 5
b = 10
c = 15
num = 10

#小さいほうを出力する条件分岐
if(a < b):
    print(a)
else:
    print(b)
#5

#elifを含む条件分岐
if(a > b):
    print(a)
elif(b > c):
    print(b)
else:
    print(c)
#15