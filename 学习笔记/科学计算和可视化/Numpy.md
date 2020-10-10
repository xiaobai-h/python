## 数组创建

``` python
import numpy as np
arr1 = np.array([-9,7,4,3])  # 效率不高，不常用
arr1 = np.array([-9,7,4,3], 'float')
arr1 = np.array([-9,7,4,3], dtype='str')
arr1 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])


# 等差数列
arr2 = np.arange(0, 10, 0.5)  # 对应起点，终点(不可取到)，步差
arr3 = np.linspace(1,10,10)  # 对应起点，终点(可取到)， 元素个数 。创建一个有10个元素的等差数列
arr3 = np.linspace(1,10,10,endpoint=False)  # 终点不可取，其他同上

# 等比数列
np.logspace(1, 5, base=2, num=10)  = 2 ** np.linspace(1,5,10)  # 起点，终点，幂，个数

# 创建零数组
np.zeros([4,5])  # 四行五列

# 创建一数组
np.ones([7,6])  # 七行六列

# 创建对角线上为一的数组
np.eye(6)  # 六行六列单位阵

# 指定对角线数字
np.diag([4,5,6])  # 除对角线都是1，对角线为4,5,6

# 通过np可进行所有元素加减
np.diag([4,5,8]) + 1
np.array[4,5,6] + 1
# 但是 [4,5,6] + 1 就不对
```





## 数组属性

```python
arr3.shape
# 返回数组行列

arr3
# 返回具体内容

arr3.ndim
# 返回维度

arr3.size
# 返回元素个数

arr3.dtype
# 返回元素类型
```





## 索引和切片

```python
# 列表倒序
arr = np.arange(1,10)
arr[::-1]

# 视图上修改，原数据也会发生改变
arr_change = arr
arr_change[1:3] = [17, 19]
arr_change
arr 
# 放到jupyter可见arr也发生了改变

# 以后采用复制
arr_change = arr.copy()

'''普通索引'''
# 二维数组切片问题
data2 = ((8.5,6,4.1,2,0.7),(1.5,3.5,4,7,3.9),(3.2,4.5,6,3,9),(11.2,13.4,15.6,17.8,19))
arr2 = np.array(data2)
arr2
arr2[2]  # 输出第三行
arr2[2,1]  # 输出第三行第二列元素
arr2[:, 2:4]  # 输出第三列到第四列
arr2[1:, 2:]  # 输出第二行到最后一行，第三列到最后一列
arr2[2][1]  # 第三行第二列
~(arr2>=3.5)  # 输出大于等于3.5的非，结果元素都是boolean值
arr2[~(arr2>=3.5)]  # 输出小于3.5的元素
arr2[(arr2>3.5) & (arr2<10)]

'''花式索引'''
data = ((8.5, 6.0, 4.1, 2.0, 0.7),
        (1.5, 3.0, 5.4, 7.0, 3.9),
        (3.2, 4.5, 6.0, 3.0, 9.0),
        (11.2, 13.4, 15.6,17.8,19.0))
arr2 = np.array(data)
arr2[[2,1]]  # 以此输出第三行和第二行，
arr2[[3,2],[0,1]]  # 等价于先输出arr2[3,0],在输出arr2[2,1]
arr2[:,[3,1]]  # 先输出第四列在输出第二列
arr2[:,1]  # 输出array([ 6. ,  3. ,  4.5, 13.4])
arr[:,[1]]  ''' 输出array([[ 6. ],
                [ 3. ],
                [ 4.5],
                [13.4]])'''
arr2[np.ix_([0,-1],[0,1,3])]  # 输出第一行和最后一行，第一列第二列和第四列
arr2[0,-1][:,0,1,3]  # 同上

```





## 数组形状改变

