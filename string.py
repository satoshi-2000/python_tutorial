# coding: utf-8

#Name : satoshi-2000
#Date : 2020/12/3
#Title: string

##### 文字列 #####

#文字列置換

a = 'game'
b = 'video'
ex = 'You say hello and I say hello'

#文字数
print(len(a))   #4

#連結
print(a + b)    #gamevideo

#繰り返し
print(a * 3)    #gamegamegame

#置換
print(ex.replace('say','soy'))  #You soy hello and I soy hello
print(ex.replace('hello','hi')) #You say hi and I say hi

#1文字ずつ処理
print(list(a))  #['g', 'a', 'm', 'e']