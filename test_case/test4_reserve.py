# coding:utf-8

import unittest
import requests
import json
import sys
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')

token = '4c2192c200742f8a88288de123bc833a'
userid = '2242'
username = '2485'
password = '2485'


class shanghutong(unittest.TestCase):
    """预约受理"""
    def setUp(self):
        # 初始化config实例
        config = ConfigParser.ConfigParser()
        # 读写配置文件
        config.readfp(open('config.ini'), 'rw')
        # 获取token
        token = config.get('parameters', 'token')
        # 获取userid
        user_id = config.get('parameters', 'userid')
        # 获取url
        url = config.get('parameters', 'url')
        self.base_url = url + '/bespeak/dispose'
        payload = {'token': token, 'userId': user_id, 'status': '1', 'reserveId': '0'}
        self.params = payload

    def tearDown(self):
        pass

    def test4_reserve(self):
        test_result = 'C:\\WORK\\workspace\\python\\report\\shanghutong20'
        filename = test_result + "\\" + 'result.txt'
        f = open(filename, 'a')
        r = requests.get(self.base_url, self.params)
        code = r.status_code
        try:
            self.assertEqual(code, 200)
        except AssertionError:
            print code

        text = r.text
        try:
            self.assertIn(u'成功', text)
        except AssertionError:
            print text

        hjson = json.loads(r.text.encode('utf-8'))
        try:
            self.assertIn(u'code', hjson)
        except AssertionError:
            print hjson

        # f.write(str(code)+'\n')
        f.write("case4:预约受理"+'\n'+'\n'+str(text)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
