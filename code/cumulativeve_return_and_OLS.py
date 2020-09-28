import matplotlib as mpl
import pandas as pd
import seaborn as sns
import tushare as ts

# 获取数据
ts.set_token('07736625310e7ad7d310e33286b21ef7b5e834df0957d405588aac69')
pro = ts.pro_api()
wanke = pro.daily(ts_code='000002.SZ', start_date='20110101')
pingan = pro.daily(ts_code='601318.SH', start_date='20110101')
maotai = pro.daily(ts_code='600519.SH', start_date='20110101')
wanhua = pro.daily(ts_code='002415.SZ', start_date='20110101')
keda = pro.daily(ts_code='002230.SZ', start_date='20110101')
dong = pro.daily(ts_code='600776.SH', start_date='20110101')
guangda = pro.daily(ts_code='601788.SH', start_date='20110101')
hs300 = pro.index_daily(ts_code='000300.SH', start_date='20110101')

# 仅保留收益率数据，且用日期作为index
# 然后按照日期排序（增序）
stock_list = [wanke, pingan, maotai, wanhua, keda, dong, guangda, hs300]
for stock in stock_list:
    stock.index = pd.to_datetime(stock.trade_date)
df = pd.concat([stock.pct_chg / 100 for stock in stock_list], axis=1)
df.columns = ['wanke', 'pingan', 'maotai', 'wanhua', 'keda', 'dong', 'guangda', 'hs300']
df = df.sort_index(ascending=True)
df.describe()

# 累计收益率和方差情况
df = df.fillna(0)
returns = (df + 1).product() - 1
print('累计收益率：\n', returns)
print('\n标准差：\n', df.std())

# 收益率波动

sns.set()
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'SimHei'


rf = 1.032 ** (1/360) - 1
print(rf)

df_rp = df - rf
df_rp.head()
sns.pairplot(df_rp);

import statsmodels.api as sm

stock_names = {
    'wanke': '万科A',
    'pingan': '中国平安',
    'maotai': '贵州茅台',
    'wanhua': '万华化学',
    'keda': '科大讯飞',
    'dong': '东方通信',
    'guang': '光大证券'
}
for stock in ['wanke', 'pingan', 'maotai', 'wanhua', 'keda', 'dong', 'guang']:
    model = sm.OLS(df_rp[stock], sm.add_constant(df_rp['hs300']))
    result = model.fit()
    print(stock_names[stock] + '\n')
    print(result.summary())


