'''
獲取列表中的單個元素
  1.正向索引 : 從 0 到 N-1 , 舉例 lst[0]
  2.逆向索引 : 從 -N 到 -1 , 舉例 lst[-1]
  3.指定索引不存在 , 拋出IndexError
'''
lst1=['hello','world',98,'hello','world',234]
print(lst1[2])
print(lst1[-3])
#print(lst1[10])   #IndexError: list index out of range