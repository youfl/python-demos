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

from functools import partial


def func(a, b, c, d=5):
    return (a + b) * c - d


def test_partial():
    f1 = partial(func, 3)
    f2 = partial(func, 3, 2)
    f3 = partial(func, 3, 2, 3)
    f4 = partial(func, 3, 2, 3, 5)

    print(f1(2, 3))  # 10
    print(f2(3))  # 10
    print(f3())  # 10
    print(f4())  # 10


if __name__ == '__main__':
    test_partial()
