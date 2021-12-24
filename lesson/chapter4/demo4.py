'''
1. for-in 迴旋
     in 代表從 字符串 、 序列 等 中依次取值 , 又稱為肩遍歷
     for-in 遍歷的對象必須是可迭代對象 
2. for in 的語法結構
     for 自定義的變量 in 可迭代的對象 : 循環體
3. 若循環體內不需要訪問自定義變量 , 可將自定義變量替代為下劃線 
'''

for item in "Python" :
    print(item)

print('---------------------------')

for i in range(0,10,1) : 
    print(i)

print('---------------------------')

for _ in range(5) : 
    print('人生苦短,我用Python')

print("-----1-100的偶數和----------")

sum=0
for a in range(0,101,2) : 
    sum += a
print(sum)
