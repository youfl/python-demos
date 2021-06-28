#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    @Version:  python 3.7.2
    @FileName: config.py
    @Author:   youfl
    @Email:    393639665@qq.com
    @Time:     2021-06-28 15:06
    @Description:
"""


from functools import reduce

def test_list():
    '''
    测试迭代器中为简单类型的问题
    :return:
    '''
    l = range(1, 10)
    # 不赋予初始值
    ret = reduce(lambda x,y: x+y, l)
    print(ret) #45

    # 赋予初始值为100
    ret = reduce(lambda x, y: x + y, l, 100)
    print(ret) #145

    # 空数组情况1, 不赋予初始值
    ret = reduce(lambda x, y: x + y, [])
    print(ret)  # TypeError: reduce() of empty sequence with no initial value

    #空数组情况2
    ret = reduce(lambda x, y: x + y, [], 0)
    print(ret)  # 0

def test_list_dict():
    '''
    测试迭代器中为复杂对象的问题
    :return:
    '''
    l = [{'value': i} for i in range(1, 10)]

    # 赋予初始值
    ret = reduce(lambda x, y: x + y['value'], l, 0)
    print(ret) #45

    # 不赋予初始值
    ret = reduce(lambda x,y: x+y['value'], l)
    # TypeError: unsupported operand type(s) for +: 'dict' and 'int'
    print(ret)

if __name__ == '__main__':
    #test_list()
    test_list_dict()



