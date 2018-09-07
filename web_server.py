# coding: utf-8 

from flask import Flask,request
import os,sys,json
from settings import get_hotlist
from models import query_channels_info
reload(sys)
sys.setdefaultencoding('utf-8')

hotlist=get_hotlist()
lang=""


server = Flask(__name__)

@server.route('/nostreams/channels')
def index():
    global lang
    lang = request.values.get('lang')
    if lang:
      query_result=query_channels_info(lang)
      response=html_view_tmp(query_result)
      return response
    else:
      return "请输入查询语种"

#页面显示
def html_view_tmp(query_result):
    str1=""
    str2=""
    cutstrams_num=0
    hot_cutstrams_num=0
    cutstrams_num=len(query_result)
    for row in query_result:
      mediacode=row[1]
      channelname=row[0]
      if mediacode in hotlist:
	hot_cutstrams_num=hot_cutstrams_num+1
	str1="""%s
		<tr style='color:red'>
		  <th>%s</th><th>%s</th>
		</tr>
	"""  %(str1,channelname,mediacode)
      else:
        str2="""%s
                <tr>
                  <th>%s</th><th>%s</th>
                </tr>
        """  %(str2,channelname,mediacode)
    str="""<style type="text/css">body{background-color:#EAF2D3;} table  {   border-collapse:collapse;  }td,th   {  font-size:1em;  border:1px solid #98bf21;  padding:1px 5px 1px 5px;  }th {  font-size:1.1em;  text-align:left;  padding-top:3px;  padding-bottom:2px;  background-color:#A7C942;  color:000000;  }td {  color:000000;  background-color:#EAF2D3;  }</style>
      <table>
	<tr>
		<th style='background-color:#EAF2D3;'>%s断流情况如下：</th>
		<th style='background-color:#EAF2D3;'>断流总数：%s，<h style='color:red'>热门节目断流总数：%s</th>
	</tr>
        <tr>
                <th>频道名</th>
                <th>mediacode</th>
        </tr>
	%s %s
      </table>	
    """ %(lang,cutstrams_num,hot_cutstrams_num,str1,str2)
    return str

if __name__ == '__main__':
  server.run(port=8123,debug=True,host='127.0.0.1')
