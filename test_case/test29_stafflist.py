# coding:utf-8

import unittest
import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

token = 'a2394fe12c99585b3ce907adbaeb2a12'
# userid = '61044'
userid = '1'
username = 'yk'
password = 'yk'


class shanghutong(unittest.TestCase):
    """店员列表"""
    def setUp(self):
        self.base_url = 'http://121.43.60.118:8082/staff/list'
        self.payload = {'token': token, 'userId': userid, 'mchId': '2485'}

    def tearDown(self):
        pass

    def test29_stafflist(self):
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
        f.write("case29:店员列表"+'\n'+'\n'+str(text)+'\n'+'\n'+'\n')
        # f.write(str(hjson)+'\n')
        f.close()

if __name__ == "__main__":
    unittest.main()
