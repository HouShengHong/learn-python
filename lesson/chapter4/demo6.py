'''
break
用於結束循環體 , 通常 if 一同使用
'''
 #範例 : 從鍵盤輸入密碼 , 最多三次 , 如果正確就結束循環

for _ in range(3) : 
    pwd=input('請輸入密碼 : ')
    if pwd == '8888' : 
        print('密碼正確')
        break
    else : 
        print('密碼不正確')

    

     