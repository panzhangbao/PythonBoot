# coding=utf-8
#
#  Http util
#
# Created by Jason Pan on 2021-01-16 20:38:31
# Copyright © 2021 Jason Pan. All rights reserved.
#

import requests
import json

if __name__ == '__main__':

    # GET
    url = "https://restapi.amap.com/v3/config/district?parameters"
    query_params = "{'name': 'Jane'}"
    response = requests.get(url, params=query_params)
    print(response.text)

    # POST
    body_params = "{'name': 'Jane'}"
    # 定制头和cookie
    header = {'user-agent': 'Mozilla/5.0'}
    cookie = {'key': 'value'}
    response = requests.post(url, data=json.dumps(body_params), headers=header, cookies=cookie)
    print(response.text)

    # 会话对象，能够跨请求保持某些参数
    s = requests.Session()
    s.auth = ('auth', 'passwd')
    s.headers = {'key': 'value'}
    r = s.get('url')
    r1 = s.get('url1')

    # 代理
    proxies = {'http': 'ip1', 'https': 'ip2'}
    requests.get('url', proxies=proxies)
