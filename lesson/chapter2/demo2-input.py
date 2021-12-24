a=input('請輸入一個加數:')
b=input('請輸入一個被加數:')

print('a為',type(a),'b為',type(b))
print('兩數之合為',int(a)+int(b))  #由於 input 會轉成 <class 'str'> ,需將其轉成 int , 才得以進行整數計算

a=int(a) 
b=int(b) 
print('將a、b轉成 int ,','a為',type(a),'b為',type(b))
print('轉成int後的兩數之合',a+b) # 可直接將 a 、 b 轉成int