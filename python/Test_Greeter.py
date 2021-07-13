import unittest
from datetime import datetime
from Greeter import MyGreeter

class MyGreeterTest(unittest.TestCase):
    def test_Client(self):
        tr=[
            ('2020-11-18 11:11:09','Good morning'),
            ('2021-07-18 07:11:09','Good morning'),
            ('2028-11-18 16:11:09','Good afternoon'),
            ('2027-11-18 3:11:09','Good evening')
        ]
        for t in tr:
            tn=datetime.strptime(t[0], "%Y-%m-%d %H:%M:%S")
            g = MyGreeter(tn)
            result = g.Client()
            self.assertEqual(result, t[1],'Error in: '+t[0])
            #self.assertIn(result, ['Good morning','Good afternoon','Good evening'])

if __name__ == '__main__':
    unittest.main()