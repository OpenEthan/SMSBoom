![logo](https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/smsboom-logo.png)

![test](img/test2.gif)

## 免责声明

1. 本程序由一位 **高一摆烂美术生** 开发( **15周岁未成年** ),若使用者滥用本项目,本人 **无需承担** 任何法律责任.  
2. 本程序仅供娱乐,源码全部开源,**禁止滥用** 和二次 **贩卖盈利**.  **禁止用于商业用途**.
3. 本人有 **抑郁症病史**,若本人遭受任何形式的网络暴力(包括但不限于发送淫/秽血/腥图片,问候我家人),并出现 **极端行为**,一切都是 **本人的错** 和大家无关.

## Feature

1. 通过自定义 `api.json` 的方式定义接口.  
2. 支持关键字替换. **时间戳** `[timestamp]` **手机号** `[phone]`  
3. 多线程/异步 请求.  
4. 通过 Flask 提供网页测试/添加接口.  
5. 友好的命令行参数支持.  
6. 采用方便的 pipenv 包管理.  

## Quick Start

### 适用于小白

✨本项目已经使用 `pyinstaller` 打包成 `EXE` 可执行文件!免去部署 Python 环境的烦恼,适合用于小白白.  

🔨作者的打包环境为: `Windows 10 x64 Python3.8` 如果 Windows 系统不是 **Windows 10 64位** 版本,**可能会运行失败**! 如果出现异常报错请截图发 Issue.

