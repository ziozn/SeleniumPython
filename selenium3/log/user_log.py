import logging
import os
from log import categories
'''
日志配置
'''
'''
%(name)s        Logger的名字
%(levelno)s     数字形式的日志级别
%(levelname)s   文本形式的日志级别
%(pathname)s    调用日志输出函数的模块的完整路径名，可能没有
%(filename)s    调用日志输出函数的模块的文件名
%(module)s      调用日志输出函数的模块名
%(funcName)s    调用日志输出函数的函数名    
%(lineno)d      调用日志输出函数的语句所在的代码行
%(created)f     当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d     输出日志信息时的，自Logger创建以 来的毫秒数
%(asctime)s     字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(thread)d      线程ID。可能没有
%(threadName)s  线程名。可能没有
%(process)d     进程ID。可能没有
%(message)s     用户输出的消息
'''


class Logs:

    def __init__(self):
        self.time_info_path = categories.creating('logs', 'web_info_log')
        self.time_error_path = categories.creating('logs', 'web_error_log')
        if not os.path.isdir(self.time_info_path):
            os.mkdir(self.time_info_path)
        if not os.path.isdir(self.time_error_path):
            os.mkdir(self.time_error_path)

        self.th = logging.Formatter('%(asctime)s %(filename)s %(funcName) %(levelname) %(lineno)s %(message)s')
        self.win = logging.StreamHandler()
        self.win.setFormatter(self.th)

    def __info(self, mes):
        logger = logging.getLogger()
        logger.setLevel('INFO')
        text_info_log = os.path.join(self.time_info_path, 'web_info_log.text')
        ih = logging.FileHandler(text_info_log, 'a', encoding='utf8')
        ih.setFormatter(self.th)
        logger.__dict__['handlers'] = []
        logger.addHandler(ih)
        logger.addHandler(self.win)
        logger.info(mes)

    def __error(self, mes):
        logger = logging.getLogger()
        logger.setLevel('DEBUG')
        text_error_log = os.path.join(self.time_error_path, 'web_error_log.text')
        ch = logging.FileHandler(text_error_log, 'a', encoding='utf8')
        ch.setFormatter(self.th)
        logger.__dict__['handlers'] = []
        logger.addHandler(ch)
        logger.addHandler(self.win)
        logger.error(mes)

    def goinfo(self, mes):
        self.__info(mes)

    def goerror(self, mes):
        self.__error(mes)


if __name__ == '__main__':
    logs = Logs()
    logs.goinfo('ddd')
    logs.goerror('sss')
