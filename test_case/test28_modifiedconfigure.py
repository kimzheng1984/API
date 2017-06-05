# coding:utf-8

import unittest
import json
import sys
import urllib
import urllib2
reload(sys)
sys.setdefaultencoding('utf-8')

token = 'a2394fe12c99585b3ce907adbaeb2a12'
# userid = '61044'
userid = '1'
username = 'yk'
password = 'yk'

class shanghutong(unittest.TestCase):
    """修改用户配置"""
    def setUp(self):
        self.base_url = 'http://121.43.60.118:8082/staff/config'
        payload = {'token': token, 'userId': userid, 'username': username, 'param': 'test'}
        self.params = payload

    def tearDown(self):
        pass

    def test28_modifiedconfigure(self):
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
        f.write("case28:修改用户配置"+'\n'+'\n'+str(hjson)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
