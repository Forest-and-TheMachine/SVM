import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix, solvers

# DATA & LABEL
original_data = np.array([-3.0, -2.9, 0.5, 8.7, 2.9, 2.1, -0.1, 5.2, -4.0, 2.2,
                         -1.3, 3.7, -3.4, 6.2, -4.1, 3.4, -5.1, 1.6, 1.9, 5.1,
                         -2.0, -8.4, -8.9, 0.2, -4.2, -7.7, -8.5, -3.2, -6.7, -4.0,
                         -0.5, -9.2, -5.3, -6.7, -8.7, -6.4, -7.1, -9.7, -8.0, -6.3]).reshape(-1, 2)
x1_1, x2_1 = original_data[0:10, 0], original_data[0:10, 1]  # _1 代表属于第一类
x1_2, x2_2 = original_data[10:20, 0], original_data[10:20, 1]  # _2 就属于第二类

# plt.plot(x1_1, x2_1, 'g*', x1_2, x2_2, 'y^')
# plt.show()

# label, 第一类全是1， 第二类全是-1
a = np.ones((1,10))
label = np.concatenate((a, -a), axis=1)

# data pre-processing  [1, x1, x2, x1^2, x1*x2, x2^2]
data = np.zeros((20, 6))
data[:, 0] = np.ones(20)
data[:, 1] = original_data[:, 0]
data[:, 2] = original_data[:, 1]
data[:, 3] = original_data[:, 0] * original_data[:, 0]
data[:, 4] = original_data[:, 0] * original_data[:, 1]
data[:, 5] = original_data[:, 1] * original_data[:, 1]


class SVM:
    def __init__(self, x, y):

        self.data = x
        self.label = y
        self.threshold = 1e-4
        self.supportV = []

    def train(self, n):  # n 代表使用多少组数据， 每个样本 dim = 6
        N = 2*n   # 每组数据两类
        dim = 6  #  如果今后会换数据，这里需要改

        # 求解凸二次规划问题  参考《统计学习方法》 (7.13) and (7.14)
        P = matrix(np.identity(dim+1, dtype=np.float))
        P[0, 0] = 0

        q = matrix([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])  # 列数得符合dim+1， 以后有时间改成通用的  general version

        G = matrix(np.zeros((N, dim+1), dtype=np.float))
        Y = np.hstack((label[0, 0:n], label[0, 10:10+n]))
        G[:, 0] = matrix(-np.transpose(Y))
        X = np.vstack((data[0:n, :], data[10:10+n, :]))
        temp = np.identity(n, dtype=np.float)
        X_upper = -temp.dot(data[0:n, :])
        X_lower = temp.dot(data[10:10+n, :])
        X_temp = np.vstack((X_upper, X_lower))
        G[:, 1:dim+1] = matrix(X_temp)

        h = -matrix(np.ones((N,), dtype=np.float))

        # print(P)
        # print(q)
        # print(G)
        # print(h)
        sol = solvers.qp(P, q, G, h)

        # w, b
        b = sol['x'][0]
        w = np.zeros(dim, )
        for i in range(dim):
            if -self.threshold < sol['x'][i + 1] < self.threshold:
                w[i] = 0.0
            else:
                w[i] = sol['x'][i + 1]

        # 支持向量
        for j in range(N):
            v = Y[j] * (w.dot(np.transpose(X[j])) + b)
            if -self.threshold< v-1 < self.threshold:
                self.supportV.append(j)
        # print(self.supportV)

        return w, b


# S1 = SVM(data, label)
# w1, b1 = S1.train(1)
# print(w1)
# print(b1)
# print(S1.supportV)
#
# S2 = SVM(data, label)
# w2, b2 = S2.train(2)
# print(w2)
# print(b2)
# print(S2.supportV)
#
# S3 = SVM(data, label)
# w3, b3 = S3.train(3)
# print(w3)
# print(b3)
# print(S3.supportV)
#
# S4 = SVM(data, label)
# w4, b4 = S4.train(4)
# print(w4)
# print(b4)
# print(S4.supportV)

S10 = SVM(data, label)
w10, b10 = S10.train(10)
print(w10)
print(b10)
print(S10.supportV)