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
``````python
class Calculator:
    name='Nice Calculator'
    price=5
    def fun(self,x,y):
        result=x+y
        print(result)
``````
#### 当我们调用这个类，先把类赋给个体：
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
    self.hi=hight
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

可修改，添加内容，20240610
