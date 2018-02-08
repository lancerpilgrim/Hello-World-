import json
import multiprocessing
import time
import datetime
import pylab as pl
import matplotlib.pyplot as plt
import numpy as np
from huobi.monitor import send_wechat


class Image(multiprocessing.Process):
    def __init__(self):
        super().__init__()

    def run(self, *args, **kwargs):
        self.show_image(kwargs["x"], kwargs["y"])

    def show_image(self, x, y):
        pl.plot(x, y)
        pl.show()


def format_time_as_min(timestamp):
    # datetime.datetime()
    t = time.strftime('%Y%m%d%H%M', time.localtime(timestamp))
    return t


def as_np_array(t):
    return np.array(t)


# send_wechat("你好, 这是一条机器人发送的消息")