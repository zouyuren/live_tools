# -*- coding:UTF-8 -*-

import logging

import psycopg2
import settings as s


CFG = s.cfg_init()
database = CFG.get('db','database')
host = CFG.get('db','host')
port = CFG.get('db','port')
user = CFG.get('db','user')
password = CFG.get('db','password')

def query_channels_info(lang):
  conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
  #建立操作游标
  cur = conn.cursor()
  #传入的参数是 SQL 建表语句
  cur.execute("select channel_title,media_code from t_live_channel_info where language = '%s' and media_code not in (select media_code from t_mvlss_channel) order by channel_title;" %(lang)) 
  data = cur.fetchall()
  conn.close()
  return data


