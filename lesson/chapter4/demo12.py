# 二重循環中 break 和 continue 只用於控制本層循環

# break 範例

for a in range(5) : 
    for b in range(1,11) : 
        if b % 2 == 0 : 
            break
        print(b)

#因 break 只打斷本層循環 , 故輸出 5 次 '1'

print('------------------------------')

# continue 範例

for a in range(5) : 
    for b in range(1,11) : 
        if b % 2 == 0 : 
            continue
        print(b,end='\t')
    print()
      