```python
data = ((8.5,6,4.1,2,0.7),(1.5,3.5,4,7,3.9),(3.2,4.5,6,3,9),(11.2,13.4,15.6,17.8,19))
arr = np.array(data)
arr
arr.resize(10,2)  # 不直接改变
arr.reshape(10,2)  # 直接改变
arr.shape = (10,2)  # 三个改变数组形状的函数
arr.revel()  # 默认为横向改为一位数组
arr.revel(order='F')  # 改为纵向
arr.flatten()  # 同revel
arr.flatten(order='F')  # 同revel
arr.reshape(2,-1)  # 展成两行10列
arr.reshape(-1)  # 展成一维数组
'''reshape, ravel和flatten三个函数中的reshape和ravel会改变视图的结果，但都不会改变形状'''

arr_t = arr.ravel()
arr_t.nidm  # 相应为1
arr_t.shape  # 相应为(20,)
# 如果想要相应为(20,1)
arr_t[:,np.newaxis]  # 相应为(20,1)

```





## 组合合并

```python
arr1 = np.arange(12).reshape(3,4)
arr1
arr2 = np.array([[8.5,6,4.1,2,0.7],[1.5,3.5,4,7,3.9],[3.2,4.5,6,3,9]])
arr2
np.hstack((arr1, arr2))
'''
输出为
array([[ 0. ,  1. ,  2. ,  3. ,  8.5,  6. ,  4.1,  2. ,  0.7],
       [ 4. ,  5. ,  6. ,  7. ,  1.5,  3.5,  4. ,  7. ,  3.9],
       [ 8. ,  9. , 10. , 11. ,  3.2,  4.5,  6. ,  3. ,  9. ]])
'''
arr3 = np.array([[8.5,6,4.1,0.9],[1.5,3,5.4,1.1],[3.2,4.5,6,7.3],[11.2,13.4,15.6,14.2]])
arr3
np.vstack((arr1,arr3))
'''
输出为
array([[ 0. ,  1. ,  2. ,  3. ],
       [ 4. ,  5. ,  6. ,  7. ],
       [ 8. ,  9. , 10. , 11. ],
       [ 8.5,  6. ,  4.1,  0.9],
       [ 1.5,  3. ,  5.4,  1.1],
       [ 3.2,  4.5,  6. ,  7.3],
       [11.2, 13.4, 15.6, 14.2]])
'''
np.concatenate((arr1,arr2),axis=1)  # aixs等于1是按着列的方向合并
np.concatenate((arr1,arr3),axis=0)  # aixs等于0是按着行的方向合并

arr4 = np.array([[0,1],[2,3]])
np.tile(arr4,(4,1))  # 原来两行两列，现在八行两列

# 三维数组
arr5 = np.arange(8).reshape(2,2,2)
```





## 数组的ufunc广播机制

一维数组，广播运算时，按照行补全方式，当行数不一致时，首先补齐行数，然后进行运算

二维数组，广播运算时，当列数不一致时，首先补齐列数，然后进行运算，当行数不一致时，首先补齐行数，然后进行运算

```python
import numpy as np
arr1 = np.array([[0,1,3],[4,2,9],[4,5,9],[1,-3,4]])
arr2 = np.arange(0,12).reshape(4,3)
arr1 + arr2
```



```python
'''通用函数'''
math = np.array([98,83,86,92,67,82])
english = np.array([68,74,66,82,75,89])
chinese = np.array([92,83,76,85,87,77])
total = math + english + chinese  # 执行加法
np.add(np.add(chinese,math),english)  # 加法函数
np.subtract(math,english)  # 减法函数

np.divide(weight,np.divide(height,100)**2)  # 执行除法，命名为1式
weight/(height/100)**2  # 结果同1式

np.multiply(height,weight)  # 执行乘法
height * weight  # 同上

np.power(arr2,3)  # 对arr2的每个元素都使之三次方

s = np.array([1,2,3,4,3,2,1,2,4,6,7,2,4,8,4,5])
test = [2,4,6]
np.unique(s)
# 输出为 array([1, 2, 3, 4, 5, 6, 7, 8])  即去除相同的

np.id1d(s,test)  # 判断s中的每一个元素是否在test中，如果在的话就为True，否则就是Flase
'''array([False,  True, False,  True, False,  True, False,  True,  True,
        True, False,  True,  True, False,  True, False])
'''

np.intersect1d(test, s)  # 返回交集
arr1 = np.array([[0,1,3],[4,2,9],[4,5,9],[1,-3,4]])
arr2 = np.array([1,2,3])
np.equal(arr1,arr2)  # 判断两者是否相等,会先执行广播机制
''' 返回结果
array([[False, False,  True],
       [False,  True, False],
       [False, False, False],
       [ True, False, False]])
'''
np.greater(arr1,arr2)  # 如果arr1>arr2,则返回True，否则返回Flase
np.greater(arr1,arr2).any()  # 如果有一个True，则输出True，否则输出False
np.greater(arr1,arr2).all()  # 全部为True，则返回True，否则返回False

```



