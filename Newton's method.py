# 牛顿迭代法
import math
import sys


def f(xe):
    y = xe * math.e ** xe - 1
    return y


def df(xe):
    dy = (math.e ** xe) + xe * (math.e ** xe)
    return dy


x = 0.5  # x的值在0.5附近
k = 0    # 迭代次数计数
e = 0.0000001  # 误差要求
N = 1000       # 最大迭代次数

while k < N:
    if df(x) == 0:
        print("初始值错误")
        sys.exit()
    x1 = x - f(x) / df(x)
    if abs(x1 - x) < e:
        print("方程的解为:%f" % x1)
        sys.exit()
    else:
        k = k + 1
        x = x1

print("计算失败")
