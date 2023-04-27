from . import work_seperator

def first_match_chunk(chunk, target_words):
    for index, word in enumerate(chunk):
        if word in target_words:
            l_paragraph = chunk[:index]
            r_paragraph = chunk[index:]
            ct = 0
            paragraph = []
            for wd in r_paragraph:
                ct += len(wd)
                paragraph.append(wd)
                if ct > 512:
                    return 'success at r_list', 'r', ' '.join(paragraph[:-1])
            if ct < 512:
                for wd in reversed(l_paragraph):
                    ct += len(wd)
                    paragraph.insert(0, wd)
                    if ct > 512:
                        return 'success at l_list', 'l', ' '.join(paragraph[1:])
    ct = 0
    for idx, wd in enumerate(chunk):
        ct += len(wd)
        if ct > 512:
            return 'no match', 'n', ' '.join(chunk[:idx])

def get_list(split_text, target_words, sep_delimiter=1):
    paragraphs = []
    chunks = list(work_seperator.seperate(split_text, len(split_text)//sep_delimiter))
    for chunk in chunks[:sep_delimiter]:
        try:
            s, c, p = first_match_chunk(chunk, target_words)
            paragraphs.append({'status': s, 'code': c, 'paragraph': p})
        except TypeError as err:
            print('Error at first_match.get_list', err)
            print(''.join(chunk))
    return paragraphs