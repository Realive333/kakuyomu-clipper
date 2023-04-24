import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
import unittest
from clipper.work_factory import WorkFactory
from clipper.method import first_match, work_seperator

class TestFirstMatch(unittest.TestCase):
    def setUp(self):
        self.wf = WorkFactory(42)
        self.wf.load_tsv('morpheme', 'test')
        self.wf.load_target_words()
        self.wf.split_works()
        self.test_work = self.wf.get_works()[251]
        self.target = self.wf.get_target()
        
        self.target_words = self.wf.get_target_words()
        
    def test_calculate_length(self):
        assertion = work_seperator.calculate_length(['いち', 'に', 'さん', 'し'])
        self.assertEqual(assertion, 6)
        
    def test_first_match(self):
        result = first_match.get_list(self.test_work, self.target_words, 5)
        print(result)
        self.assertTrue(True)