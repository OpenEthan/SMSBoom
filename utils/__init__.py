
import random

USER_AGENT_LIST = [
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.4 (KHTML, like Gecko) Chrome/3.0.194.0 Safari/531.4"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.50 Safari/525.19"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.7 Safari/532.0"},
    {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 5.0 alpha2)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.7 Safari/532.2"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru-RU) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon;"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.169.0 Safari/530.1"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.7) Gecko/20040614 Firefox/0.9"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.810.0 Safari/535.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0 Safari/534.6"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; TencentTraveler)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.370.0 Safari/533.4"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.4.154.31 Safari/525.19"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE) Chrome/4.0.223.3 Safari/532.2"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/12.0.702.0 Safari/534.24"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.42 Safari/525.19"},
    {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.227.0 Safari/532.3"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.460.0 Safari/534.3"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.463.0 Safari/534.3"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.9 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.9"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.794.0 Safari/535.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.694.0 Safari/534.24"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Maxthon; .NET CLR 1.1.4322)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.4 Safari/532.2"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.682.0 Safari/534.21"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/7.0.531.0 Safari/534.9"},
    {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.811.0 Safari/535.1"},
    {"User-Agent": "ozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.5) Gecko/20041108 Firefox/1.0"},
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
    {
        "User-Agent": "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Safari/533.4"},
    {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.50"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/7.0.0 Safari/700.13"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/0.9.2 StumbleUpon/1.994"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.7.5) Gecko/20041110 Firefox/1.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.6 Safari/530.5"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.0.3705)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.168.0 Safari/530.1"},
    {
        "User-Agent": "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20040913 Firefox/0.10"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.177.1 Safari/530.8"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.40 Safari/530.5"},
    {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.24 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.2 Safari/528.10"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; T312461)"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20041001 Firefox/0.10.1"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.801.0 Safari/535.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.697.0 Safari/534.24"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.548.0 Safari/534.10"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.652.0 Safari/534.17"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 ChromePlus/1.5.2.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.0 Safari/532.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.7 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.2 Safari/533.2"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.4 Safari/532.1"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.0; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.0 Safari/525.19"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.7.5) Gecko/20041108 Firefox/1.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.462.0 Safari/534.3"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.5) Gecko/20041122 Firefox/1.0"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; uZardWeb/1.0; Server_JP)"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; HCI0449; .NET CLR 1.0.3705)"},
    {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt); Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1);"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.23 Safari/530.5"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.176.0 Safari/530.7"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.678.0 Safari/534.21"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; InfoPath.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.55 Safari/525.19"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.724.100 Safari/534.30"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_HK)"},
    {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1"},
    {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)"},
    {
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/3.0.191.3 Safari/531.2"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.39 Safari/530.5"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.38 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b) Gecko/20050118 Firefox/1.0+"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.7) Gecko/20040707 Firefox/0.9.2"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0"},
    {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.171.0 Safari/530.4"},
    {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"},
    {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl-NL; rv:1.7.5) Gecko/20041202 Firefox/1.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/1.0.156.0 Safari/528.8"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0)"},
    {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 2.0.50727; .NET CLR 1.1.4322)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.43 Safari/534.7"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13"},
    {
        "User-Agent": "Mozilla/5.0 (ipad Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.498.0 Safari/534.6"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.19 (KHTML, like Gecko) Chrome/11.0.661.0 Safari/534.19"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-CA) AppleWebKit/534.13 (KHTML like Gecko) Chrome/9.0.597.98 Safari/534.13"},
    {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.6 Safari/525.19"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.599.0 Safari/534.13"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/7.0.521.0 Safari/534.8"},
    {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1"
    },
    {
        "User-Agent": "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5"},
]


def default_header_user_agent():
    return random.choice(USER_AGENT_LIST)
