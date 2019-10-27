import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.resizer import Resizer

class TestResizer(unittest.TestCase):

    def setUp(self):
        print('%s/tests/test.jpg'%(os.getcwd()))
        self.resizer = Resizer(path='%s/tests/test.jpg'%(os.getcwd()))

    def test_resize(self):
        out = self.resizer.resize(128, 128).output()
        out.show()
        # try:
        #     out.save('%s/tests/test-thumb.jpg'%(os.getcwd()), "JPEG")
        # except IOError:
        #     print("cannot create thumbnail for", 'test-thumb.jpg')

if __name__ == '__main__':
    unittest.main()
