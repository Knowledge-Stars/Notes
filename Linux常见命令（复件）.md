### 常用操作
1. 安装安装包：sudo dpkg -i 安装包名称与格式
2. 安装软件： sudo apt-get install 名称
3. 进入文件，上一个目录：cd ../../  
4. 浏览当前文件夹的文件：ls  详细信息查看：ls -l  全部显示：ls -a  人性化查看：ls -lh
5. 查看用户名：finger  查看网络配置：ifconfig
   

### 文件操作
1. 创建文件：touch 文件名1 文件名2 文件名3 
2. 创建文件夹：mkdir 文件夹名/里面的文件夹名
* 递归创建文件夹：mkdir -p a/b/c

3. 复制文件：cp 原文件名 复制后的文件名
4. 将文件复制到文件夹：cp 原文件名 文件夹/
5. 将文件夹复制到文件夹里：cp -R 文件夹1/ 文件夹2/
6. 将文件移动：mv 文件名 文件夹/

7. 移除文件：rm 文件名
8. 移除文件夹以及里面的内容：rm -r  文件夹名
9. 树状图查看当前目录文件：tree,只看目录不看文件：tree -d

### 文件编辑
1. 编辑文件：nano 文件名.格式 
2. 显示文件内容：cat 文件名.格式
3. 将文件内容移动到另一个文件,会覆盖原来的文件！：cat file1.py file2.py > file3.py
4. 将文件1的内容直接添加到文件2中：cat file1.py >> file2.py
5. 显示文件内容：more file1.py适用于文件内容较多，空格读下一页，回车读一行，q退出
6. 查找文件内容：grep 文本 file1.py
* grep -n:显示匹配行与行号
* grep -v:显示不包含匹配文本
* grep -i:忽略大小写
* p.s.若搜索内容有空格，须加上引号“”
7. 搜索行首、尾文本：^首、尾$
8. 重定向：echo 内容 > 文件 （这叫重定向，会覆盖所有先前内容）
	   echo 内容 >> 文件 （这叫追加，在先前文件后面添加内容）
9. 管道：将前一个命令的输出作为后一个命令的输入，如ls -lh | more 分屏显示|前面的命令结果

### 文件权限
d      rwx      r-x      r-x
type   user     Group     Others
drw xrw 首字母d表示文件夹，-表示文件，r,w,x分别表示有读,写,执行的权限
修改权限：chmod u+r file1.py
         chmod u-r file.py
         chmod ug-rw file.py
      
### 网络操作
1. 查看网卡配置信息：ifconfig 
2. 检查网卡是否正常链接 ping ip地址
3. SSH操作：建立链接：ssh [-p port] username@ip地址
