## 常用技巧
1. linspace(-1,1,50) #表示生成从-1到1的均匀的50个数字
2. rand(n) #表示生成0~1之间的n个随机数（一维数组）；rand(n,m) #表示生成n行m列的随机数组
```python
import numpy as np
from numpy.random import rand
r=rand(5)
s=rand(3,5)
t=rand(2,3,4,5,...n)
print("rand(5)=",r)
print("rand(3,5)=",s)
print("rand(2,3,4,5)=",t) #生成4*5的数组，按照2*3的形式输出
```
3. L=np.eye(n)表示生成维数为n的单位阵。





### 输入输出函数
* 基本输出
print("a","b","c",sep='、',end=' ')
其中sep表示分隔符号，end表示以什么结尾。
* 带有参数行
print("a="%(参数行))
***%s表示输出字符串，%d表示整数，%f表示浮点数。***
例如：
name=衬衫;price=9.15
print("%s的价格是%f"%(name,price))
或者：print("{}的价格是{}".format(name,age))


### while循环：
``````python
a=1
while a<=100:   #注意要加冒号
  a+=1
print(a)
``````
### for循环：
``````python
list=[1,2,3,4,5,6,7,8,9,10]
for i in list:
    print(i)
``````
``````python
for i in range(4):  #输出[0,1,2,3]
for i in range(1,5):  #输出[1,2,3,4]
for i in range(1,10,2):  #输出[1,3,5,7,9]


range(start , stop , [,step]) #step可选填
``````
if语句：
if a<b:   #注意要加冒号
且 &     或|

if elif else
    
### 定义函数：
def fun(a,b):

#### 用return返回函数调用的结果。
``````python
def fun(a,b,c):
    y=a**2+b**2+c**2
    print("结果为：",y)
    return y
print(fun(3,4,5))
``````
### 全局变量类型： global a
后面有局部变量定义时，全局变量保持不变。

### 读写文件：
``````python
  text="jgrfjjbgrf\nkefhr\n"
  my_file=open('文件.txt','w')  #文件名，读写形式,追加a,只读r,写入w.
  my_file.write(text)
  my_file.close()
  #这样就在当前Python目录下创建了一个.txt
``````
#### 读：
``````python
file=open('my_file.txt','r')
a=file.read()
#另外，file.readline()一次只读取一行，
#file.readlines()一次读取所有信息输出在一行里面。
print(a)
``````
#### 类：

* **说白了，定义一个类lei，可以通过lei.fun调用里面的各个函数，如果想在其他函数里面调用这些函数里面的参数，需要调用self.para**

* **<span style="color:#AA33FF">固定套路：我的类里面的__init__函数对类进行初始化，通过指定self和其他对象(选填)来初始化，然后在__init__函数下面self.duixiang来初始化**
* **调用类的时候传入的参数是__init__除了self之外的参数**
```python
import numpy as np

#定义激活函数
def sigmoid(x):
    return 1/(1+np.exp(-x))

class neuron:
    def __init__(self , weights , bias):
        self.weights = weights
        self.bias = bias
        
    def feedforward(self , inputs):
        #重复上述前向传播计算过程
        total = np.dot(self.weights , inputs) + self.bias
        return sigmoid(total)

# w1=0 , w2=1
weights = np.array([0,1])
bias = 4

######前面__init__函数传入了weights和bias参数，这里就要输入这些参数######
n = neuron(weights , bias)

#x1=2 , x2=3
x = np.array([2,3])
print('前向传播计算结果为:\n',n.feedforward(x))
```

```python
import numpy as np

class twoNN:
    '''
    定义了一个网络：
    * 两个输入
    * 一个隐层，包含两个神经元(h1 , h2)
    * 一个输出层o1
    * 权重均为$w=[0,1]$
    * 偏置项均为0
    '''
    def __init__(self):
        self.weights = np.array([0,1])
        self.bias = 0
        
        #上面定义了一个neuron类
        self.h1 = neuron(weights , bias)
        self.h2 = neuron(weights , bias)
        self.o1 = neuron(weights , bias)
        
    def feedforward(self , x):
        out_h1 = self.h1.feedforward(x)
        out_h2 = self.h2.feedforward(x)
        
        #o1的输入是h1和h2的输出
        out_o1 = self.o1.feedforward(np.array([out_h1 , out_h2]))
        
        return out_o1

######前面的__init__函数除self外没有其它参数，这里不需要再传入######
x = np.array([2,3])
network = twoNN(w,0)
print(network.feedforward(x))
```



