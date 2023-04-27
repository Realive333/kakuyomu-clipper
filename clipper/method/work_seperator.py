def calculate_length(split_text):
    return len(''.join(split_text))

def seperate(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]
        
def splitter(work_text):
    text = work_text.replace('\n', '。 ')
    split_text = text.split(' ')
    split_text.remove('')
    return split_text