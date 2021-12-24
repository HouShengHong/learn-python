'''
else
與 if 使用 , if 條件表達不成立時 , 執行 else 
與 while 及 for 使用 , 沒碰到 break 時 , 執行 else
''' 
for _ in range(3) : 
    pwd=input('請輸入密碼 : ')
    if pwd == '8888' : 
        print('密碼正確')
        break
    else : 
        print('密碼不正確')
else : 
    print('對不起 , 三次密碼均輸入錯誤')