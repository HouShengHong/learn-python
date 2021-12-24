'''
列表元素的排序操作

.reverse()           列表中的元素反轉
.sort()              升序排序
.sort(reverse=True)  降序排序
'''


lst1=[20,40,10,98,54]
print('排序前的列表',lst1)

lst1.reverse()
print('反轉後的列表',lst1)

lst1.sort()
print('升序排序後的列表',lst1)

lst1.sort(reverse=True)
print('降序排序後的列表',lst1)

print('------使用內置函數 sorted() 對列表進行排序 , 將產生一個新的列表對象-----------')

lst1=[20,40,10,98,54]
print(lst1,id(lst1))

lst1=sorted(lst1)                   #升序排序
print(lst1,id(lst1))                  

lst1=sorted(lst1,reverse=True)      #降序排序
print(lst1,id(lst1))