``````python
class Calculator:
    name='Nice Calculator'
    price=5
    def fun(self,x,y):
        result=x+y
        print(result)
``````
#### 当我们调用这个类，先把类赋给对象：
lei=Calculator()
#### 然后再调用这个类的一些属性：
print(lei.name)
#### 输出的是这个类的名字Nice Calculator
``````python
print(lei.price)
#输出的是5
lei.fun(5,6)
#输出的是11
``````
#### 类的init功能：
``````python
class Calculator:
    name='Nice Calculator'  #固有属性
    price=5
def __init__(self,name,price,hight):
    self.na=name  #自定义属性，定义后可以覆盖固有属性 
    self.pr=price
    self.hi=height
``````
### 输入：
``````python
  a=input('输入一个数：')  #默认输入的是字符串，可以强制转换int(input())
  print('你输入的是：',a)
  print("%s的名字是%d"%(name,age))
  %7s:输出7个字符，不足补空格
  %7d:输出7个数字
  %8.2f:输出8个字符(含小数点)，保留两位小数
``````
### 元组：
``````python
  a_tuple=(1,2,3,4,5)
  a=(9,)  #元组，只含元素9
  a=(9)  #变量，值为数字9

  a_list=[5,4,3,2,1]
``````
##### 可以对他们的元素进行迭代：
``````python
for i in a_tuple：
    print(i)
for index in range(len(a_tuple)):  
``````
##### 输出元组长度个元素
    print('index=',index,'number=',a_tuple[index])

### 列表：里面元素类型不受限制
索引：
- 正向索引:从0开始从左到右递增[0,...,n-1]
- 负向索引:[-n,...,-1]
- 无线索引:[::step]表示从第一个元素开始，最后一个元素结束

#### 插入
``````python
a=[1,2,3,4,5]
a.append(6)  #在列表a的 最 后 添加一个元素6
a.extend([1,2,3])#在列表a的末尾添加3个元素
a.insert(1,0)  #在第一位 前 面 插入0
``````
#### 删除
``````python
a=[1,2,3,4,5]
a.remove(2)  #去掉第一次出现的2
a.pop() #删除最后一个元素
a.pop(n) #删除索引n元素(从0开始)
a.clear() #清空列表

print(a[-1])  #从最后往前数的第一位
print(a[0:3])  #输出第零位到第三位
print(a.count(2))  #统计2出现了多少次
print(a.index(2))  #看2的索引是什么
print(a*n)  #列表a重复n次
print(len(a))  #获取列表a的长度
a.sort()  #从小到大排序  
a.sort(reverse=Ture)  #从大到小排序
a.reverse()  #按照下标位置逆序输出元素
``````
### 多维列表：
``````python
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(a[0][1])  #输出第零行第一列的值
``````
### 字典：无序的，给定键，输出值
``````
  a=[1,2,3,4,5]
  d={'key':1,'key2':2,'haha':3}  
  #须按照'key':元素的形式,key的类型可任意可以定义字典中的字典
  print(d['haha'])  #相当于找到key为'haha'的那个值并输出
  del d['haha']  #删除haha那个key
  d['haode']=20  #创建一个key
``````
### 数组
```python
import numpy as np
# 创建示例数组
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
# 取出矩阵a的第一行中列索引从0到n-1的所有元素
result_a = a[0, 0:a.shape[1]]
# 取出矩阵b的第一行的所有列元素
result_b = b[0, :]
print(result_a)
print(result_b)
```
##### 在上面的代码中，使用`np.array`函数创建了示例数组`a`和`b`，然后通过索引操作来实现：
1. `a[0, 0:a.shape[1]]`表示取出矩阵a的第一行中第0列到第n-1列的所有元素。`a.shape[1]`表示矩阵a的列数，因此可以得到从第0列到第n-1列的连续范围。
2. `b[0, :]`表示取出矩阵b的第一行的所有列元素。冒号表示取该维度的所有元素，即省略了列的范围。
通过NumPy库，可以在Python中实现类似MATLAB中的数组操作，并进行各种操作，如切片、筛选等。 NumPy库提供了丰富的函数和方法，可以方便地进行数组和矩阵运算。



