# 布林運算符 Boolean Operator 

a,b=1,2
print('''

----------------- and -----------------
''')
print('a='+str(a),'b='+str(b))
print('a==1 為',a==1,' ,  b==2 為',b==2,' ,  a==1 and b==2 為',a==1 and b==2,' ,  True and True --> True')
print('a==1 為',a==1,' ,  b!=2 為',b!=2,' ,  a==1 and b!=2 為',a==1 and b!=2,' ,  True and False --> False')
print('a!=1 為',a!=1,' ,  b==2 為',b==2,' ,  a!=1 and b==2 為',a!=1 and b==2,' ,  False and True --> False')
print('a!=1 為',a!=1,' ,  b!=2 為',b!=2,' ,  a!=1 and b!=2 為',a!=1 and b!=2,' ,  False and False --> False')
print('''
總結:
True and True --> True
True and False --> False
False and True --> False
False and False --> False
''')

print('''
----------------- or -----------------
''')

print('a='+str(a),'b='+str(b))
print('a==1 為',a==1,' ,  b==2 為',b==2,' ,  a==1 or b==2 為',a==1 or b==2,' ,  True or True --> True')
print('a==1 為',a==1,' ,  b!=2 為',b!=2,' ,  a==1 or b!=2 為',a==1 or b!=2,' ,  True or False --> True')
print('a!=1 為',a!=1,' ,  b==2 為',b==2,' ,  a!=1 or b==2 為',a!=1 or b==2,' ,  False or True --> True')
print('a!=1 為',a!=1,' ,  b!=2 為',b!=2,' ,  a!=1 or b!=2 為',a!=1 or b!=2,' ,  False or False --> False')

print('''
總結:
True or True --> True
True or False --> True
False or True --> True
False or False --> False
''')

print('''
----------------- not 對type of bool 取反-----------------
''')
print('not True 為',not True)
print('not False 為',not False)

print('''
----------------- in & not in -----------------
''')

print(''' 'p' in 'python' 為''','p' in 'python')
print(''' 'k' in 'python' 為''','k' in 'python')
print(''' 'p' not in 'python' 為''','p' not in 'python')
print(''' 'k' not in 'python' 為''','k' not in 'python')
