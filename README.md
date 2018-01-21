# 下载电影小工具

* 运行效果
    [运行效果](https://https://github.com/supermanxkq/fun/tree/master/img/WX20180121-235229@2x.png)
    [运行效果](https://github.com/supermanxkq/fun/tree/master/img/WX20180122-000056@2x.png)
# ======思路=======
1. 读取配置的网站地址
2. 根据关键字查找对应的资源  urllib,re 正则表达式
3. 下载相应的资源/迅雷

# 运行环境
   * python3.6
   * pycharm
   * Anaconda-Navigator, 需要的包

# 使用方法

* 下载 git clone https://github.com/supermanxkq/fun.git 或 下载zip包
* 修改source_url.json中的配置，添加想要下载明星的电影    例如："key_words": "周星驰,李小龙,成龙"
* pycharm右键运行sou.py，或者命令行直接运行 ```python3 sou.py```
* 下载迅雷
* 设置中选中响应剪贴板
   [选中响应剪贴板](https://github.com/supermanxkq/fun/tree/master/img/WX20180121-234816@2x.png)
* 复制当前项目下生成的种子文件，下载电影。