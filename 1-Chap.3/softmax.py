import numpy as np


# 일반 소프트맥스
def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y


# 개선된 소프트 맥스( 1000이상만 돼도 nan값이 나와 최대값을 빼주어 계산
def up_softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y


a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
up_y = up_softmax(a)
print(y)
print(up_y)
