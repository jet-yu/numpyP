# -*-coding:utf-8-*-
#@see https://zhuanlan.zhihu.com/p/32242331

import numpy as nu

a = nu.arange(15).reshape(3, 5)
print(a)

print(a.shape)
print(a.size)
# 轴或者秩
print(a.ndim)
print(type(a))

b = nu.arange(10)
print(b)
print(type(b))
print(b.dtype)

print("-------c------")
c = nu.array([10.1, 10.2, 10.3])
print(c)
print(c.dtype)

print("-------d------")
d = nu.array([[10.1, 10.2, 10.3], [1.0, 20.0, 3.0]])
print(d)
print(d.size)
print(d.dtype)

# 矩阵行数列数 返回矩阵的shape的行列
print(d.shape[0])
print(d.shape[1])

# 矩阵按行列选取
print(d[0:2, 0:3])

print("-------按条件截取------")
# 矩阵按条件截取
print(d[d > 6])
print(d > 6)
d[d > 6] = 0
print(d)
