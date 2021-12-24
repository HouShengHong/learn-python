# 比較運算符 ComparisonOperator , 比較運算符運算結果為 type of bool

a,b=10,20

print('a=',a,'  b=',b)
print(end='\n')
print('a<b',a<b)
print('a>b',a>b)
print('a<=b',a<=b)
print('a>=b',a>=b)
print('a==b',a==b)
print('a!=b',a!=b)


print('''
----------- '==' 與 'is' 之比較--------------
''')

a=10
b=10

lst1=[1,2,3,4]
lst2=[1,2,3,4]

print('a=',a,'  b=',b)
print('id(a)',id(a),'id(b)',id(b))
print('a==b',a==b)
print('a!=b',a!=b)
print('a is b  ',a is b)
print('a is not b  ',a is not b)

print(end='\n')

print('lst1=',lst1,'  lst2=',lst2)
print('lst1==lst2',lst1==lst2)
print('lst1!=lst2',lst1!=lst2)
print('id(lst1)=',id(lst1),'  id(lst2)=',id(lst2))
print('lst1 is lst2',lst1 is lst2)
print('lst1 is not lst2',lst1 is not lst2)

print('''
'==' 比較的是Value
'is' 比較的是id
''')