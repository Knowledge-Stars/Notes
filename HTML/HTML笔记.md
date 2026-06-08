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
</body>
</html>
```

### 属性

* 像`href`, `src`, `alt`这些都是属性，有的必须用在特定的元素里面，有的可以通用。

* 比如`style`所有元素可用，直接在元素上应用 CSS 样式：`<p style="color: blue; font-size: 14px;">`，`title`所有元素可用，为元素提供额外的提示信息，通常在鼠标悬停时显示，如`<p title="段落">`

## 段落

* 分行：`<p>这个<br>段落<br>演示了分行的效果</p>`




