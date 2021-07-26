def get_features(words):
    length = 0
    for elt in words:
        length += len(elt)
    k_words = len(words)
    if k_words > 1:
        freq = LangModel.get_freq_query2(words)
    else:
        freq = LangModel.get_freq_query(words)
    
    in_dict = 0
    max_p = 0
    min_p = 1
    
    for word in words:
        if word in Dict:
            in_dict += 1
        p = LangModel.get_frequency_word(word)
        min_p = min(p, min_p)
        max_p = max(p, max_p)
    
    not_in_dict = k_words - in_dict
    
    return [length, k_words, not_in_dict, max_p, min_p, freq]