## 搜索与排序

### 重要函数

sort函数

```python
s = np.array([12, 3, 4, 3, 1, 2, 2, 4, 6, 7, 2, 4, 8, 5])
np.sort(s)
# 输出为array([ 1,  2,  2,  2,  3,  3,  4,  4,  4,  5,  6,  7,  8, 12])
sorted(s)
[1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6, 7, 8, 12]
np.array(sorted(s, reverse=True))  # 倒序
# array([12,  8,  7,  6,  5,  4,  4,  4,  3,  3,  2,  2,  2,  1])
```

argsort函数

```python
np.argsort(s)
# 输出为array([ 4,  5,  6, 10,  1,  3,  2,  7, 11, 13,  8,  9, 12,  0],dtype=int64)
# 输出的是拍完序之后的索引
```

argmax函数

```python
s.argmax()
# 输出最大值所在位置
```

argmin函数

```python
s.argmin()
# 输出最小值所在的位置
```

argmax和argmin函数可以对多维数组进行操作，需要指定axis，当axis=1时，按列进行操作，当axis=0，按行进行操作

![image-20200915221918154](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200915221918154.png)



where函数

```python
arr2 = np.arange(12).reshape(4,3)
np.where(arr3>3, '1', '0')
''' 第一个为true，则返回第一个，否则返回第二个
输出为
array([['0', '0', '0'],
       ['0', '1', '1'],
       ['1', '1', '1'],
       ['1', '1', '1']], dtype='<U1')
'''
```

extract函数

```python
np.extract(arr1>arr2, arr1)
'''
array([3, 4, 9, 9])
'''
```



## 文件读取和存储，不常用，一般用pandas

可以使用<span style="color: yellow;">genfromtxt</span>读取TXT或者CSV文件

可以使用<span style = "color: yellow;">loadtxt</span>读取TXT或者CSV文件

两个函数功能类似，<span style="color: yellow;">genfromtxt</span>针对的更多是结构化数据

```python
import numpy as np
data = np.genfromtxt(r''D:\desktop\test.txt',delimiter=',')  # delimiter是指以什么分割，
```

<span style = "color: yellow;">savetxt</span>存储数据



## Numpy字符串操作  char

- Numpy提供char模块处理字符串，运用向量化运算方式

- char模块提供常用的字符串操作函数，如连接、切片、删除、替换等

