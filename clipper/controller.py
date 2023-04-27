from . import work_factory
from tqdm import tqdm
from .method import nearest_k, first_match, work_seperator

class Controller:
    def __init__(self, target, dataset_type, clip_type, size=5, offset=256, n_size=100):     
        self.offset = offset
        self.BERT_MAXIMUM_INPUT = 512
        self.wf = work_factory.WorkFactory(target)
        self.wf.load_tsv('morpheme', dataset_type)
        self.wf.load_target_words()
        self.wf.split_works()
        self.delimiter_size = size
        self.n = n_size
        
        if clip_type == 'first-match':
            self.target_words = self.wf.get_target_words()
        elif clip_type == 'nearest-k':
            self.wf.load_similar_wordlist()
            self.wordlist = self.wf.get_similar_wordlist(self.n)
    
        self.works = self.wf.get_works()

    def first_match(self):
        results = []
        for work in tqdm(self.works):
            label = work['label']
            try:
                assert work_seperator.calculate_length(work['split']) > self.delimiter_size * self.BERT_MAXIMUM_INPUT, 'Work length is shorter than expection'
                paragraphs = first_match.get_list(work, self.target_words, self.delimiter_size)
            except AssertionError as err:
                print(err)
            results.append({'label': label, 'paragraphs': paragraphs})
        return results
   
    def nearest_k(self):
        results = []
        for work in tqdm(self.works):
            label = work['label']
            try:
                assert work_seperator.calculate_length(work['split']) > self.delimiter_size * self.BERT_MAXIMUM_INPUT, 'Work length is shorter than expection'
                paragraphs = nearest_k.get_list(work, self.wordlist, self.offset, self.delimiter_size)
            except AssertionError as err:
                print(err)
            results.append({'label': label, 'paragraphs': paragraphs})
        return results