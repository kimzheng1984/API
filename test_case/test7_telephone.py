# coding:utf-8

import unittest
import json
import requests
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class shanghutong20(unittest.TestCase):
    """客服电话"""
    def setUp(self):
        # 初始化config实例
        config = ConfigParser.ConfigParser()
        # 读写配置文件
        config.readfp(open('config.ini'), 'rw')
        # 获取countryid
        countryid = config.get('parameters', 'countryid')
        # 获取url
        url = config.get('parameters', 'url')
        self.base_url = url + '/service/telephone'
        payload = {'countryId': countryid}
        self.params = payload

    def tearDown(self):
        pass

    def test7_telephone(self):
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
        f.write("case7:客服电话"+'\n'+'\n'+str(hjson)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
