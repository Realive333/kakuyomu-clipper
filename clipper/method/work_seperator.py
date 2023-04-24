def calculate_length(split_text):
    return len(''.join(split_text))

def seperate(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i+n]