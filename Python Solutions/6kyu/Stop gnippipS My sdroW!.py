def spin_words(sentence):
    words = sentence.split(" ")
    new_sent = ""
    for word in words:
        if len(word) >= 5:
            letters = list(word)
            new_word = ''
            for l in reversed(letters):
                new_word = new_word + l
            word = new_word
        new_sent = new_sent + word + ' '
        
    new_sent = new_sent[:-1]
    return new_sent
