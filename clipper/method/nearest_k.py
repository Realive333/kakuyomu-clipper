import re
from . import work_seperator

def get_jointlist_by_offset(split_text, offset):
    sep_list = []
    comp_list = []
    joint_list = []
    
    for i, word in enumerate(split_text):
        if work_seperator.calculate_length(sep_list) < offset:
            sep_list.append(word)
            if i == len(split_text)-1:
                comp_list.append(' '.join(sep_list))
        else:
            comp_list.append(' '.join(sep_list))
            sep_list.clear()
            sep_list.append(word)
        
    for i, _ in enumerate(comp_list):
        try:
            if offset == 256:
                joint_list.append(comp_list[i]+comp_list[i+1])
            elif offset == 512:
                return comp_list
        except IndexError:
            _ # reach the end of the comp_list
    return joint_list

def nearest_k_chunk(split_text, similar_wordlist, offset):
    joint_list = get_jointlist_by_offset(split_text, offset)
    best_paragraph = joint_list[0]
    best_score = 0
    for paragraph in joint_list:
        score = 0
        sep_paragraph = re.split(' ', paragraph)
        for word in sep_paragraph:
            if word in similar_wordlist:
                score += 1
        if (score > best_score) and (score > 0) and len(paragraph.replace(' ', '')) > 500:
            best_score = score
            best_paragraph = paragraph
    return (best_paragraph, best_score)

def get_list(split_text, similar_wordlist, offset=256, sep_delimiter=1):
    paragraphs = []
    chunks = list(work_seperator.seperate(split_text, len(split_text)//sep_delimiter))
    for chunk in chunks[:sep_delimiter]:
        try:
            p, s = nearest_k_chunk(chunk, similar_wordlist, offset)
            paragraphs.append({'score': s, 'paragraph': p})
        except TypeError as err:
            print('Error at nearest_k.get_list', err)
            print(''.join(chunk))
    return paragraphs