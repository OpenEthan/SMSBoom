# encoding=utf8
# 日志模块
from loguru import logger
import pathlib
import sys
import os

# 终端日志输出格式
stdout_fmt = '{level.icon}  <cyan>{time:HH:mm:ss,SSS}</cyan> ' \
    '[<level>{level}</level>] ' \
    '<cyan>{thread.name}</cyan> ' \
    '<blue>{module}</blue>:<cyan>{line}</cyan> - ' \
    '<level>{message}</level>'

# 日志文件记录格式
# logfile_fmt = '<light-green>{time:YYYY-MM-DD HH:mm:ss,SSS}</light-green> ' \
#     '[<level>{level: <5}</level>] ' \
#     '<cyan>{process.name}({process.id})</cyan>:' \
#     '<cyan>{thread.name: <10}({thread.id: <5})</cyan> | ' \
#     '<blue>{module}</blue>.<blue>{function}</blue>:' \
#     '<blue>{line}</blue> - <level>{message}</level>'

logfile_fmt = '<light-green>{time:YYYY-MM-DD HH:mm:ss,SSS}</light-green> ' \
    '[<level>{level}</level>] ' \
    '<blue>{module}</blue>.<blue>{function}</blue>:' \
    '<blue>{line}</blue> - <level>{message}</level>'

log_pathDir = pathlib.Path(os.getcwd()).resolve().joinpath('logs')
if not log_pathDir.is_dir():
    log_pathDir.mkdir()
log_path = log_pathDir.joinpath('run.log').resolve()

logger.remove()

if not os.environ.get('PYTHONIOENCODING'):  # 设置编码
    os.environ['PYTHONIOENCODING'] = 'utf-8'

logger.add(sys.stderr, level='INFO', format=stdout_fmt, enqueue=True)
# 输出到文件
# logger.add(log_path, level='DEBUG', format=logfile_fmt,
#            enqueue=True, encoding='utf-8')

if __name__ == "__main__":
    logger.info("test")
