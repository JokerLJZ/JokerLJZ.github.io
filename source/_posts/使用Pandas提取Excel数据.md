---
title: 使用Pandas提取Excel数据
date: 2020-02-23 22:09:34
img: https://raw.githubusercontent.com/JokerLJZ/Image/master/雪之下雪乃-1.jpg
categories: Python
summary: 介绍Pandas的Excel读取方法技巧
author: 火柴人
tags:
  - Python
  - Pandas
---

## 1. 原始数据表

创建测试数据表 test.xlsx：

|时间|项目经理|预算|设备数量|
|---|--------|---|--|
|2020-01-24|张三|2670|2
|2019-12-27|李四|283.1|3
|2019-12-27|王二|0|1
| |张三|25|4


## 2. 使用Pandas的read_excel()函数读取原始数据表中的数据

read_excel()函数可以直接读取excel文件并返回pandas的dataframe数组，index标签默认为行号，columns标签默认为excel表中的第一行，默认读取第一个sheet的数据，可以根据sheet名或者序号进行sheet的索引。  
官方文档的参数说明请[点击这里](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html#pandas.read_excel)

```python
import pandas as pd
import datetime

# 从EXCEL文件中读取数据
df = pd.read_excel(io="test.xlsx")
print(df)

# 输出 DataFrame
         时间 项目经理    预算  设备数量
0  2020-01-24    张三  2670.0       2
1  2019-12-27    李四   283.1       3
2  2019-12-27    王二     0.0       1
3         NaN    张三    25.0       4

```

## 3. 读取数据的数据类型

Dataframe 拥有属性dtypes可以查看column数据类型，整数对应int64，浮点数对应float64等

```python
print(df.dtypes)

# 输出column与对应的数据类型
时间         object
项目经理     object
预算        float64
设备数量      int64
```

## 4. 时间的读取

根据读取的数据可以看到时间未对应到datetime数据类型，根据read_excel函数的官方文档，函数的参数:  
**parse_dates**: bool, list-like, or dict, default False  
可以将指定column设置为时间类型，本例使用list格式修改时间column为datetime格式

```python
df = pd.read_excel(io="test.xlsx", parse_dates=["时间"])
print(df.dtypes)

# 输出
时间        datetime64[ns]
项目经理            object
预算               float64
设备数量             int64
```

### 目前本人使用的项目仅用到以上举例的用法及参数，参考官方文档read_excel函数可以有多种参数设定以应对各种不同的数据提取需求。