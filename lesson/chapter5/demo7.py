'''
列表元素的刪除
.remove()  一次刪除一個元素 ; 重複元素只刪除第一個 ; 元素不存在 ValueError
.pop()     刪除一個指定索引位置上的元素 ; 若不指定索引 , 則刪除列表中最後一個元素 ; 指定索引不存在 IndexError 
切片       一次至少刪除一個元素
.clear()   清空列表
del list        刪除列表
'''

lst1=[10,20,30,40,50,60,30,]
lst1.remove(30)        # 一次刪除一個元素 ; 重複元素只刪除第一個
print(lst1)

# lst1.remove(100)     #元素不存在 ValueError

lst1.pop(1)
print(lst1)

lst1.pop()
print(lst1)            #若不指定索引 , 則刪除列表中最後一個元素

#lst1.pop(5)           #指定索引不存在 IndexError 

lst1[1:3]=[]           #切片 : 將原列表中的內容以 [] 替代
print(lst1)

lst1.clear()           #清空列表中的所有元素
print(lst1)

del lst1
#print(lst1)           # NameError: name 'lst1' is not defined