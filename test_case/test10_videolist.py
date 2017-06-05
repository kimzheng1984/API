# coding:utf-8

import unittest
import requests
import json
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

token = '4c2192c200742f8a88288de123bc833a'
userid = '2242'
username = '2485'
password = '2485'


class shanghutong(unittest.TestCase):
    """操作教程列表"""
    def setUp(self):
        # 初始化config实例
        config = ConfigParser.ConfigParser()
        # 读写配置文件
        config.readfp(open('config.ini'), 'rw')
        # 获取url
        url = config.get('parameters', 'url')
        self.base_url = url + '/video/list'
        self.payload = {'language': 'zh-cn'}

    def tearDown(self):
        pass

    def test10_videolist(self):
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
        f.write("case10:操作教程列表"+'\n'+'\n'+str(text)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
