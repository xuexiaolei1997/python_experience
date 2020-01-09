'''
随机梯度下降
在样本中进行随机挑选
'''
import numpy as np
import pandas as pd

# import data
train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
submit = pd.read_csv('data/sample_submit.csv')

# initialize variable
beta = [1, 1]  # basic value
alpha = 0.2  # learning rate
tol_L = 0.1  # threshold 阈值

# 归一化x,用每个值除个数，使得所有自变量相加为0
max_x = max(train['id'])
x = train['id']/max_x
y = train['questions']


def compute_grad_SGD(beta, x, y):
  grad = [0, 0]
  r = np.random.randint(0, len(x))
  grad[0] = 2. * np.mean(beta[0] + beta[1] * x[r] - y[r])
  grad[1] = 2. * np.mean(x[r] * (beta[0] + beta[1] * x[r] - y[r]))
  return np.array(grad)


def update_beta(beta, alpha, grad):
  new_beta = np.array(beta) - alpha * grad
  return new_beta


def rmse(beta, x, y):
  squared_err = (beta[0] + beta[1] * x - y) ** 2
  res = np.sqrt(np.mean(squared_err))
  return res


np.random.seed(10)
grad = compute_grad_SGD(beta, x, y)
loss = rmse(beta, x, y)
beta = update_beta(beta, alpha, grad)
loss_new = rmse(beta, x, y)

# 迭代
i = 1
while np.abs(loss_new - loss) > tol_L:
  beta = update_beta(beta, alpha, grad)
  grad = compute_grad_SGD(beta, x, y)
  if i % 100 == 0:
    loss = loss_new
    loss_new = rmse(beta, x, y)
    print('Round %s Diff RMSE %s'%(i, abs(loss_new - loss)))
  i += 1
print('Coef: %s \nIntercept %s'%(beta[1], beta[0]))