1. 下载 EXE 可执行文件  
  请移步到项目的 [release页](https://github.com/AdminWhaleFall/SMSBoom/releases) 下载
  
  > 若遇到国内网络环境下载不下来,请参见 [https://github.do/](https://github.do/) 等加速镜像.
  
2. 运行  

   1. 在任意盘(**除C盘外**)中新建一个文件夹.将程序移动到其中. e.g.  
   ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/e.g.1.png)
  
   2. `Win`+`R` 打开cmd.输入存放的盘符.例如: `E:` 然后cd到文件夹,例如 `cd SMS`
   ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/cmd1.png)
   
   3. 确认 cmd 路径是 EXE 所在路径后,cmd 输入:`smsboom_pyinstall.exe`,若出现命令提示,则说明脚本已正常运行. 
   ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/cmd2.png)

   5. 使用前必须更新一遍最新接口
    ```shell
    smsboom_pyinstall.exe update
    ```  
    > 若更新接口出现错误 `ssl_`,请参见 [issue](https://github.com/AdminWhaleFall/SMSBoom/issues/2) **关闭代理软件**再 update.

   7. 传递参数,命令示例:

    启动64个线程,轰//炸一个人的手机号(198xxxxxxxx),只轰//炸一波。
   ```shell
   smsboom_pyinstall.exe run -t 64 -p 198xxxxxxxxx
   ```

   启动64个线程,轰//炸多个人的手机号(19xxxxxxx),启动循环轰//炸，每个循环间隔60秒  

   ```shell
   smsboom_pyinstall.exe run -t 64 -p 198xxxxxxxxx -s -i 60
   ```

   启动64个线程,轰//炸多个人的手机号(138xxx,139xxxx),启动循环轰//炸,每个循环间隔60秒。  

   ```shell
   smsboom_pyinstall.exe run -t 64 -p 138xxxxxxxx -p 139xxxxxxxx -s -i 60
   ```


### 适用于大佬

#### 下载项目

- 方法一：使用Git:  

```shell
git clone https://github.com/AdminWhaleFall/SMSBoom.git/
```  

> 墙国加速
>  
> ```shell
> git clone https://github.do/https://github.com/AdminWhaleFall/SMSBoom.git
> ```  

- 方法二：点击下载[项目压缩包](https://github.com/AdminWhaleFall/SMSBoom/archive/refs/heads/master.zip)并解压.  

#### 配置环境  

**前提条件:** 请确保自己的电脑有 `python3.x` 的环境,推荐使用 `3.8` 及以上!  

方案一: 有 `Python3.8` 环境的可以使用 `pipenv` 工具.

1. 安装 pipenv 包管理工具.  
```shell
pip install pipenv
```

2. 为项目构建虚拟环境.  
```shell
pipenv install  # 仅使用轰//炸功能
pipenv install --dev # 使用 webui 调试接口功能.
```

3. 尝试运行 smsboom.py  
```shell
pipenv shell # 激活虚拟环境
python smsboom.py  # linux
```

若无报错，输出帮助信息，则说明环境已经正确安装。若报错请使用方案二

方案二: 只有 `Python3.X` 环境的需要使用原生 `pip` 工具.

1. 安装所需要的库
```shell
pip install -r requirements.txt # 仅使用轰//炸
pip install -r requirements-dev.txt # 使用 webui
```

2. 尝试运行 smsboom.py
```shell
python smsboom.py 
```

若无报错，输出帮助信息，则说明环境已经正确安装。

#### 运行  

若使用虚拟环境,请先激活. `pipenv shell`

```shell
# 输出帮助信息
python smsboom.py --help

Usage: smsboom.py [OPTIONS] COMMAND [ARGS]...    
Options:
--help  Show this message and exit.
Commands:
run     传入线程数和手机号启动轰//炸,支持多手机号
update  从 github 获取最新接口
```

- 启动轰//炸  

帮助信息:

```shell
python smsboom.py run --help

Usage: smsboom.py run [OPTIONS]

传入线程数和手机号启动轰//炸,支持多手机号

Options:
-t, --thread INTEGER    线程数(默认64)
-p, --phone TEXT        手机号,可传入多个再使用-p传递  [required]
-s, --super             循环模式
-i, --interval INTEGER  循环间隔时间(默认60s)
--help                  Show this message and exit.
```

### 命令示例  

启动64个线程,轰//炸一个人的手机号(198xxxxxxxx),只轰//炸一波。

```shell
python smsboom.py run -t 64 -p 198xxxxxxxxx
```

启动64个线程,轰//炸多个人的手机号(19xxxxxxx),启动循环轰//炸，每个循环间隔60秒

```shell
python smsboom.py run -t 64 -p 198xxxxxxxxx -s -i 60
```

启动64个线程,轰//炸多个人的手机号(138xxx,139xxxx),启动循环轰//炸,每个循环间隔60秒。

```shell
python smsboom.py run -t 64 -p 138xxxxxxxx -p 139xxxxxxxx -s -i 60
```

## Development

程序提供接口调试工具，但目前还不完善，欢迎前端大佬 PR。  
调试工具以 `Flask` 为后端，`vue` 为前端，实现前后端分离。  
目前只有测试接口，添加接口的功能。

### Flask 前端调试

> **前提是已经根据前文 Quick Start 的方式安装好 pipenv 环境**

```shell
pipenv shell # 激活虚拟环境
python run_flask_app.py start -p 9090 # 监听9090端口
```

**运行帮助:**
```shell
Usage: run_flask_app.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  init         初始化数据库
  json2sqlite  将json数据转为sqlite数据库
  sqlite2json  将sqlite数据转为json
  start        启动 flask app
```

```shell
Usage: run_flask_app.py start [OPTIONS]

  启动 flask app

Options:
  -h, --host TEXT     监听地址
  -p, --port INTEGER  监听端口
  --help              Show this message and exit.
```

默认监听 *0.0.0.0:9090* 地址,浏览器访问[http://127.0.0.1:9090/admin/](http://127.0.0.1:9090/admin/)若无意外,就可以出现前端调试界面。

![](img/webui-test.png)  
![](img/webui-test-2.png)  

## 赞助
[爱发电🔗](https://afdian.net/@smsboom)  

**微/信 && 支/付宝🔗**  
<center class="half">
<img src="https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/wx_pay.jpg" width=40%/>
<img src="https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/aliyun_pay.jpg" width=40%/>
</center>

> 赞助的金额将用于我每月治疗 **抑/郁症** 的支出.谢谢大家的支持和鼓励! **比心ing**

<center class="half">
<img src="img/mypic.png" width=70%/>
</center>

> ~~丑陋的自拍 )逃~~

## Star ♥ 趋势图

<img src="https://starchart.cc/adminwhalefall/smsboom.svg">

## ✨讨论

欢迎加入讨论对项目提出问题和建议！！！mua!

### 企鹅🐧群
> 企鹅群不允许讨论相关敏感信息!违者上飞机票✈

![企鹅群 QR](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20220409151539.jpg)

### Telegram Channel (TG群组)
> 涉及敏/感信息,政/治,民/主运动话题请到 **TG群聊**

[SMSBoomPro](https://t.me/SMSBoomPro)