## 数学运算

### 序列的常用操作
1. len() 字符串长度
2. str.count('a') 找a出现的个数
3. eval() 把字符串内容算出来
4. str.find('abc') 找出字符串
5. str.split(',') 返回按','分割的列表
6. str.strip() 去除str前后的空格
7. join() 拼接字符：' '.join(['I','am','Marisa','daze'])

### 索引
[:a]表示从头开始引用前a个元素
[a:]表示从索引a开始引用后面的所有元素
[::a]表示以间隔a引用从头到尾的所有元素
[:,a]表示取出所有行第a列的元素
[a,:]表示取出a行所有列的元素

### 服从各种分布的随机数
在 Python 中，你可以使用 `random` 模块或者 `numpy` 库来生成随机数。这两种方法都可以用于生成特定区间的均匀分布随机数，以及其他分布的随机数。下面是详细的介绍。

### 1. 生成从-1到1之间的均匀分布的随机数

#### 使用 `random` 模块

你可以使用 `random.uniform(a, b)` 函数，其中 `a` 和 `b` 是你想要生成随机数的区间：

```python
import random

random_number = random.uniform(-1, 1)
print(random_number)
```

#### 使用 `numpy`

如果你使用的是 `numpy` 库，可以使用 `numpy.random.uniform(a, b, size)` 函数：

```python
import numpy as np

random_numbers = np.random.uniform(-1, 1, size=10)  # 生成10个随机数
print(random_numbers)
```

### 2. 生成指定区间服从指定分布的随机数

#### 生成均匀分布随机数

若要生成均匀分布的随机数，可以使用上述方法，只需更改区间值。

#### 生成正态分布随机数
`numpy` 提供了很多其他分布的随机数生成函数。例如：

- 正态分布：`np.random.normal(mu, sigma, size=10)`
- 二项分布：`np.random.binomial(n, p, size)`
- 指数分布：`np.random.exponential(scale, size)`
- 伽马分布：`np.random.gamma(shape, scale, size)`


#### 保留指定位数的小数
print("sin","%.2f"%x,"=","%.3f"%s)


### 矩阵操作
```python
import numpy as np
# 输入一个矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# 对矩阵进行转置操作
transposed_matrix = matrix.T
print(transposed_matrix)

# 求矩阵的逆矩阵
inverse_matrix = np.linalg.inv(matrix)
print(inverse_matrix)

# 输入两个矩阵
matrix1 = np.array([[1, 2],
                    [3, 4]])
matrix2 = np.array([[5, 6],
                    [7, 8]])
# 矩阵相乘操作
product_matrix = np.dot(matrix1, matrix2)
print(product_matrix)


# 定义一个线性变换矩阵
linear_transform_matrix = np.array([[2, 0],
                                    [0, 2]])
# 进行线性变换操作
transformed_matrix = np.dot(matrix, linear_transform_matrix)
print(transformed_matrix)
```


### 堆栈创建和操作
在Python中，可以使用内置的列表（list）来实现堆栈（Stack），因为列表提供了方便的`append()`和`pop()`方法，可以轻松地进行堆栈的入栈和出栈操作。
以下是一个简单的堆栈实现示例：
```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """检查堆栈是否为空"""
        return len(self.items) == 0

    def push(self, item):
        """入栈"""
        self.items.append(item)

    def pop(self):
        """出栈，返回最上面的元素"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        """查看最上面的元素，但不移除"""
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def size(self):
        """返回堆栈的大小"""
        return len(self.items)

# 示例用法
if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("当前堆栈的大小:", stack.size())  # 输出: 3
    print("最上面的元素:", stack.peek())      # 输出: 3
    print("出栈元素:", stack.pop())            # 输出: 3
    print("出栈元素:", stack.pop())            # 输出: 2
    print("堆栈是否为空:", stack.is_empty())    # 输出: False
    stack.pop()  # 出栈最后一个元素
    print("堆栈是否为空:", stack.is_empty())    # 输出: True
```
在这个示例中，我们实现了一个简单的堆栈类，包含以下功能：
- `push(item)`: 将元素添加到堆栈顶。
- `pop()`: 移除并返回堆栈顶的元素。
- `peek()`: 返回堆栈顶的元素，但不移除它。
- `is_empty()`: 检查堆栈是否为空。
- `size()`: 获取堆栈中元素的数量。
通过使用这个堆栈类，你可以进行基本的堆栈操作。



