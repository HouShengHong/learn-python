'''
獲取列表中的多個元素
語法結構 : 列表名[start,stop,step]

切片操作 : 
  1.切片的結果 : 原列表片段的拷貝
  2.切片的範圍 : [start:stop]
  3.step : 默認為 1
  5.start : 默認為 0
  4.stop : 默認到最後
'''

lst1=[0,1,2,3,4,5,6,7]
print('原列表',id(lst1))
print('切片',lst1[1:6:2],id(lst1[1:6:2])) # 切片創建新 id

print(lst1[1:6:2])

print(lst1[1:6])
print(lst1[1:6:])    # step 默認為 1

print(lst1[:6:1])     #start 默認為 0

print(lst1[1::1])     # stop 默認到最後

print(lst1[::])

print('---------------------step為負數--------------------------')

print('原列表',lst1[::])
print('step = -1',lst1[::-1])

print(lst1[6::-1])    # 6 到 第一個

print(lst1[:2:-1])    # 最後一個 到 2

print(lst1[1:6:-1])  #[]空列表
print(lst1[6:1:-1])