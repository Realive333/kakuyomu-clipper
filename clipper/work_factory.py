import csv
import sys
csv.field_size_limit(sys.maxsize)

import logging

class WorkFactory:
    def __init__(self, target):
        self.target = target
        self.logger = logging.getLogger(__name__)
        self.works = []
        self.target_words = []
        self.similar_wordlist = []
        
    def get_path(self, docType, dataType):
        try:
            assert docType == 'full' or docType == 'morpheme', f'need to assign document type, is {docType}'
            assert dataType == 'train' or dataType == 'dev' or dataType=='test', f'need to assign seperation type, is {dataType}'
            return f'/data/realive333/kakuyomu-dataset/tsv/{docType}/{self.target}/{dataType}.tsv'
        except AssertionError as err:
            self.logger.error(err)
            raise
            
    def load_tsv(self, docType, dataType):
        path = self.get_path(docType, dataType)
        with open(path, 'r', encoding='utf-8') as file:
            rows = csv.reader(file, delimiter='\t')
            for row in rows:
                label = row[0]
                text = row[1]
                self.works.append({'label': label, 'text': text})
                
    def split_works(self):
        works = []
        for work in self.works:
            label = work['label']
            text = work['text']
            text = text.replace('\n', '。 ')
            split_text = text.split(' ')
            split_text.remove('')
            works.append({'label': label, 'text': text, 'split': split_text})
        self.works = works
    
    def load_target_words(self):
        rows = []
        with open('/data/realive333/kakuyomu-dataset/numeric_label.tsv', encoding='utf-8') as f:
            rd = csv.reader(f, delimiter='\t')
            for row in rd:
                rows.append({'label':row[0], 'name':row[1:]})
        self.target_words = rows[self.target-1]['name']
    
    def load_similar_wordlist(self):
        with open(f'/data/realive333/kakuyomu-dataset/morpheme/similarity/{self.target}/total_avg.tsv', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            next(reader, None) # Skip headder
            for row in reader:
                self.similar_wordlist.append({'word': row[0], 'score': row[1]})
        
    
    def get_works(self):
        return self.works
    
    def get_target(self):
        return self.target
    
    def get_target_words(self):
        return self.target_words
    
    def get_similar_wordlist(self, list_length):
        return [word['word'] for word in self.similar_wordlist[:list_length]]
        
        