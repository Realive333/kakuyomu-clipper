import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

import unittest
from clipper.work_factory import WorkFactory


class TestWorkFactory(unittest.TestCase):
    def setUp(self):
        self.wf = WorkFactory(42)
        self.wf.load_tsv('morpheme', 'test')
    
    def test_get_path(self):
        self.assertEqual(self.wf.get_path('full', 'train'), '/data/realive333/kakuyomu-dataset/tsv/full/42/train.tsv')
        self.assertEqual(self.wf.get_path('full', 'dev'), '/data/realive333/kakuyomu-dataset/tsv/full/42/dev.tsv')
        with self.assertRaises(AssertionError):
            self.wf.get_path('full', 'eval')
            
    def test_load_tsv(self):
        self.assertTrue(True)
        #print(self.wf.works[250])
        
    def test_break_works(self):
        self.assertTrue(True)
        self.wf.split_works()
        #print(self.wf.works[250])
        
    def test_load_target_word(self):
        self.wf.load_target_words()
        assertion = self.wf.get_target_words()
        self.assertEqual(assertion, ['超能力', '異能', '異能力', '能力', '異能力バトル', '異能バトル'])

if __name__ == '__main__':
    unittest.main()