#print之應用

#可輸出整數
print(520) 

#可輸出小數
print(98.5) 
print(8.5)

#可輸出字符串
print('Hello world') 

#可輸出含有運算符的表達式
print(3+1) 

#可將數據輸出至文件中，注意：所指定位置存在 and 使用 file=a
a=open('C:/Users/qaz97/Desktop/python/lesson/text.txt','a+') #a+如困文件不存在就創建，存在就追加文件內容
print('Hello world',file=a)
a.close()
