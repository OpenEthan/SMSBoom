

<!--
 * @Author: whalefall
 * @Date: 2021-08-10 11:41:34
 * @LastEditTime: 2021-08-10 14:23:14
 * @Description: 
-->
# 短信轰炸 Python 程序(包含1000+有效接口)

## 前言

- 这是一个爬取网络上**在线轰炸的接口**，后通过 **Python 异步** 请求接口以达到 **手机短信轰炸** 的目的。
- 此为**开源项目**，仅供**娱乐学习使用**，使用者所带来的**一切后果**与**作者无关**，使用**请遵守相关的法律法规**，**合理使用，请勿滥用**。

## 食用方法

### 1. 爬取接口

   - 寻找网上形如：[http://www.sss.pet/](http://www.sss.pet/) 的**在线轰炸网站**
     ![轰炸网站实例](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210810115304.png)

   - 输入手机号并**启动轰炸**，这时会刷新界面，观察**构造出来的地址**。
   
     ![轰炸网站地址](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210810115635.png)
   
     > 可以**发现**地址从：
     >
     > > ```ini
     > > http://www.sss.pet/
     > > ```
     >
     > **变成了**：
     >
     > > ```ini
     > > http://www.sss.pet/index.php?hm={手机号码}&ok=
     > > ```
   
   - 修改 `main.py` 文件
   
     ![实例化SMS对象参数](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210810120405.png)
   
     ![实例化并运行](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210810120700.png)
   
     在函数入口实例化**SMS**对象，此对象要传入一个主网站url，和url后面的参数key，key中的手机号用`{SMS.default_phone}`代替。

   ![非常规](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210810133201.png)

   > 例如上图一个**非常规 Key** 的网站。

   调用**SMS对象**的`main()`方法即可多线程校验接口。

   调用**SMS对象**的`get_sms_api()`即可查看调试网址接口总数。

   ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210810122404.png)

   前面**注释**的网址**我都校验过了**，大家都不用再校验了【狗头】

   - **运行过程**
   
     1. 运行后会先请求轰炸网站正则**获取其接口**API。
     
     2. 把获取到的接口Put到检验队列。
     3. Put完队列后启动**多线程校验**，如果请求接口的**HTTP状态码为200**就写入到**sqlite3数据库**，数据库文件在项目目录下的`data.db`
          
        > 注意：HTTP状态码为200的**不一定是有用**的接口**（好多都不能用的，敲！）**，不过HTTP状态码不正常或者无法访问的**一定是不可以用的**。
        >
        > > **目前只想到这一种检验接口的方法**。
     
        > 支持**数据库自动去重**，不用担心数据重复问题。
     
     4. **2021.8.10** 我已经校验了1113个接口（**不重复**）到 `data.db` 大家可以直接使用（看下面）

### 2. 启动异步轰炸

- 修改`boom.py`下的手机号启动轰炸异步请求。

  ![修改手机号轰炸](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210810132221.png)

- **2021.8.10** 亲测：

  **在5分钟内发了29条短信。**

  ![img](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20210810133449.jpg)

## Todo
- [ ] 🎈允许添加自定义接口`json`格式，自定义请求头、方法、内容。
- [ ] 🎈优化数据库结构，兼容自定义接口。
- [ ] 🎈添加多线程、异步两种轰炸方式。
- [ ] 🎈添加GUI页面方便操作。
- [ ] 🎈用`Flask`做个轰炸API，支持异步返回调用。
- [ ] .....未完待续......
### 欢迎提出`issue`🤔以便开发者完善，也欢迎大佬们Pr完善此项目。

> PS：开发者目前初三🐣，写的垃圾代码，还请大佬们多多指教。😘

## 😡禁止用于非法用途😡

## 😾使用者造成的一切法律后果与本人无关😾



