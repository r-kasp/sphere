from Classificator import get_features
from errorModel import ErrorModel
from languageModel import LanguageModel
import sys

def save(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)

def load(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def get_before_tab(s):
    return s[:s.find('\t')]

def get_after_tab(s):
    return s[s.find('\t')+1:]

f = open('queries_all.txt', 'r')
#spec = ' ?!(),.+'
spec = ' '

ErrModel = ErrorModel(2)
LangModel = LanguageModel()
train_x = []
train_y = []

for line in f:
    if line[-1] == '\n':
        line = line[:-1]
    orig = get_before_tab(line)
    fix = get_after_tab(line)
    words = fix.split(spec)
    #words = [re.sub(r'[^A-zА-я0-9]', '', word) for word in words] 
    if fix != "":
        for word in words:
            LangModel.add_to_stat(word) 
            LangModel.add_to_dict(word)
            ErrModel.add_to_bor(word)
        bi_words = LangModel.to_bigram(words)
        if bi_words:
            for word in bi_words:
                LangModel.add_to_stat2(word)
        train_x.append(get_features(words))
        train_y.append(1)
        train_x.append(get_features(orig.split(spec)))
        train_y.append(0)
    else:
        train_x.append(get_features(orig.split(spec)))
        train_y.append(0)

sys.setrecursionlimit(100000)
save(LangModel, "objects/LanguageModel.pkl")
save(ErrModel, "objects/ErrorModel.pkl")
