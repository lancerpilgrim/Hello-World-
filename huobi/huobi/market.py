import sys
sys.path.append("../")
import time
import requests
from huobi.settings import Path, ToUSDT
from huobi.tools import format_time_as_min, Image
from huobi.utils import get_kline
from huobi.monitor import send_wechat


IN = {}
OUT = {}


def is_bottom(v_point):
    if v_point[0] > v_point[1] < v_point[2]:
        return True
    return False


def is_peak(v_point):
    if v_point[0] < v_point[1] and v_point[2] < v_point[1]:
        return True
    return False


def hold(v_point):
    if v_point[0] > v_point[1] > v_point[2]:
        return True
    return False


def is_threshold_price(v, price, lower=True):
    if lower:
        if v[0] < price:
            return True
    else:
        if v[0] > price:
            return True
    return False


def chase_buy(v):
    if v[0] > v[1] > v[2]:
        return True
    return False


def chase_sell(v):
    if v[0] < v[1] < v[2]:
        return True
    return False


def listening_eos(upper_threshold, bottom_threshold):
    while True:
        print("listening to eos/usdt")
        t, v = get_kline(ToUSDT.EOS, period='1min')
        recent_five_minute = list(reversed(list(map(lambda x: str(x), v[:5]))))
        send_wechat("##########".format(bottom_threshold, v[0]))
        if is_threshold_price(v, bottom_threshold):
            send_wechat("请注意, 火币交易所 EOS/USDT 价格低于 {}，现价为 {}".format(bottom_threshold, v[0]))
        if is_threshold_price(v, upper_threshold, lower=False):
            send_wechat("请注意, 火币交易所 EOS/USDT 价格高于 {}，现价为 {}".format(bottom_threshold, v[0]))
        if is_bottom(v):
            send_wechat("EOS/USDT 价格上升拐点，现价为{}，最近五分钟价格{}".format(v[0], "，".join(recent_five_minute)))
        if is_peak(v):
            send_wechat("EOS/USDT 价格下降拐点，现价为{}，最近五分钟价格{}".format(v[0], "，".join(recent_five_minute)))
        if chase_buy(v):
            send_wechat("EOS/USDT 价格连续三分钟上升，现价为{}，最近五分钟价格{}".format(v[0], "，".join(recent_five_minute)))
        if chase_sell(v):
            send_wechat("EOS/USDT 价格连续三分钟下跌，现价为{}，最近五分钟价格{}".format(v[0], "，".join(recent_five_minute)))
        time.sleep(60)


listening_eos(9, 8)



