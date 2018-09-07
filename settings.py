# -*- coding:UTF-8 -*-

import logging
import os
import json

from configparser import ConfigParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEBUG = True


def cfg_init():
    raw_cfg = os.path.join(BASE_DIR, 'conf' ,'config.ini')
    def_cfg = os.path.join('/', 'etc','config.ini')
    if not os.path.exists(def_cfg):
        def_cfg = raw_cfg
    cfg = ConfigParser()
    cfg.read(def_cfg)
    return cfg
def get_hotlist():
    hotlist_conf=os.path.join(BASE_DIR, 'conf','hotlist.json')
    with open(hotlist_conf,'r') as load_hotlist:
      hotlist_dict = json.load(load_hotlist)
    data = hotlist_dict["mediacode"]
    return data



BIND_ADDRESS = "0.0.0.0" if DEBUG else "127.0.0.1"
