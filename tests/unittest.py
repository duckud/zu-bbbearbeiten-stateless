import unittest
import helper
import main

class TestMethod1(unittest.TestCase):

    def test_replace1(self):
        helper.clear()
        helper.add("test")
        self.assertEquals(len(helper.get_all()),1)
        self.assertEquals(helper.get(0), "test")
    
if __name__ == '__main__':
    unittest.main() 


