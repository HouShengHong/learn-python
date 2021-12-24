# bool()的應用

age = int(input('請輸入您的年齡 : '))
if age :
    print(age)                #當年齡不為0時 , bool() 為 True , 所以執行 if 
else : 
    print('年齡為',age)       #當年齡為0時 , bool() 為 False , 所以執行 else