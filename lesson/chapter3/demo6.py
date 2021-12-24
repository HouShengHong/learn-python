# 嵌套 if

'''
範例 : 購物
  會員     >=200  打8折
           >=100  折9折
           100>   不打折 

  非會員   >=200  打9.5折
           200>   不打折
'''

a=input("您是會員嗎?y/n ")
b=float(input('請輪入消費金額'))
if a == 'y' :
    print("會員")
    if b >= 200 :
        print('付款金額為',b * 0.8)
    elif b >= 100 :
        print('付款金額為',b * 0.9)
    else :
        print('付款金額為',b)
else :
    print('非會員')
    if b >= 200 :
        print('付款金額為',b * 0.95)
    else : 
        print('付款金額為',b)