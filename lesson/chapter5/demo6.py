''''
列表元素的增加
.append() 在列表的末尾添加一個元素
.extend() 在列表的末尾至少添加一個元素
.insert() 在列表的任意位置添加一個元素
切片      在列表的任意位置添加至少一個元素

------------以上方法 , 皆不產生新的id-----------
'''

lst1=[10,20,30]
print(lst1)
print(id(lst1))


lst1.append(100)
print(lst1)
print(id(lst1))


lst2=['hello','world']
# lst1.append(lst2)       #將 lst2 做為一個元素添加到末尾
lst1.extend(lst2)         #向列表的末尾一次性添加多個元素
print(lst1)    
print(id(lst1))   

lst1.insert(1,90)         #在指定的位置添加一個元素
print(lst1)
print(id(lst1))

lst3=[True,False,'world']
lst1[1:]=lst3
print(lst1)
print(id(lst1))
