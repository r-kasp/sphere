class LanguageModel():
    
    def __init__(self):
        self.stat = dict()
        self.stat2 = dict()
        self.size = 0
        self.size2 = 0
        self.Dict = set()
        
    def add_to_dict(self, word):
        self.Dict.add(word)
    
    def isin(self, word):
        return word in Dict
        
    def add_to_stat(self, word):
        self.size += 1
        if word in self.stat:
            self.stat[word] += 1
        else:
            self.stat[word] = 1
            
    def add_to_stat2(self, word):
        self.size2 += 1
        if word in self.stat2:
            self.stat2[word] += 1
        else:
            self.stat2[word] = 1
    
    def to_bigram(self, words):
        res = []
        for i in range(1, len(words)):
            bigram = words[i-1] + words[i]
            res.append(bigram)
        return res
    
    def get_freq_query(self, words):
        p = 1
        for word in words:
            if word in self.stat:
                p *= self.stat[word]/self.size
        return p
    
    def get_freq_query2(self, words):
        p = 1
        for i in range(1, len(words)):
            bigram = words[i-1] + words[i]
            if bigram in self.stat2:
                p *= self.stat2[bigram]/self.size2
        return p
    
    def get_frequency_word(self, word):
        if word in self.stat:
            return self.stat[word]/self.size
        else:
            return 0
