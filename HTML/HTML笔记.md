# HTML笔记

* `<!DOCTYPE html>` 声明为 HTML5 文档
* `<html>` HTML 页面的根元素
* `<head>` 文档的元（meta）数据，如 `<meta charset="utf-8">` 定义网页编码格式为 utf-8。
* `<title> `标题
* `<body>` 元素包含了可见的页面内容
* `<h1 title='大标题'>` 大标题
* `<p>` 段落
* `<a href="https://www.runoob.com">这是一个链接</a>`插入链接，其中`href`叫做属性，位于括号内，用`""`括起来
* `<img src="/images/logo.png" width="258" height="39" />`插入图像
* `<br>`换行，有多个就空多行
* `<hr>`水平线
* `<!--注释-->`注释
* `<b>文本</b>`加粗
* `<i>文本</i>`斜体
* `<sub>下标</sub>`和`<sup>上标</sup>`
* `<pre> </pre>`之间的文本空格，换行不用符号直接输入即可
* `<del>删除</del> <ins>插入</ins>`
* `<code>计算机代码，相当于``<code>`

#### 一个具体例子: 
```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <h1>我的第一个标题</h1>
    <p>我的第一个段落。</p>
    <pre>
    此例演示如何使用 pre 标签
    对空行和    空格
    进行控制
    </pre>
</body>
</html>
```

## 属性

* 像`href`, `src`, `alt`这些都是属性，有的必须用在特定的元素里面，有的可以通用。

* 比如`style`所有元素可用，直接在元素上应用 CSS 样式: `<p style="color: blue; font-size: 14px;">`，`title`所有元素可用，为元素提供额外的提示信息，通常在鼠标悬停时显示，如`<p title="段落">`

## 其他文本

### 地址
```html
<address>
Written by <a href="mailto:webmaster@example.com">Jon Doe</a>.<br> 
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>
```
### 链接

* `href`定义链接目标: `<a href="https://www.example.com">访问 Example</a>`，显示为<a href="https://www.example.com" title='example.com'>访问 Example</a>

* `target`: 定义链接的打开方式。
`_blank`: 在新标签页中打开链接。
`_self`: 在当前窗口打开链接（默认）。
`_parent`: 在父框架中打开链接。
`_top`: 在整个窗口中打开链接，取消任何框架。

例如`<a href="https://www.example.com" target="_blank" rel="noopener">新窗口打开 Example</a>`

* 锚点链接：同一页面下跳转到指定位置，指定位置用id表示
```html
<a href="#section1">跳转到第1部分</a>
<br>
<br>
<div id="section1">这是第1部分</div>
```

* 图像链接：点击图像跳转链接
```html
<a href="https://www.example.com">
  <img src="example.jpg" alt="示例图片">
</a>
```
<a href="https://www.example.com">
  <img src="../色图.png" alt="示例图片" title="色图" width='500' height='400px'>
</a>

### 居中
`<h1 style="text-align:center;">居中对齐的标题</h1>`

### 特殊样式

<div style="opacity:0.5;position:absolute;left:50px;width:300px;height:150px;background-color:#40B3DF"></div>

<!--div style="font-family:times;padding:2px;border-radius:100px;border:10px solid #EE872A;"-->

<div style="opacity:0.3;position:absolute;left:120px;width:100px;height:200px;background-color:#8AC007"></div>

<h3>Look! Styles and colors</h3>

<div style="letter-spacing:8px;">Manipulate Text</div>

<div style="color:#40B3DF;">Colors
<span style="background-color:#B4009E;color:#ffffff;">Boxes</span>
</div>

<div style="color:#DD00AA;">and more...</div>


```html
<div style="opacity:0.5;position:absolute;left:50px;width:300px;height:150px;background-color:#40B3DF"></div>

<div style="font-family:times;padding:20px;border-radius:100px;border:1px solid #EE872A;">

<div style="opacity:0.3;position:absolute;left:120px;width:100px;height:200px;background-color:#8AC007"></div>

<h3>Look! Styles and colors</h3>

<div style="letter-spacing:8px;">Manipulate Text</div>

<div style="color:#40B3DF;">Colors
<span style="background-color:#B4009E;color:#ffffff;">Boxes</span>
</div>

<div style="color:#DD00AA;">and more...</div>
```


### 表格

* `tr`: table row 的缩写，表格的一行。
* `td`: table data 的缩写，数据单元格。
* `th`: table header的缩写，表格的表头单元格

<table border="0">
<caption><b>标题</b></caption>
  <thead>
    <tr>
      <th>列标题1</th>
      <th>列标题2</th>
      <th>列标题3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>行1，列1</td>
      <td>行1，列2</td>
      <td>行1，列3</td>
    </tr>
    <tr>
      <td>行2，列1</td>
      <td>行2，列2</td>
      <td>行2，列3</td>
    </tr>
  </tbody>
</table>

### 列表

#### 无序列表

<ul>
  <li>Coffee</li>
  <li>Tea
    <ul>
      <li>Black tea</li>
      <li>Green tea
        <ul>
          <li>Good</li>
          <li>Not good</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>Milk</li>
</ul>

#### 有序列表

<ol>
<li>Coffee</li>
<li>Milk</li>
<li>Water</li>
</ol>

#### 自定义列表

<dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
<dt>Water</dt>
<dd>- H2O</dd>
</dl>