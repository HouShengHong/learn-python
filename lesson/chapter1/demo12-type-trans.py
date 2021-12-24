#type 轉換

name='侯佳君'
age=28
print(name,type(name))
print(age,type(age))

#print('我叫'+name+',今年'+age+'歳')  # TypeError , 唯同type,才能使用+連結

print('我叫'+name+',今年'+str(age)+'歳')


print('--------#str() 將其他type轉成 type of string-------------')
a1=2
a2=3.5
a3=False
print(type(a1),type(a2),type(a3))
print(str(a1),type(str(a1)))
print(str(a2),type(str(a2)))
print(str(a3),type(str(a3)))

print('--------#int() 將其他type轉成 type of integer-------------')
b1=98.7
b2='98'
b3='98.7'
b4=True
b5='hello world'
print(b1,type(b1))
print(b2,type(b2))
print(b3,type(b3))
print(b4,type(b4))
print(b5,type(b5))

print(int(b1),type(int(b1))) #將float轉成int,小數點後拾去
print(int(b2),type(int(b2))) #將str轉成int,str需為數字串
#print(int(b3),type(int(b3))) #ValueError , str轉成int , 僅能 整數 字串
print(int(b4),type(int(b4))) #True將轉成 1 
#print(int(b5),type(int(b5))) #ValueError , str轉成int , 僅能 整數 字串
 
print('--------#float() 將其他type轉成 type of float-------------') 
c1=98
c2='98'
c3='98.7'
c4=False
c5='hello world'
print(c1,type(c1))
print(c2,type(c2))
print(c3,type(c3))
print(c4,type(c4))
print(c5,type(c5))

print(float(c1),type(float(c1))) # int 可轉成 float , 並加.0 
print(float(c2),type(float(c2))) # 整數str 可轉成 float , 並加.0
print(float(c3),type(float(c3))) # 小數str 可轉成 float 
print(float(c4),type(float(c4))) # bool 可轉成 float , 並加.0
#print(float(c5),type(float(c5))) # ValueError , 若 str 欲轉成 float , 需為 數字str