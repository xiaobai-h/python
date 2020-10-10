## Series

### Series类

- 通过pandas.Seires来创建Series数据结构
- pandas.Series(data,index,dtype,name)
- 上述参数中，data可以为列表，array或者dict
- 上述参数中，index表示索引，必须和数据同长度，name代表对象的名称

```python
import pandas as pd
import numpy as np
# 创建一个series对象
series1 = pd.Series([2.8, 3.01, 8.99, 8.59, 5.18])  #可以是数组
series
'''
0    2.80
1    3.01
2    8.99
3    8.59
4    5.18
dtype: float64
'''
series = pd.Series(np.array([2.8,3.01,8.99,8.59,5.18]))  # 可以使array
series4 = pd.Series({'北京':2.8,'上海':3.01,'广东':8.99,'浙江':5.18})  # 可以使dict
```



### Series常用属性

<img src="https://hsx-1302513282.cos.ap-beijing.myqcloud.com/img/image-20200925195932602.png" alt="image-20200925195932602" style="zoom: 33%;" />

```python
series4.values  # 输出数据  array([2.8 , 3.01, 8.99, 5.18])
series4.index  # 输出标签  array(['北京', '上海', '广东', '浙江'], dtype=object)
series4.dtypes  # 输出类型  dtype('float64')
series4.ndim  # 输出维度  1
series4.shape  # 输出形状
series4['北京':'广东']  # 输出从北京到广东，不包含广东
series5 = pd.Series({'四川':3.80,'重庆':2.01,})
series6 = series4.append(series5)  # 可以添加
series4['北京'] = 2.89  # 可以修改
series6.drop(['四川','重庆'],inplace=True)  # 可以删除，inplace为True对原数组操作

```



## DataFrame

### DataFrame类

- 通过pandas.DataFrame来创建DataFrame数据结构。
- pandas.DataFrame(data, index, dtype, columns)。
- 上述参数中，data可以为列表，array或者dict
- 上述参数中，index表示行索引，columns代表列名或者列标签

```python
import pandas as pd
import numpy as np

list = [['张三',23,'男'],['李四',24,'女'],['王二',26,'女']]
df1 = pd.DataFrame(list, columns=['姓名','年龄','性别'])  # 可以列表创建
df1
'''
	姓名	年龄	性别
0	张三	23	男
1	李四	24	女
2	王二	26	女
'''
df2 = pd.DataFrame({'姓名':['张三','李四','王二'], '年龄':[23,24,26], \
                    '性别':['男','女','女']})  # 可以字典创建
df2  # 输出同上

array1 = np.array(list)
df3 = pd.DataFrame(array1, columns=['姓名','年龄','性别'], index=['a','b','c'])
df3  # 输出同上  可以数组创建

```



###  DataFrame属性

```python
df2.values  # 输出所有元素
df2.shape  # 输出形状
df2.dtypes  # 输出所有的列的类型
df2.columns # 输出所有列的名称
df2.nidm  # 输出维度
df2.index  # 输出行标签
df3.index.tolist()  # 以数组形式输出行标签 ['a', 'b', 'c']
```



## 数据获取和保存

### 如何读取和保存

- 使用sqlalchemy建立连接
- 需要知道数据库的相关参数，如数据库IP地址、用户名和密码等
- 通过pandas中read_sql函数读取
- 通过dataframe中to_sql方法保存

<img src="https://hsx-1302513282.cos.ap-beijing.myqcloud.com/img/image-20200926163237084.png" alt="image-20200926163237084" style="zoom: 33%;" />