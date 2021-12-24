# 計算0-100之間的偶數和

sum=0
a=0
while a <= 100 :
    if not bool(a % 2)  : 
        sum+=a
    a+=1
print(sum)