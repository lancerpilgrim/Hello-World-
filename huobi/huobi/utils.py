import json
import time
import datetime
import pylab as pl
import requests
from huobi.settings import Path, ToUSDT
from huobi.tools import format_time_as_min


def get_kline(coin, period="1min"):
    req = requests.get(Path.root_url + Path.kline_url, params={"symbol": coin, "period": period})
    res = req.json()
    print(req)
    data = res["data"]
    kline = [{x['id']: x["close"]} for x in data]
    # print(kline)
    t_point = [format_time_as_min(list(x.keys())[0]) for x in kline]
    v_point = [list(x.values())[0] for x in kline]
    # show_image(t_point, v_point)
    return t_point, v_point
