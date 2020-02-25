---
layout: post
title: Pandas DataFrame对行和列求和及添加新行和列
date: 2020-02-26 00:01:23
img: https://raw.githubusercontent.com/JokerLJZ/Image/master/740128.png
categories: Python
summary: Pandas DataFrame对行和列求和及添加新行和列
author: 火柴人
tags:
  - Python
  - Pandas
  - DataFrame
---

### 1. Excel数据格式如下,从Excel文件中获取数据：

```python
df = pd.read_excel(io="test.xlsx", sheet_name=1)
```

|   | A  | B   | C  | D   |
|---|----|-----|----|-----|
| 0 | 58 | \-5 | 19 | \-5 |
| 1 | 15 | 98  | 38 | 43  |
| 2 | 58 | 21  | 19 | 1   |
| 3 | 16 | 28  | 84 | 60  |
| 4 | 92 | 99  | 89 | 98  |
| 5 | 61 | 37  | 53 | 97  |
| 6 | 60 | 14  | 79 | 99  |

### 2. 计算各行和各列的和并增加新列和新行作为记录

方法一，借助lamda表达式

```python
df["合计"] = df.apply(lambda x: x.sum(), axis=1)
df.loc["合计"] = df.apply(lambda x: x.sum())
```

方法二, 借助np.sum函数

```python
import numpy as np

df["合计"] = df.apply(np.sum, axis=1)
df.loc["合计"] = df.apply(np.sum, axis=0)
```

两种方法输出相同：

|    | A   | B   | C   | D   | 合计   |
|----|-----|-----|-----|-----|------|
| 0  | 58  | \-5 | 19  | \-5 | 67   |
| 1  | 15  | 98  | 38  | 43  | 195  |
| 2  | 58  | 21  | 19  | 1   | 101  |
| 3  | 16  | 28  | 84  | 60  | 191  |
| 4  | 92  | 99  | 89  | 98  | 382  |
| 5  | 61  | 37  | 53  | 97  | 253  |
| 6  | 60  | 14  | 79  | 99  | 258  |
| 合计 | 360 | 292 | 381 | 393 | 1426 |

关于dataframe 的apply()函数用法可以[参考这里](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply)。
