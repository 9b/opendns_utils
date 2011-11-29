from libs.urlsanity import *
import unittest

class TestUrlSanityFunctions(unittest.TestCase):

    def test_global_pass(self):
        instance = url_sanity("test_files/global_pass.txt",False)
        result = instance.check_critical()
        self.assertTrue(result,"Globals not present, should be True")
        
    def test_global_fail(self):
        instance = url_sanity("test_files/global_fail.txt",False)
        result = instance.check_critical()
        self.assertFalse(result,"Globals present, should be False")       
        
    def test_alexa_pass(self):
        instance = url_sanity("test_files/alexa_pass.txt",False)
        result = instance.check_top10K()
        self.assertTrue(result,"Top10K not present, should be True")       
        
    def test_alexa_fail(self):
        instance = url_sanity("test_files/alexa_fail.txt",False)
        result = instance.check_top10K()
        self.assertFalse(result,"Top10K present, should be False") 
        
if __name__ == '__main__':
    unittest.main()
