# 按位運算符 BitwiseOperator , 需轉為二進制才能計算
print('''
5的二進制為00000101
9的二進制為00001001
''')
print('5&9 為',5&9,''', '&' 僅於 '二進制下同位置' 皆為1時才取1
''')

print('5|9 為',5|9,''', '|' 僅於 '二進制下同位置' 皆為0時才取0
''') # | = shift + \

print('5<<2 為',5<<2,''', '<<' 為 '二進制下向右位移' , 高位保留 , 低位補0
''')

print('5>>1 為',5>>1)
print('5>>2 為',5>>2,''', '>>' 為 '二進制下向左位移' , 低位刪除 , 高位補0
''')