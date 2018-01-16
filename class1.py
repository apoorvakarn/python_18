# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 12:52:47 2018 by Apoorva Karn"""



#list
x= [1,2,3]
x
x
print(x)
l=eval(input("enter a list"))
l
rollnos= [1,2,3,4,5,6,10,11]
rollnos[0]
rollnos[8]
rollnos[7]
len(rollnos)
sum(rollnos)
min(rollnos)
max(rollnos)
rollnos
for i in range (len(rollnos)):
    print(rollnos[i],end = ',')
if 3 in rollnos:
    print("yes")
if 7 in rollnos:
    print("yes")
else:
    print("no")
    
rollnos.append(13)
rollnos
sorted(rollnos)
rollnos.index(13)# for value
rollnos.reverse
sorted(-(rollnos))
