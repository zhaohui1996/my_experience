
"""
机器学习4步:
    1.准备数据
    2.训练模型并实现可视化
    3,评估模型
    4.保存模型,并应用模型
"""
import numpy as np
import matplotlib.pyplot as plt

#样本准备
train_X = np.linspace(-1, 1, 100)#随机取100个-1到1之间的数
train_Y = 2 * train_X + np.random.randn(*train_X.shape) * 0.3 # y=2x，但是加入了噪声(y=2*x+a*0.3)
#显示模拟数据点
plt.plot(train_X, train_Y, 'ro', label='Original data')#设置一个标签名(原始数据)
plt.legend()#作图
plt.show()

#模型训练及可视化
from sklearn.linear_model import LinearRegression
model = LinearRegression()#模型实例化
model.fit(train_X.reshape(100,1),train_Y.reshape(100,1))#传入训练样本
print("输入6，的模型预测结果：",model.predict(6))#输入6预测结果
print("线性模型的斜率与截距：",model.coef_,model.intercept_)#求斜率和截距
#y = kx+b
print("使用斜率与截距的计算结果：",model.coef_*6 +model.intercept_ )#y=6k+b


plt.plot(train_X, train_Y, 'ro', label='Original data')
plt.plot(train_X, model.predict(train_X.reshape(100,1)), label='Fitted line')
plt.legend()
plt.show()


#模型评估
X_test = np.linspace(11,20,20)#生成测试样本
Y_test =  2 * X_test + np.random.randn(*X_test.shape) * 0.3
print("模型评估的分值：",model.score(X_test.reshape(20,1),Y_test.reshape(20,1)))#分数越高,越准确



#模型保存，及应用
from sklearn.externals import joblib#导包
joblib.dump(model, "train_model.m")#保存模型,在代码的同级文件下
model = joblib.load("train_model.m")#载入模型
print("导入模型，并输入6得到的预测结果：",model.predict(6))#使用模型