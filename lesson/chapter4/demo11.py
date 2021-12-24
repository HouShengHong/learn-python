#嵌套循環

#範例 : 輸出一個 3 行 4 列 的矩形

for _ in range(3) : 
    for _ in range(4) : 
        print('*',end=" ")
    print()

print('---------------------------------')

#輸出 九九乘法表

for a in range(1,10) : 
    for b in range(1,a+1) : 
        print(str(a)+'*'+str(b)+'='+str(a*b),end='\t')
    print()