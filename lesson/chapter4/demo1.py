'''
range的三種創建方式
range(stop)
range(start,stop)
range(start,stop,step)
'''

# range(stop)
r=range(10)
print(r)         #range(0, 10)  
print(list(r))   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  默認 start=0 , step=1

# range(start,stop)
r=range(1,10)
print(r)         #range(1, 10)
print(list(r))   #[1, 2, 3, 4, 5, 6, 7, 8, 9]     默認 step=1

# range(start,stop)
r=range(1,10,2)
print(r)         #range(1, 10, 2)
print(list(r))   #[1, 3, 5, 7, 9]                

# 判斷指定對象是否存在於序列中 , 用 in,not in
print(9 in r)
print(10 in r)
print(9 not in r)
print(10 not in r)