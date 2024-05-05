def pig_it(text):
    text_list = text.split()
    for i, word in enumerate(text_list):
        text_list[i] = list(word)
    for i, word_list in enumerate(text_list):
        if not word_list[0].isalpha():
            text_list[i] = ''.join(word_list)
        else:
            word_ending = word_list[0] + 'ay'
            word_list.pop(0)
            word_list.append(word_ending)
            text_list[i] = ''.join(word_list)
        
    return ' '.join(text_list)