'''
獲取列表中指定元素的索引 - .index()
  1.若列素中有個峃同元素 , 只返回相同元素中的第一個元素索引
  2.若查詢的元素不在列表中 , 則會拋出 ValueError
  3.還可以在指定的start和stop之間進行查找
'''

lst1=['hello','world',98,'hello']

print(lst1.index('hello'))     #若列素中有個峃同元素 , 只返回相同元素中的第一個元素索引
# print(lst1.index('Python'))  #若查詢的元素不在列表中 , 則會拋出 ValueError
print(lst1.index('hello',1,4)) #還可以在指定的start和stop之間進行查找