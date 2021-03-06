# coding:utf-8

import unittest
import json
import urllib
import urllib2
import ConfigParser
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class shanghutong20(unittest.TestCase):
    """问题反馈"""
    def setUp(self):
        # 初始化config实例
        config = ConfigParser.ConfigParser()
        # 读写配置文件
        config.readfp(open('config.ini'), 'rw')
        # 获取token
        token = config.get('parameters', 'token')
        # 获取userid
        user_id = config.get('parameters', 'userid')
        # 获取username
        user_name = config.get('parameters', 'username')
        # 获取reason
        reason = config.get('parameters', 'reason')
        # 获取detail
        detail = config.get('parameters', 'detail')
        # 获取url
        url = config.get('parameters', 'url')
        self.base_url = url + '/feedback/add'
        payload = {'token': token, 'userId': user_id, 'username': user_name, 'reason': reason, 'detail': detail}
        self.params = payload

    def tearDown(self):
        pass

    def test6_feedback(self):
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
        f.write("case6:问题反馈"+'\n'+'\n'+str(hjson)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
