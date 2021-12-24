''''
判斷 key 是否於字典中存在     : in 和 not in 
刪除指定 key-value           : del dic[key]
新增 or 修改 key-value       : dic['newkey'] = newvalue
清空字典元素                 : dic.clear()

'''

scores={'張三' : 100 , '李四' : 98 , '王五' : 45}
print('張三' in scores)
print('張三' not in scores)

del scores['張三']
print(scores)

scores['陳六'] = 98
print(scores)

scores['陳六'] = 100
print(scores)

scores.clear()
print(scores)