### 读取csv文件数据
#### 读取为字符串string
下面的split即转化为string,asarray将string转化为浮点数。
```python
data = []
data_string = []
data_float = []
for line in open('data.csv'):
  data_string.append(line.strip().split(','))
  data_float = np.asarray(data_string, float)
print(data_string)
print(data_float)
```
***loadtxt直接转化为数字***
```python
  data = np.loadtxt('data.csv', delimiter=',')
  print(data)
```
***提取文件数据并求中位数平均数,保留1位小数***
```python
import numpy as np
data = np.loadtxt('data.csv', delimiter=',')
a ,b = np.mean(data) , np.median(data)
c = np.round(a , 1)
d = np.round(b , 1)
```
***将多个文件数据加起来求平均***
import numpy as np
```python
def mean_datasets(filenames):
#文件的个数n
  n = len(filenames)
  if n > 0:
#按照索引来读取文件
    data = np.loadtxt(filenames[0], delimiter=',')
#文件按照数组读出来，可以像矩阵一样直接相加！
    for i in range(1,n):
      data += np.loadtxt(filenames[i], delimiter=',')
    data_mean = data/n
    return np.round(data_mean, 1)
```



### 模块：
``````python
import time
print(time.localtime())

import time as t
print(t.localtime())

from time import*  #调用模块的所有内容，后面调用不需要再用time.
print(localtime())
print(time())
``````
### 自定义模块:
在当前目录下创建一个m1.py文件：
``````python
def fun(a)
    print(a)
#然后在另一个.py文件里面调用
import m1
    'Diaoyong'
``````
break:结束本层循环。
continue：在循环中跳出本次循环。

### 错误信息处理：
``````python
try:
  file=open('Yukari','r')
except Exception as e:
    print('无法找到文件')
    response=input('创建一个文件？y/n')
    if response=='y'
        file=open('Yukari','w')
    else:
        pass
else:
    file.write('Yakumo')
file.close()
``````
set():找出列表中不同的元素乱序排列。
 只能添加***元素***而不能添加列表 


### 绘制txt文件图像
在Python中，使用with open(filename) as f:
语句打开文件后，f是一个文件对象，它表示已经打开的文件。
文件对象具有许多方法
（例如.read(),.readline(),.readlines(), .write()等），可以用来读取或写入文件内容。
``````python
filename = '0～2能谱 - 副本.txt'
Hx_data1, Hy_data1 = [], []
with open(filename) as f:
    for line in f:
        data = line.strip().split(',')  
        #逐行读取文件中的内容，将每行数据按逗号分割成一个列表，
        #并将第一个元素转换为浮点数后添加到Hx_data1列表中，
        # 将第四个元素转换为浮点数后添加到Hy_data1列表中。
        Hx_data1.append(float(data[0]))
        Hy_data1.append(float(data[3]))
``````
#### 如果想选取其中第几行到第几行，用如下代码：
``````python
lines = f.readlines()
selected_lines = lines[start_line-1:end_line] 
``````
### 选取指定范围的行数据

``````python
for line in selected_lines:
    data = line.strip().split('\t')
    x_data.append(float(data[0]))
    y_data.append(float(data[4]))
``````

        
### 常用技巧
#### 设置Matplotlib参数以支持中文显示  
``````python
plt.rcParams['font.sans-serif'] = ['SimHei'] 
`````` 
#### 指定默认字体为黑体  
``````python
plt.rcParams['axes.unicode_minus'] = False
``````     
#### 解决保存图像是负号'-'显示为方块的问题
``````python
import matplotlib.font_manager  
``````
### 列出所有字体 
`````` python
for f in matplotlib.font_manager.fontManager.ttflist:  
    print(f.name)
  ``````


### 定义一个空列表，并赋值：
定义一个空列表:  
my_list = []  
### 使用循环将数字添加到列表中  

```python
for i in range(1, 6):  # 假设你想添加1到5  
    my_list.append(i)  
print(my_list)  # 输出: [1, 2, 3, 4, 5]

```

