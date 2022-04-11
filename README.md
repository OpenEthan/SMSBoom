![logo](https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/smsboom-logo.png)

![test](https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/test.gif)

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
   ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/cmd.png)
   
   3. 确认 cmd 路径是 EXE 所在路径后,cmd 输入:`smsboom_pyinstall.exe`,若出现命令提示,则说明脚本已正常运行. 
   ![](https://cdn.jsdelivr.net/gh/AdminWhaleFall/SMSBoom@master/img/cmd2.png)

   4. 传递参数.  
    命令示例:  

    启动64个线程,轰炸一个人的手机号(198xxxxxxxx),只轰炸一波。
   ```python
   smsboom_install.exe run -t 64 -p 198xxxxxxxxx
   ```

   启动64个线程,轰炸多个人的手机号(19xxxxxxx),启动循环轰炸，每个循环间隔60秒  

   ```python
   smsboom_install.exe run -t 64 -p 198xxxxxxxxx -s -i 60
   ```

   启动64个线程,轰炸多个人的手机号(138xxx,139xxxx),启动循环轰炸,每个循环间隔60秒。  

   ```python
   smsboom_install.exe run -t 64 -p 138xxxxxxxx -p 139xxxxxxxx -s -i 60
   ```


### 大佬运行 

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

### 配置环境  

> **请确保自己的电脑有 `python3.x` 的环境,推荐使用 `3.8` 及以上！**  

- 安装 pipenv 包管理工具.  

```shell
pip install pipenv  # windows
pip3 install pipenv # linux
```

- 为项目构建虚拟环境.  

```shell
pipenv install
```

- 尝试运行 smsboom.py  

```shell
pipenv run python3 smsboom.py  # linux
pipenv run python smsboom.py # windows
```

若无报错，输出帮助信息，则说明环境已经正确安装。

### 运行  

```python
# 输出帮助信息
pipenv run python smsboom.py --help # windows
pipenv run python3 smsboom.py --help # linux

Usage: smsboom.py [OPTIONS] COMMAND [ARGS]...    
Options:
--help  Show this message and exit.
Commands:
run     传入线程数和手机号启动轰炸,支持多手机号
update  从 github 获取最新接口
```

- 启动轰炸  

帮助信息:

```python
pipenv run python smsboom.py run --help # windows
pipenv run python3 smsboom.py run --help # linux

Usage: smsboom.py run [OPTIONS]

传入线程数和手机号启动轰炸,支持多手机号

Options:
-t, --thread INTEGER    线程数(默认64)
-p, --phone TEXT        手机号,可传入多个再使用-p传递  [required]
-s, --super             循环模式
-i, --interval INTEGER  循环间隔时间(默认60s)
--help                  Show this message and exit.
```

### 命令示例  

启动64个线程,轰炸一个人的手机号(198xxxxxxxx),只轰炸一波。

```python
pipenv run python smsboom.py run -t 64 -p 198xxxxxxxxx
```

启动64个线程,轰炸多个人的手机号(19xxxxxxx),启动循环轰炸，每个循环间隔60秒

```python
pipenv run python smsboom.py run -t 64 -p 198xxxxxxxxx -s -i 60
```

启动64个线程,轰炸多个人的手机号(138xxx,139xxxx),启动循环轰炸,每个循环间隔60秒。

```python
pipenv run python smsboom.py run -t 64 -p 138xxxxxxxx -p 139xxxxxxxx -s -i 60
```

## Development

程序提供接口调试工具，但目前还不完善，欢迎前端大佬 PR。  
调试工具以 `Flask` 为后端，`vue` 为前端，实现前后端分离。  
目前只有测试接口，添加接口的功能。

### Flask 前端调试

> **前提是已经根据前文 Quick Start 的方式安装好 pipenv 环境**

```shell
pipenv run python flask_app/app.py
# 输出
 Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:10981 
 * Running on http://192.168.5.202:10981 (访问链接)(Press CTRL+C to quit)
```

默认监听 *0.0.0.0:10981* 地址,浏览器访问[http://127.0.0.1:10981](http://127.0.0.1:10981)若无意外,就可以出现前端调试界面。

1. WebAPI
`/downloadapi/`:GET 出现当前 api.json 文件的内容。  
`/testapi/`:POST 给定抓取的api，测试请求。  
`/submitapi/`:POST 提交当前的api到 api.json 文件。  

## 企鹅🐧群

欢迎加入企鹅群提出问题和建议！！！

![企鹅群 QR](https://cdn.jsdelivr.net/gh/AdminWhaleFall/Pic@master/img/20220409151539.jpg)

