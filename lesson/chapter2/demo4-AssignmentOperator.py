#賦值運算符 Assignment Operator , 運算順序從右至左

print('------------鏈式賦值------------')

a=b=c=20
print("a=",a,'   id(a)=',id(a))
print("b=",b,'   id(b)=',id(b))
print("c=",c,'   id(c)=',id(c)) # 支持鏈式賦值 , 且賦予相同id

print('------------參數賦值------------')

i=10
i+=2          
print(i)      # i+=2 相當 i=i+2 , 所以得 12

o=35
o-=10
print(o)      # o-=10 相當 o=o-10 , 所以得 25

p=8
p*=5
print(p)      # p*=5 相當 p=p*5 , 所以得 40

s=16
s/=4
print(s)      
print(type(s)) # s/=4 相當 s=s/4 , 所以得 4.0 , 且結果為 float 

q=17
q//=4
print(q)      # q//=4 相當 q=q//4 , 所以得 4

print('------------系列解包賦值------------')

j,k,l=1,2,3
print('j,k,l=1,2,3')
print('j=',j)
print('k=',k)
print('l=',l)         # 支持系列解包賦值

# j,k=1,2,3           #ValueError , 因 變量的個數 需等同 值的個數

print('------------交換兩個變量的值------------')

n,m=3,4
print('n,m=3,4')
print('交換前','n=',n,'   m=',m)

print(end='\n')

n,m=m,n
print('n,m=m,n')
print('交換後','n=',n,'   m=',m)