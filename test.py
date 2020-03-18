import pandas as pd
import numpy as np
import datetime

# 解决列名无法对齐问题
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# Read data from excel file
# df = pd.read_excel(io="test.xlsx", sheet_name=1)
# # df = pd.read_excel(io="test.xlsx", parse_dates=["时间"])

# df["合计"] = df.apply(np.sum, axis=1)
# df.loc["合计"] = df.apply(np.sum, axis=0)
# df.loc["合计"] = df.apply(lambda x: x.sum())
# df["合计"] = df.apply(lambda x: x.sum(), axis=1)

# df["设备总价"] = df["设备数量"] * df["设备单价"]
# df.fillna(datetime.date.today(), inplace=True) 
# df["时间"] = pd.to_datetime(arg=df["时间"], format="%Y/%m/%d")
# df.index = ["项目A", "项目B", "项目C", "项目X"]
# print(df["设备总价"].sum())
# df['Col_sum'] = df.apply(lambda x: x.sum(), axis=1)
# print(df)
# print(df.dtypes)

data = pd.DataFrame(
    np.arange(16).reshape((4,4)),
    index=["北京", "上海", "西安", "成都"],
    columns=["智障数量", "天才数量", "逗逼数量", "脑残数量"])
print(data)
print(data[["智障数量", "天才数量"]])
print(data[:2])
print(data["逗逼数量"] > 5)
print(data[data["逗逼数量"] > 5])
print(data.loc[data["逗逼数量"] > 5])
print(data.loc[["北京", "上海"], ["智障数量","天才数量"]])
print(data.iloc[[0, 1], [0, 1]])
print(data.iloc[:, :3][data.智障数量 > 1])