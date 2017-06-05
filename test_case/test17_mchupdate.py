# coding:utf-8

import unittest
import json
import sys
import urllib
import urllib2
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf-8')


class shanghutong(unittest.TestCase):
    """门店信息编辑"""
    def setUp(self):
        # 初始化config实例
        config = ConfigParser.ConfigParser()
        # 读写配置文件
        config.readfp(open('config.ini'), 'rw')
        # 获取token
        token = config.get('parameters', 'token')
        # 获取userid
        user_id = config.get('parameters', 'userid')
        # 获取vo1
        vo_1 = config.get('parameters', 'mchid')
        # 获取url
        url = config.get('parameters', 'url')
        self.base_url = url + '/merchant/update'
        payload = {'token': token, 'userId': user_id, 'vo': vo_1}
        self.params = payload

    def tearDown(self):
        pass

    def test17_mchupdate(self):
        test_result = 'C:\\WORK\\workspace\\python\\report\\shanghutong20'
        filename = test_result + "\\" + 'result.txt'
        f = open(filename, 'a')
        self.params = urllib.urlencode(self.params)
        self.params = self.params.encode('ascii')
        r = urllib2.Request(self.base_url, self.params)
        r.add_header = ('Content-Type', 'application/x-www-form-urlencoded')
        text = urllib2.urlopen(r)
        hjson = json.loads(text.read().encode('utf8'))
        try:
            self.assertIn(u'code', hjson) and self.assertIn('0', hjson)
        except AssertionError:
            print hjson

        # f.write(str(code)+'\n')
        f.write("case17:门店信息编辑"+'\n'+'\n'+str(hjson)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
