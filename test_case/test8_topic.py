# coding:utf-8

import unittest
import requests
import json
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



class shanghutong(unittest.TestCase):
    """暖游头条"""
    def setUp(self):
        # 初始化config实例
        config = ConfigParser.ConfigParser()
        # 读写配置文件
        config.readfp(open('config.ini'), 'rw')
        # 获取countryid
        countryid = config.get('parameters', 'countryid')
        # 获取url
        url = config.get('parameters', 'url')
        self.base_url = url + '/topic/list'
        self.payload = {'countryId': countryid, 'num': '8'}

    def tearDown(self):
        pass

    def test8_topic(self):
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
        f.write("case8:暖游头条"+'\n'+'\n'+str(text)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
