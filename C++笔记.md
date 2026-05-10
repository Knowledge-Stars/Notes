## 20260510

1. 函数类型为void可以不用返回任何内容
2. **形参**：函数定义的时候给的没有具体值的参数，如`func(int num1, int num2)`里面的`num1`和`num2`
3. **实参**：自己定义的有具体值的参数，如`int a = 10;`
4. 当做数据传递时，形参变化的时候，实参不会改变。例如下面即使`num1`和`num2`改变了，但输出`a, b`不变：

```cpp
void swap(int num1, int num2)
{
int temp = num1;
num1 = num2;
num2 = temp;
}

int main()
{
int a = 10;
int b = 20;
swap(a, b)

return 0;
}
```