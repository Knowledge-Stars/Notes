# LaTex笔记

```
1.在里面编写内容。
  \begin{document}
  \end{document}

2.\title{标题}
  \author{作者}
  \date{\today}
  不要日期：\date{}
  
  \begin{abstract}
  \end{abstract}
  
3.标题单独成页。
  \begin{titlepage}
  \maketitle
  \end{titlepage}
4.\section{条分缕析1.，2.，3....}
  \subsection{更加细分1.1,1.2，...}
5.中文使用。
   \usepackage{xeCJK},编译器改为XeLaTex.
6.换页\newpage
7.对齐（居中，左对齐，右对齐）
   \begin{center}   flushleft   flushright
  \end{center}        ~             ~
8.字体
  加粗：\textbf{}
  下画线：\underline{}  
  斜体：\textit{}
  大小：\tiny  \scriptsize  \small  \normalsize  \large  \Large  \LARGE  \huge  \Huge
9.图片
  包： \usepackage{graphicx}
    \graphicspath{{.路径}}
   \includegraphics[scale=放缩比例,angle=旋转角度]{路径}
   \includegraphics[width=宽cm,height=高cm]{路径}
  浮动图片，自动排版位置：
   \begin{figure}
  \end{figure}
10.文字包围图片。
  包：  \usepackage{wrapfig}
  \begin{wrapfigure}{r代表右对齐，l代表左对齐}{0.25\textwidth四分之一页面宽度}
11.图片标题，注释。
  \caption{内容}
  若一个注释两个图片，包：\usepackage{subcaption}
  \begin{subfigure}
  \end{subfigure},两对语句之间分别插入图片信息。
  引用图片：\ref{名称}
 
12.表格
（1）\begin{center}
     \begin{tabular}{c c c(表示居中，r r r表示居右，三个表示三列。)}
     A & B & C \\换行
        ...
（2）\begin{tabular}{|c|c|c|}加竖线，多条也可以。
         \hline 加横线，多条也可以。
（3）固定宽度表格，包：\usepackage{array}
         \begin{tabular}{| m{3cm} | m{3cm} | m{3cm} |}若要让某一列居中对齐，在某一列后面<{\centering}
（4）合并单元格\multicolumn{合并几列}{|对齐方式|}{内容} & x \\
            包：\usepackage{multirow}
            合并行：\multirow{合并的行数目}
13.页面
页边距：\usepackage{geometry}
\geometry{left=2cm,right=2cm,top=3cm,bottom=3cm}

其他：
点乘：a \cdot b(注意空格)  \dots 多个点。
叉乘：a \times b
除以：a \div b
绝对值：${\lvert \Psi \rvert}^2$
大于等于： \geq
小于等于：\leq
约等于：\approx
定积分：$\int_{a}^{b} x^2 dx$
二重积分：$\iint_V f(u,v) \,du\,dv$ 在公式编辑里面空格用“\,”
多重积分，iiiiiiiiiint
大Σ求和：$\sum_{下面}^{\infty} 被求和式子 = 结果$   无穷大：\infty
求积：$\prod_{下面}^{上面} f(i)$
极限：\lim_{下面}
让公式变大： 用$\displaystyle{}$更好。
公式居中：$$   $$
换行：\\ 或 \par 或 \newline 或回车空一行。
指定换行长度：\vspace{2cm}

波浪线~：$\sim$
右上角的撇：  a^{\prime}
箭头：\rightarrow   \leftarrow   \up~   \down~
箭头上写字：X \stackrel{F}{\longrightarrow} Y
推出符号：\Rightarrow   \Left~
左右矢<>： \langle   \rangle
嵌入代码：
反斜杠begin{verbatim}
Your code here
反斜杠end{verbatim}
输入跨行大括号：
$
\left\{ 
    \begin{array}{lc}
        weight，\\
        0 or \infty,\\
    \end{array}
}
\right
$
```