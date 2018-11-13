# from sklearn.manifold import TSNE
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.family'] = 'STSong'#让图示功能支持中文

import pandas as pd

df = pd.read_csv("d://fei/stock//600000_20180730.csv", encoding="gbk")#打开文件
print(df.head(1))  # 输出部分信息,参数1 的意思是第一条
df.plot()  # 图示

price = df[['日期', '收盘价']]  # 选取关注列
print(price[:5])  # 输出部分信息
price.columns = ["data", 'price']  # 修改列名
print(price[:5])  # 输出部分信息

df_new = df[['日期', '开盘价', '收盘价']].set_index('日期')  # 修改索引
print(df_new[:5])  # 输出部分信息
df_new['收盘价'][:20].plot(kind='bar')  # 以直方图形式显示
df_new[:20].plot()  # 以折线图形式显示