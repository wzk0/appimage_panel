# appimage_panel

一个扫描, 管理, 启动, 删除`appimage`文件的小工具

> appimage是`所有Linux发行版`都可运行的一种软件格式. 使用appimage, 抵制`deb`, `rpm`从我做起.

# 起因

因为我发现appimage启动器是不是很好用.

于是做了这个终端小工具.

支持:

0. 扫描全盘或指定文件夹, 并记录所有`appimage`文件的位置;
1. 从一个地方启动/删除appimage文件;
2. 彩色输出.

# 用法

打开终端, 输入:

```sh
wget https://raw.githubusercontent.com/wzk0/appimage_panel/main/appimage.py

python3 appimage.py
```

或将此文件移动到某环境变量文件夹中, 并输入`chmod +x appimage.py`

# 注意

会在本地的`~/`文件夹下生成一个`.appimage_py.json`保存数据.