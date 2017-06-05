# coding:utf-8

import unittest
import requests
import json
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

token = '785be082c4ad49f65701ae34b8ff834e'
# userid = '61044'
userid = '1'
username = 'yk'
password = 'yk'


class shanghutong(unittest.TestCase):
    """付款二维码"""
    def setUp(self):
        # 初始化config实例
        config = ConfigParser.ConfigParser()
        # 读写配置文件
        config.readfp(open('config.ini'), 'rw')
        # 获取token
        token = config.get('parameters', 'token')
        # 获取userid
        user_id = config.get('parameters', 'userid')
        # 获取mchid
        mchid = config.get('parameters', 'mchid')
        # 获取url
        url = config.get('parameters', 'url')
        self.base_url = url + '/merchant/payUrl'
        self.payload = {'token': token, 'userId': user_id, 'mchId': mchid}

    def tearDown(self):
        pass

    def test16_payURL(self):
        test_result = 'C:\\WORK\\workspace\\python\\report\\shanghutong20'
        filename = test_result + "\\" + 'result.txt'
        f = open(filename, 'a')
        r = requests.get(self.base_url, self.payload)
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
        f.write("case16:付款二维码"+'\n'+'\n'+str(text)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
