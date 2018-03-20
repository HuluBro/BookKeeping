'''
字典的内容是无顺序的，相当于一个查询表；列表是有顺序的
'''

dict = {'Alice': 'Name', '19': 'Birthday', 'Class': 'First'}

print dict['Alice']

dict['Class'] = 'Second'
dict['School'] = 'Ny'
#列出字典dict的所有条目
print dict.items()
#删除
del dict['Alice']
#以字符串表示dict
print str(dict)
#比较两键的值，0，-1
print cmp('19', 'Class')
print len(dict)
print dict
#列出字典dict的所有键
print dict.keys()

print dict.get('19')

#print dict.clear()