![char模块常用函数](https://5015060987.oss-cn-beijing.aliyuncs.com/img/image-20200917161246067.png)

```python
import numpy as np
str_list = ['hello','world']
[i.upper() for i in str_list]  # 可以实现小写变大写
np.char.upper(str_list)  # 效率更高，更推荐, 元素全部大写

np.char.add(['中国','国企'],['海军','大阅兵'])
# 输出为array(['中国海军','国企大阅兵'],dtype='<U5')，				元素连接

np.char.multiply(['中国','万岁'],3)
# 输出为array(['中国中国中国','万岁万岁万岁'],dtype='<U6')，		  元素重复

np.char.join([':','-'],['hello','world'])
# 输出为array(['h:e:l:l:o', 'w-o-r-l-d'], dtype='<U9')，          元素拆分

a = ['我想学习一下Python','好好学习一下java']
np.char.replace(a,'学习一下','深入学习')
# 输出为array(['我想深入学习Python','好好深入学习java'],dtype='<U12')

np.char.strip(['-电动汽车','海洋科技-','-学习Python'],'-')
# 输出为array(['电动汽车','海洋科技','学习Python'],dtype='<U9')      删除前道

f = open('D:\desktop\短信.txt',encoding='utf-8').realines()  # 打来短信.txt并按行读取
f
'''
['截至当前，\n',
 '您的套餐使用情况如下：\n',
 '-流量2017沃派2.0主套餐(首月按天)\n',
 '国内流量\n',
 '已用0.00MB校园沃派专属校区流量放心用-50个月\n',
 '省内基站流量\n',
 '已用0.00MB校园沃派专属4GB全国流量国内流量\n',
 '已用4096.00MB校园沃派专属寒暑假漫游升级送-50个月\n',
 '国内流量\n',
 '已用300.00MB校园沃派专属9G全国流量-50个月\n',
 '国内流量\n',
 '已用0.00MB0元65G全国流量国内流量已用56050.94MB\n',
 '本数据仅供参考。\n',
 '回复“5083”，查看流量半年包余量。\n',
 '回复“1071”，查看手机上网流量。\n',
 '抗击疫情，服务不停！使用手机营业厅，足不出户交话费、查余额、办业务，免流量看电影、玩游戏，点击http://u.10010.cn/khddx，马上拥有】']
'''
S = f[-1]
arr = S.split(',')  # 以，作为分隔，分成数组
arr
'''
['抗击疫情',
 '服务不停！使用手机营业厅',
 '足不出户交话费、查余额、办业务',
 '免流量看电影、玩游戏',
 '点击http://u.10010.cn/khddx',
 '马上拥有】']
'''
arr = np.char.rstrip(arr,'】')  # r表示去除右边的东西，l表示去除左边的东西，去除右边的】
arr
'''
array(['抗击疫情', '服务不停！使用手机营业厅', '足不出户交话费、查余额、办业务', '免流量看电影、玩游戏',
       '点击http://u.10010.cn/khddx', '马上拥有'], dtype='<U25')
'''
arr = np.char.repalce(arr,'、',',')  # 替换函数
arr
'''
array(['抗击疫情', '服务不停！使用手机营业厅', '足不出户交话费,查余额,办业务', '免流量看电影,玩游戏',
       '点击http://u.10010.cn/khddx', '马上拥有'], dtype='<U25')
'''

np.char.find(arr,'玩游戏')  # 在arr的每个元素中查找有没有玩游戏这个关键词
'''
array([-1, -1, -1,  7, -1, -1])
'''

np.char.islower(arr)  # 判断英文字符是否都是小写的，小写就为true，否则就是false
np.char.isdigit(arr)  # 判断是否全是数字，全是数字就为true，否则就是false
np.char.isalpha(arr)  # 判断是否全是汉字或者字母，不能包含数字，符号之类的，全中文输出true
np.char.count(arr,'服务')  # 输出每个元素中服务的个数
```



## Numpy随机数生成

```python
import numpy as np
np.random.random((3,4))  # 随机产生三行四列零到一之间的浮点数

np.random.seed(112)  # 任意填一个数，可固定下面的random的随机数
np.random.random((3,4))  # 此时产生随机数之后不再变动

np.random.rand(2,10)  # 均匀分布

np.random.randint(0,100,size=(10,10))  # 随机生成10行10列0到100之间的随机整数

np.random.uniform(low=0,high=100,size=100)  # 随机生成100个0到100的随机浮点数

np.set_printoptions(precision=4)
np.random.uniform(low=0,high=100,size=(100,100))  # 随机生成4位小数点的0到100的100行100列的浮点数

np.random.normal(1,3,size=100)  # 生成均值为1，标准差为3的100个数组
np.mean(np.random.normal(1,3, size=100))  # 检测均值

np.random.randn(10,4)  # 生成十行四列的标准正态分布的数组

s = np.array([1,2,5,7,9,10])
np.random.shuffle(s)  # 类似于重新洗牌，可以直接改变s

np.random.permutation(s)  # 也是重新洗牌，只不过不会改变s
```



## Numpy统计相关的函数

```python
import numpy as np
data = np.genfromtxt(r'D:\desktop\arr.txt',delimiter=',')
data
'''
array([[ 2.,  3.,  4.,  6.,  2.,  1.,  4.,  6.,  2., 66.],
       [12.,  3.,  4.,  3.,  5.,  6.,  8.,  2.,  3.,  9.],
       [ 1., 34.,  6.,  4.,  3., 67., 43.,  6.,  3., 11.],
       [ 1.,  4.,  7.,  9.,  2.,  3., 44., 55.,  6., 21.]])
'''
data.sum()  # 求和
# 481.0
data.sum(axis=0)  # 按列进行操作
'''
array([ 16.,  44.,  21.,  22.,  12.,  77.,  99.,  69.,  14., 107.])
'''

data.mean()  # 求平均值
data.mean(axis=0)  # 按列进行操作

data.cumsum()  # 累积求和
data.cumsum(axis=0)  # 按列累积求和

data.cumprod()  # 累计求积

data.max()  # 求最大值

np.percentile(data,20)  # 求分位数，20%，第二个为50时，即为中位数
np.median(data)  # 求中位数

np.percentile(data,[10,20,30,40,50,60,])  # 分别输出10,20,30,40,50,60%分位数

np.ptp(data)  # 求极差，最大值减最小值
data.ptp(axis=1)  # 求每一个行中最大值减最小值

np.sum(data>65)  # 如果data的个项大于65则加一
```



## Numpy线性代数

```python
import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
vector = np.dot(a,b)
vector  # 输出为32

'''矩阵乘法'''
arr5 = np.array([5,15,25,40]).reshape(4,1)
arr6 = np.arange(12).reshape(3,4)
arr2d = np.dot(arr6,arr5)

'''矩阵转置'''
data = ((8.5,6,4.1,2,0.7),(1.5,3,5.4,7.3,9),(3.2,4.5,6,3,9), \ (11.2,13.4,15.6,17.8,19.0),(12,3.4,1.2,4.,7))
arr2 = np.array(data)
arr2
'''
array([[ 8.5,  6. ,  4.1,  2. ,  0.7],
       [ 1.5,  3. ,  5.4,  7.3,  9. ],
       [ 3.2,  4.5,  6. ,  3. ,  9. ],
       [11.2, 13.4, 15.6, 17.8, 19. ],
       [12. ,  3.4,  1.2,  4. ,  7. ]])
'''
np.transpose(arr2)
'''
array([[ 8.5,  1.5,  3.2, 11.2, 12. ],
       [ 6. ,  3. ,  4.5, 13.4,  3.4],
       [ 4.1,  5.4,  6. , 15.6,  1.2],
       [ 2. ,  7.3,  3. , 17.8,  4. ],
       [ 0.7,  9. ,  9. , 19. ,  7. ]])
'''
arr2_inv = np.linalg.inv(arr2)  # 获得逆矩阵
np.set_printoptions(suppress = True)
np.dot(arr2,arr2_inv)  # 输出为单位阵

np.diag(arr2)  # 取出对角线上的元素

# 3x + 2y + z = 38
# 2x + 3y + z = 34
# x + 2y + 3x + 26
A = np.array([[3,2,1],[2,3,1],[1,2,3]])
A
'''
array([[3, 2, 1],
       [2, 3, 1],
       [1, 2, 3]])
'''
b = np.array([[39],[34],[36]])
b
'''
array([[39],
       [34],
       [36]])
'''
X = np.linalg.solve(A,b)  # 用来求解方程组的解
X
'''
array([[8.42],
       [3.42],
       [6.92]])
'''
```



