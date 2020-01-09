'''
小批量随机梯度下降
'''
import pandas as pd
import numpy as np

# 导入数据
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
submit = pd.read_csv('sample_submit.csv')

# 初始设置
beta = [1, 1]
alpha = 0.2
tol_L = 0.1
batch_size = 16

# 对x进行归一化
max_x = max(train['id'])
x = train['id'] / max_x
y = train['questions']

# 定义计算mini-batch随机梯度的函数
def compute_grad_batch(beta, batch_size, x, y):
    grad = [0, 0]
    r = np.random.choice(range(len(x)), batch_size, replace=False)
    grad[0] = 2. * np.mean(beta[0] + beta[1] * x[r] - y[r])
    grad[1] = 2. * np.mean(x[r] * (beta[0] + beta[1] * x[r] - y[r]))
    return np.array(grad)

# 定义更新beta的函数
def update_beta(beta, alpha, grad):
    new_beta = np.array(beta) - alpha * grad
    return new_beta

# 定义计算RMSE的函数
def rmse(beta, x, y):
    squared_err = (beta[0] + beta[1] * x - y) ** 2
    res = np.sqrt(np.mean(squared_err))
    return res

# 进行第一次计算
np.random.seed(10)
grad = compute_grad_batch(beta, batch_size, x, y)
loss = rmse(beta, x, y)
beta = update_beta(beta, alpha, grad)
loss_new = rmse(beta, x, y)

# 开始迭代
i = 1
while np.abs(loss_new - loss) > tol_L:
    beta = update_beta(beta, alpha, grad)
    grad = compute_grad_batch(beta, batch_size, x, y)
    if i % 100 == 0:
        loss = loss_new
        loss_new = rmse(beta, x, y)
        print('Round %s Diff RMSE %s'%(i, abs(loss_new - loss)))
    i += 1
print('Coef: %s \nIntercept %s'%(beta[1], beta[0]))