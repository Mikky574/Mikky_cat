import requests
import re
from urllib.parse import urlunsplit
from urllib.request import ProxyHandler,build_opener
import json

import os
from urllib.request import urlopen

from urllib.parse import urlparse
import time

def gethtml(url):
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'
    }#firefox浏览器表头
    req=requests.get(url,headers=headers,timeout=10)
    print("加载成功:",url)
    return req.text


# netloc='www.bigfun.cn'
# scheme='https'
# path='/api/client/web'
# params=''

# page=1
# order='like'
# # role_id=['68,','66']
# # role_id=[100]

# roles=''
# for i in role_id:
#     roles+=str(i)

# query='method=findLineUp&page=%s&order=%s&roles=%s' %(str(page),order,roles)

# fragment=''

# url=urlunsplit([scheme,netloc+path,params,query,fragment])

role_d={}

def url_sp_join(role_l):
    netloc='www.bigfun.cn'
    scheme='https'
    path='/api/client/web'
    params=''
    page=1
    order='like'
    # role_l=['68','66']
    # role_l=[100]
    roles=''
    for i in role_l:
        roles+=str(i)+','
    roles=roles[:-1]
    query='method=findLineUp&page=%s&order=%s&roles=%s' %(str(page),order,roles)
    fragment=''
    url=urlunsplit([scheme,netloc+path,params,query,fragment])
    return url

# role_l=[100]

# for i in range(1,100):
#     role_l=[i]
#     url=url_sp_join(role_l)
#     while True:
#         try:
#             html=gethtml(url)
#             break
#         except:
#             time.sleep(1)
#     js=json.loads(html)
#     if js['data']==[]:
#         break
#     for j in js["data"][0]['lose']:
#         role_d[j['name']]=j['role_id']    

# js["data"][0]['lose'][0]['role_id']
# js["data"][0]['lose'][0]['name']

# role_d2= dict(zip(role_d.values(), role_d.keys()))
# role_d2 = {value:key for key,value in role_d.items()}

# with open("pcr.txt","a",encoding="utf-8") as f:
#     f.write(str(role_d))

# data=sorted(zip(role_d2.keys(),role_d2.values()))

# with open("pcr_role_id.txt","w",encoding="utf-8") as f:
#     f.write(str(s_new))

with open("pcr_role_id.txt","r",encoding="utf-8") as f:
    role_id_s=f.read()
    role_d=json.loads(role_id_s)


role_l_s='布丁,空花,万圣忍,环奈，黄骑'

def role_out(role_l_s):
    role_l_s=role_l_s.replace(' ','')
    role_l_s=role_l_s.replace('，',',')
    role_l=role_l_s.split(',')
    role_l
    role_l_num=[role_d[i] for i in role_l]
    url=url_sp_join(role_l_num)
    html=gethtml(url)
    js=json.loads(html)
    count_role=0
    out_l=[]
    if js['data']!=[]:
        for i in js['data']:
            l=[]
            if count_role>4:
                break
            l.append(i['user']['nickname'])
            l.append(i['like'])
            l.append(i['dislike'])
            l1=[]
            for j in i['win']:
                l1.append(j['name'])
            l.append(l1)
            l1=[]
            for j in i['lose']:
                l1.append(j['name'])
            l.append(l1)
            out_l.append(l)#用户名，攒，踩，赢，输
            count_role+=1
    return out_l,count_role

#role_out(role_l_s)
