''' 
while 迴旋結構
1.初始化變量
2.條件判斷
3.條件執行體(循環體)
4.改變變量
'''

print("---------------if--------------")
a=0
if a < 10 :        # if 判斷 1 次 , 條件為 True 執行 1 次
    print(a)
    a+=1

print("---------------while--------------")

while a < 10 :     # while 判斷 N+1 次 , 條件為 True 執行 N 次
    print(a)
    a+=1

print("---------------while應用(0-10之和)--------------")
sum = 0  #存儲累加和
a = 1
while a < 11 :
    sum += a
    a += 1
print(sum)