### 报错
FileNotFoundError: [Errno 2] No such file or directory:'02a.txt'
的解决:
##### 右键该文件，复制路径，将\改为/.
##### 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
##### 切换工作目录到当前文件所在目录
os.chdir(current_dir)
### 常用实例
#### 饼状图
``````python
labels = ['原材料采购', '劳动力支出', '运营成本', '设备购置与维护', '研发与创新', '其他']  
sizes = [3000000, 2000000, 1000000, 2500000, 1000000, 500000]  
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#cc99ff','#9999ff']  
# 绘制饼状图  
fig1, ax1 = plt.subplots()  
ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)  
# 确保图形是一个完整的圆形，而不是椭圆形  
ax1.axis('equal')  
# 添加标题  
plt.title('财务计划饼状图')  
# 显示图例  
plt.legend()  
# 显示图形  
plt.show()
``````



#### 柱状图
``````python
years = ['2021', '2022', '2023']  
net_profit = [4000000, 5000000, 6000000]  
retained_profit = [2000000, 2500000, 3000000]  
# 设置柱子的宽度和位置  
bar_width = 0.35  # 柱子的宽度  
index = np.arange(len(years))  # 年份的索引  
# 绘制净利润的柱子  
plt.bar(index, net_profit, bar_width, label='净利润', color='#ff9999')  
# 绘制留存利润的柱子，并调整位置使其与净利润的柱子并排  
plt.bar(index + bar_width, retained_profit, bar_width, label='留存利润', color='#66b3ff')  
# 添加年份标签  
plt.xticks(index + bar_width / 2, years)  
# 添加图例、标题和坐标轴标签  
plt.legend()  
plt.title('利润留存变化柱状图')  
plt.xlabel('年份')  
plt.ylabel('利润金额（百万元）')  
# 显示图形  
plt.show()
``````


#### 折线图
``````python
years = ['2021', '2022', '2023']  
equipment_investment = [2000000, 3000000, 4000000]  
research_investment = [1000000, 1500000, 2000000]  
marketing_investment = [500000, 750000, 1000000]  
# 绘制折线图  
plt.figure(figsize=(10, 6))  # 设置图形大小  
# 设备投资  
plt.plot(years, equipment_investment, label='设备投资', color='blue', marker='o')  
# 研发投资  
plt.plot(years, research_investment, label='研发投资', color='green', marker='s')  
# 市场营销投资 
plt.plot(years, marketing_investment, label='市场营销投资', color='red', marker='^')  
# 添加图例、标题和坐标轴标签  
plt.legend()  
plt.title('资金投入变化折线图')  
plt.xlabel('年份')  
plt.ylabel('投资金额（百万元）')  
# 显示网格线 
plt.grid(True) 
# 显示图形  
plt.show()
``````



### 如何编写一个python库并调用？
编写一个 Python 库并调用其中的函数是一个很好的练习，可以帮助理解模块和包的概念。下面是一个详细的步骤教程，指导你如何创建一个简单的 Python 库，并在另一个 Python 脚本中调用它。
### 第一步：创建库的结构
1. **创建目录结构**: 首先，创建一个新的文件夹用于你的库。例如，我们可以将其命名为 `mymathlib`。
   ```
   mymathlib/
   ├── mymath/
   │   ├── __init__.py
   │   └── operations.py
   └── setup.py
   ```
   - `mymathlib/` 是库的根文件夹。
   - `mymath/` 是实际包含代码的文件夹。`__init__.py` 文件表明这是一个 Python 包。
   - `operations.py` 是我们将定义函数的模块。
   - `setup.py` 是用于包管理和安装的文件。
