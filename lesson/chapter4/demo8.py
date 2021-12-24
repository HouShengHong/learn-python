'''
continue
用於結束當前循環 , 進入下一個循環 , 通常與 if 一起使用
'''
#範例 : 輸出 1 - 50 之間所有 5 的倍數 , 並使用 continue

for a in range(1,51) : 
    if a % 5 == 0 : 
        print(a)

print('----------使用 continue -------------')

for a in range(1,51) : 
    if a % 5 != 0 :
        continue 
    print(a)