# else

a = 0
while a < 3 : 
    pwd=input('請輸入密碼 : ')
    if pwd == '8888' : 
        print('密碼正碼')
        break
    else : 
        print('密碼不正確')
    a += 1 
else : 
    print('對不起 , 三次密碼均輸入錯誤')