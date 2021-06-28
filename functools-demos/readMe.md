### functools-demos functools模块的常用函数和场景
#### reduce
reduce.py
测试reduce逻辑，包含空list，list为复杂对象等情况
``` python
>>> from functools import reduce
>>> help(reduce)
Help on built-in function reduce in module _functools:

reduce(...)
    reduce(function, sequence[, initial]) -> value
    
    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
```
此处要注意的是 
- reduce需要传入3个参数，最后一个参数可默认不传，如果不传，则默认使用迭代器的第一个原始替换initial，
- 需要满足function的返回和迭代器的第一个原始是**同类型**，否则会报TypeError
- 若传递了第3个参数，这x会以第三个参数的类型出现，y是迭代器中的元素,同时function运算结果必须与第三个参数一致
```python
from functools import reduce
l = [{'value': i} for i in range(1, 10)]
# 赋予初始值
ret = reduce(lambda x, y: x + y['value'], l, 0)
print(ret) #45
```

#### partial
```python
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
```

- total_ordering
- update_wrapper
- wraps
- lru_cache
