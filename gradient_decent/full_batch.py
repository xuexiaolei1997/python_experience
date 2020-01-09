'''
全批量梯度下降
使用最小二乘法
'''
import pandas as pd
import numpy as np

# import data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
submit = pd.read_csv('data/sample_submit.csv')

# initialize variable
beta = [1, 1]  # basic value
alpha = 0.2  # learning rate
tol_L = 0.1  # threshold 阈值

# 归一化x,用每个值除总个数，使得所有自变量相加为1
max_x = max(train['id'])
x = train['id']/max_x
y = train['questions']


def compute_grad(beta, x, y):
  grad = [0, 0]
  grad[0] = 2. * np.mean(beta[0] + beta[1] * x - y)
  grad[1] = 2. * np.mean(x * (beta[0] + beta[1] * x - y))
  return np.array(grad)


def update_beta(beta, alpha, grad):
  new_beta = np.array(beta) - alpha * grad
  return new_beta


def rmse(beta, x, y):
  squared_err = (beta[0] + beta[1] * x - y) ** 2
  res = np.sqrt(np.mean(squared_err))
  return res


# 第一次计算
grad = compute_grad(beta, x, y)
loss = rmse(beta, x, y)
beta = update_beta(beta, alpha, grad)
loss_new = rmse(beta, x, y)

# loop
i = 0
while np.abs(loss_new - loss) > tol_L:
  beta = update_beta(beta, alpha, grad)
  grad = compute_grad(beta, x, y)
  loss = loss_new
  loss_new = rmse(beta, x, y)
  i += 1
  print('Round %s Diff RMSE %s' % (i, abs(loss_new - loss)))
print('Coef %s \nIntercept %s' % (beta[1], beta[0]))
