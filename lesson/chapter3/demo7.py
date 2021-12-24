# 條件表達式
# "X" if ... else .... "Y"
# 範例 : 比較兩整數

'''
a = int(input("請輸入第一個整數"))
b = int(input("請輸入第二個整數"))
if a >= b :
    print(a,'大於等於',b)
else :
    print(a,'小於',b)
'''

a = int(input("請輸入第一個整數"))
b = int(input("請輸入第二個整數"))

#                    (執行左方)<--True  False-->(執行右方)  
print( str(a)+'大於等於'+str(b)  if a >= b else  str(a)+'小於'+str(b) )                             