#type ot string

str1='人生苦短,我用python'
str2="人生苦短,我用python" 
# '' and ""  二者功能相同,且只能用於單行

str3='''人生苦短,
我用python'''
str4="""人生苦短,
我用python"""      
# '''''' and """"""" 二者功能相同,且可換行

print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))