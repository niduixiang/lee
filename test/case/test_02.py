#coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    def setUp(self):
        print ("start!")
    def tearDown(self):
        time.sleep(1)
        print ("end!")
    def test01(self):
        print (1)
    def test03(self):
        print (2)
    def test02(self):
        print (3)
    def addtest(self):
        print (4)
if __name__ == "__main__":
    unittest.main()