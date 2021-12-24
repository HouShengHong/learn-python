'''
字典中元素的獲取
1.dic[key]           #若 key 不存在 , KeyError 
2.dic.get(key)       #若 key 不存在 , 輪出 None ; 可以通過參數設定默認value , 以便指定的 key 不存在時返回
'''

scores={'張三' : 100 , '李四' : 98 , '王五' : 45}

print(scores['張三'])
#print(scores['陳六'])  # KeyError

print(scores.get('張三'))
print(scores.get('陳六'))  #None
print(scores.get('張三',99))
print(scores.get('麻七',99))