---
title: Pandas数据预处理
date: 2020-02-24 09:27:24
img: https://raw.githubusercontent.com/JokerLJZ/Image/master/宾果1.jpg
categories: Python
summary: 对Pandas DataFrame数据进行预处理
author: 火柴人
tags:
  - Python
  - Pandas
  - DataFrame
---

## 1. 原始数据表

创建测试数据表 test.xlsx：

| 时间       | 项目经理 | 预算  | 设备数量 | 设备单价 |
| :--------- | :------- | :---- | :------- | -------- |
| 2020-01-24 | 张三     | 2670  | 2        | 1000     |
| 2019-12-27 | 李四     | 283.1 | 3        | 80       |
| 2019-12-27 | 王二     | 0     | 1        | 0        |
|            | 张三     | 25    | 4        | 5        |

## 2. 读取数据表获取DataFrame并进行数据预处理

1. 直接使用read_excel()获取test.xlsx的dataframe格式数据

```python
import pandas as pd
import datetime

# 从EXCEL文件中读取数据并打印column类型
df = pd.read_excel(io="test.xlsx")
print(df.dtypes)
```

```
# 输出 DataFrame

        时间  项目经理    预算  设备数量  设备单价
0 2020-01-24     张三  2670.0        2     1000
1 2019-12-27     李四   283.1        3       80
2 2019-12-27     王二     0.0        1        0
3        NaN     张三    25.0        4        5

# 输出column类型

时间         object
项目经理     object
预算        float64
设备数量      int64
设备单价      int64
```

根据输出结果可以查看数据类型及，接下来要对数据的格式及形势进行预处理，以满足数据分析的需求。下面分几个步骤针对几种场景做数据预处理

2. 新增Column列设备价格，需要每行数据都进行一次设备数量×设备单价并新增Column索引

```python
df["设备总价"] = df["设备数量"] * df["设备单价"]
```

```
# df

         时间 项目经理    预算  设备数量  设备单价  设备总价
0  2020-01-24    张三  2670.0        2     1000      2000
1  2019-12-27    李四   283.1        3       80       240
2  2019-12-27    王二     0.0        1        0         0
3         NaN    张三    25.0        4        5        20
```

3. 对df中的NaN数据进行替换，使用fillna()函数，根据isna函数中的参数inplace来确定是否替换原数据中的数据，本例中将时间中空的项进行替换替换成当前日期，并对时间column进行类型转换表，转换为datetime类型，使用to_datetime，转换完成后查看数据类型

```python
df.fillna(datetime.date.today(), inplace=True) 
df["时间"] = pd.to_datetime(arg=df["时间"], format="%Y/%m/%d")
print(df, df.dtypes)
```

```
# 输出空值已被替换

         时间 项目经理    预算  设备数量  设备单价  设备总价
0  2020-01-24    张三  2670.0        2     1000      2000
1  2019-12-27    李四   283.1        3       80       240
2  2019-12-27    王二     0.0        1        0         0
3  2020-02-24    张三    25.0        4        5        20

# 时间列类型已经转换为Datetime

时间        datetime64[ns]
项目经理            object
预算               float64
设备数量             int64
设备单价             int64
设备总价             int64
```

## 3. 数据index替换

获取数据后为了方便分析或者标注，在初始阶段对index(行)和columns(列)名称可以进行替换，方法为datafream.index = list

```python
df.index = ["项目A", "项目B", "项目C", "项目X"]
```

```
# Index已被替换

             时间 项目经理    预算  设备数量  设备单价  设备总价
项目A  2020-01-24    张三  2670.0        2     1000      2000
项目B  2019-12-27    李四   283.1        3       80       240
项目C  2019-12-27    王二     0.0        1        0         0
项目X  2020-02-24    张三    25.0        4        5        20
```

## 4. 总结

在获取数据之后可以使用DataFrame的许多内建方法对数据进行预处理，虽然Python提供了非常方便的迭代式、推导式等工具，但是使用Pandas时充分利用其内建方法能够更加快速精炼的达到目的，笔者当初为了对数据进行日期格式转换，习惯的使用了嵌套列表推导式，实际上效率又低并且可读性也很差。相关的DataFrame结构的方法很属性非常多，详细请参考[官方文档](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)。