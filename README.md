# SMSBoom (Remake)

## Feature

1. 通过自定义 `api.json` 的方式定义接口.  
    api.json:  

    ```json
    [
        {
            "desc": "接口描述",
            "url": "请求地址",
            "method": "请求方法 GET(default)/POST",
            "ua": "请求UA 若为空则默认",
            "data": {}
        }
    ]
    ```

    支持关键字替换.`{timestamp}` `{phone}`

2. 多线程请求.
3. 通过 Flask 提供网页测试/添加接口.
4. 友好的命令行参数支持.  
