# SMSBoom (重制版)

## Feature

1. 通过自定义 `api.json` 的方式定义接口.  
2. 支持关键字替换. **时间戳** `{timestamp}` **手机号** `{phone}`  
3. 多线程/异步 请求.  
4. 通过 Flask 提供网页测试/添加接口.  
5. 友好的命令行参数支持.  
6. 采用方便的 pipenv 包管理.  

## Quick Start

1. **下载本项目**  

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

2. **配置环境**  

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

1. **运行**  

- 帮助信息  
```python
pipenv run python smsboom.py --help # windows
pipenv run python3 smsboom.py --help # linux
# 输出

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

4. **命令示例**  

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

