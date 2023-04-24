import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
import unittest
from clipper.work_factory import WorkFactory
from clipper.method import nearest_k, work_seperator

class TestFirstMatch(unittest.TestCase):
    def setUp(self):
        self.wf = WorkFactory(42)
        self.wf.load_tsv('morpheme', 'test')
        self.wf.load_similar_wordlist()
        
        self.wf.split_works()
        
        self.test_work = self.wf.get_works()[251]
        self.similar_wordlist = self.wf.get_similar_wordlist(10)
    
    def test_get_nearest_words(self):
        result = self.wf.get_similar_wordlist(10)
        self.assertEqual(result, ['異能', '能力', '超常', 'バトル', 'テレパス', '魔力', '人外', 'テレパシー', '頭脳', '才能'])
    
    def test_nearest_k(self):
        word_list = ['父', 'コー', '白鳥', '銃', 'ぼうや']
        result = nearest_k.get_list(self.test_work, word_list, 256, 5)
        for r in result:
            print(r)
            print('='*10)
        self.assertEqual(len(result), 5)