### 第二步：编写函数
在 `operations.py` 中定义一些基础的数学运算函数。打开 `mymath/operations.py`，并添加以下代码：
```python
# mymath/operations.py

def add(x, y):
    """返回 x 与 y 的和"""
    return x + y

def subtract(x, y):
    """返回 x 与 y 的差"""
    return x - y

def multiply(x, y):
    """返回 x 与 y 的积"""
    return x * y

def divide(x, y):
    """返回 x 除以 y 的商。如果 y 是 0，抛出错误。"""
    if y == 0:
        raise ValueError("不能除以 0")
    return x / y
```
### 第三步：创建 `__init__.py`
在 `__init__.py` 文件中，你可以导入 `operations` 模块中的函数，方便用户直接导入。
```python
# mymath/__init__.py
from .operations import add, subtract, multiply, divide
```
### 第四步：设置 `setup.py`, ***里面的name必须为英文！***
在 `setup.py` 文件中，定义包的配置信息。打开 `setup.py`，并添加以下内容：
```python
# setup.py
from setuptools import setup, find_packages
setup(
    name='mymathlib',
    version='0.1',
    packages=find_packages(),
    description='一个简单的数学运算库',
    author='你的名字',
    author_email='你的邮箱',
    url='https://github.com/yourname/mymathlib',  # 如果有的话
)
```
### 第五步：安装你的库
在命令行进入到 `mymathlib` 文件夹，然后运行以下命令安装库：
```bash
pip install .
```
这将在你的 Python 环境中安装该库。
### 第六步：创建一个示例脚本来调用库，***from的必须为包含函数文件的文件夹！***
在库的外面创建一个新的 Python 脚本，比如 `example.py`，用于调用上面创建的库。内容如下：
```python
# example.py
from mymath import add, subtract, multiply, divide
def main():
    print("加法：", add(10, 5))
    print("减法：", subtract(10, 5))
    print("乘法：", multiply(10, 5))
    print("除法：", divide(10, 5))
if __name__ == "__main__":
    main()
```
### 第七步：运行示例脚本
在命令行中，导航到包含 `example.py` 的目录，运行以下命令：
```bash
python example.py
```
你应该会看到类似如下的输出.
```
加法： 15
减法： 5
乘法： 50
除法： 2.0
```
### 总结
你已经成功创建了一个简单的 Python 库，并在一个脚本中调用了它的函数。这一过程涉及了文件结构的组织、基本的库功能实现，以及如何使用 `setup.py` 进行简单的包管理。希望这个教程对你有所帮助！

如果你的 `tcn4ts` 库的目录不在 Anaconda 默认的库路径下，可能会影响到模块的导入。为了确保能够成功导入自定义模块，你可以尝试以下方法：

### 1. 将库移动到 Anaconda 的 site-packages 目录

可以将 `tcn4ts` 库移动到 Anaconda 环境的 `site-packages` 目录中。你可以找到 `site-packages` 目录，通常在以下路径：

- **Windows:** `C:\Anaconda3\Lib\site-packages\` 或类似路径
- **Linux / macOS:** `/home/username/anaconda3/lib/pythonX.X/site-packages/`（其中 `X.X` 是你的 Python 版本，如 `3.8`）

将 `tcn4ts` 文件夹直接复制到 `site-packages` 目录，然后尝试再次导入。

### 2. 使用环境变量临时添加路径

你也可以在 Python 脚本中，动态地将库的路径添加到 `sys.path` 上，以实现临时导入。以下是一个示例：

```python
import sys
import os

# 将 tcn4ts 的路径添加到 sys.path 中
sys.path.append('/path/to/your/tcn4ts')

# 现在可以导入
import tcn4ts  # 或者 from tcn4ts.tcn import your_function
```

确保替换 `/path/to/your/tcn4ts` 为你实际的 `tcn4ts` 库的路径。

### 3. 设置 PYTHONPATH 环境变量

你可以设置 `PYTHONPATH` 环境变量，将 `tcn4ts` 的路径添加到 Python 的模块搜索路径中。具体方法如下：

- **Windows:**
    ```bash
    set PYTHONPATH=C:\path\to\your\tcn4ts;%PYTHONPATH%
    ```

- **Linux / macOS:**
    ```bash
    export PYTHONPATH=/path/to/your/tcn4ts:$PYTHONPATH
    ```

设置完后，启动 Python 交互式环境，然后尝试导入库。

### 4. 建立符号链接（Linux / macOS）

如果你使用 Linux 或 macOS，可以考虑在 `site-packages` 目录下建立一个符号链接，指向你的 `tcn4ts` 目录：

```bash
ln -s /path/to/your/tcn4ts /path/to/anaconda3/lib/pythonX.X/site-packages/tcn4ts
```

### 5. 确保环境一致

最后，确认你使用的 Anaconda 环境是否正确。如果在不同的 Anaconda 环境中工作，可以通过以下命令管理相应环境：

```bash
conda activate your_environment_name
```
### 总结
通过以上方法，确保你的库能够被 Python 正确识别并导入。如果你有错误信息或具体问题，可以分享出来，我们可以更进一步排查。

