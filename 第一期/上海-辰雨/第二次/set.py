#!/usr/bin/env python
# encoding: utf-8

# set 是python 的基本数据类型，它有可变集合(set())和不可变集合(frozenset)两种,其是要特性如下：
# 其存储的元素是无序的；
# 其存储的元素是不重复的；


# set方法：
# 在python 中,通过add方法来给set 新增新的元素,如果添加重复元素,会被自动过滤掉，即添加没有任何的效果：
# add:新增一个元素到set中；
# remove:从set中删除指定的元素；
# clear:清空set集合
# update:用于更新多个元素值,参数为list
# issubset:用法s1.issubset(s2),判断s1中的每个元素是否都在s2中，即s1<-s2
# issuperset:用法s1.issuperset(s2),判断s2中的每个元素是否都在s1中，即s1>=s2
# union：并集，返回两个集合的并集；
# intersetction:交集，返回两个集合的交集
# difference:用法s1.difference(s2)，返回s1中有s2中没有的元素；


set_source = set([1,1,2,3,4,5,6,7])
set_demo = set([1,1,2,3,4,5,6,7])

print (u'原始数据:')
print (set_demo)

#add 方法，新增元素：
print (u'add后:')
set_demo.add(9)
set_demo.add(1)

print set_demo

#remove 删除元素：
print (u'remove后:')
set_demo.remove(9)

print (set_demo)


#update 新增多个元素值：
list_demo = ['a','b','c']
set_demo.update(list_demo)

print (u'upate后:')
print (set_demo)
