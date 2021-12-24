#轉義字符

print('hello\nworld') #\n為換行 n=newline

print('hello\tworld') 
print('helloooo\tworld') #\t 4字符串為一組,若不足以空格補齊

print('hello\rworld') #\r為回至啟始位置

print('hello\bworld') #\b為退一格

print('老師說\'大家好\'') #''中的''若需打印,需添加\' \' 
#print('老師說'大家好'')  #SyntaxError

print(r'hello\nworld') #若不希望轉義字符作用,需於字符串前添加 r 或 R
#print(r'hello\nworld\') #SyntaxError
print(r'hello\nworld\\') #若字符串最後為\,需多添加\