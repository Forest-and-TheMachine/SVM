import numpy as np
import matplotlib.pyplot as plt
from cvxopt import matrix, solvers


# 实验给定的所有数据点，reshape成了20*2的矩阵，前10个是第一类，后10个是第二类
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
        '''

        :param x: 数据, 2个点，一类一个
        :param y: 标签
        '''
        self.data = x
        self.label = y
    '''
        # 实验第一问
    def q1(self):
        X = np.vstack((self.data[0, :], self.data[10, :]))
        Y = np.vstack((self.label[0,0], self.label[0, 10]))
        # [[ 1.   -3.   -2.9   9.    8.7   8.41]
        #  [ 1.   -2.   -8.4   4.   16.8  70.56]]
        XXT = X.dot(np.transpose(X))  # a 2by2 matrix
        YYT = Y.dot(np.transpose(Y))


        P = matrix(XXT * YYT)   # 系数矩阵， Cij = yi*yj*xi*xj
        q = matrix([-1.0, -1.0])
        G = matrix([[-1.0, 0.0], [0.0, -1.0]])
        h = matrix([0.0, 0.0])
        A = matrix([1, -1], (1,2), 'd')
        b = matrix(0.0)

        sol = solvers.qp(P, q, G, h, A, b)
        alpha = sol['x']
        print(alpha)

        w = 


S = SVM(data, label)
S.q1()
    '''

# 求解对偶问题
X = np.vstack((data[0, :], data[10, :]))
Y = np.vstack((label[0,0], label[0, 10]))
# [[ 1.   -3.   -2.9   9.    8.7   8.41]
#  [ 1.   -2.   -8.4   4.   16.8  70.56]]
XXT = X.dot(np.transpose(X))  # a 2by2 matrix
YYT = Y.dot(np.transpose(Y))


P = matrix(XXT * YYT)   # 系数矩阵， Cij = yi*yj*xi*xj
q = matrix([-1.0, -1.0])
G = matrix([[-1.0, 0.0], [0.0, -1.0]])
h = matrix([0.0, 0.0])
A = matrix([1, -1], (1,2), 'd')
b = matrix(0.0)

sol = solvers.qp(P, q, G, h, A, b)
alpha = sol['x']
print(alpha)

w = alpha[0]*X[0] - alpha[1]*X[1]


# 原问题
P1 = matrix(np.identity(7, dtype=np.float))
P1[0,0] = 0
q1 = matrix([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
G1 = matrix(np.zeros((2, 7), dtype=np.float))
h1 = matrix([-1.0, -1.0])
G1[:, 0] = matrix(Y)
temp1 = np.vstack((Y[0]*X[0], Y[1]*X[1]))
G1[:, 1:7] = matrix(temp1)
sol1 = solvers.qp(P1, q1, -G1, h1)
print(sol1['x'])


# w, b
threshold = 1e-8
b1 = sol1['x'][0]
w1 = np.zeros(6, )
for i in range(6):
    if -threshold < sol1['x'][i+1] < threshold:
        w1[i] = 0.0
    else:
        w1[i] = sol1['x'][i+1]
print(w1)

# 支持向量
supportV = []
for j in range(2):
    v = Y[j]*(w1.dot(np.transpose(X[j]))+b1)
    if v < (1 + threshold):
        supportV.append(j)
print(supportV)

print(P1)
print(q1)
print(-G1)
print(h1)