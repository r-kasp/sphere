#OPENING THE FILES

import os

list_of_files = os.listdir("dataset")
files = []

for file in list_of_files:
    f = open('dataset/'+file, 'rb')
    arr = []
    str = ''
    a = f.read()
    str = a.decode('utf-8', errors='ignore')
    files.append(str.lower())
    



#PARSING AND BUILDING DATABASE
import re
def make_url(line):
    res = ''
    ind = 0
    s = 'qwertyuiopasdfghjklzxcvbnm:/.0123456789-'
    while line[ind] in s:
    	res += line[ind]
    	ind += 1
    return res
    

arr = []
for f in files:
	for elt in f.split('http'):
		arr.append(elt)
    
base = []
for site in arr:
    line = 'http' + site
    url = make_url(line)
    parsedline = re.findall('\w+', line[len(url):])
    base.append([url, parsedline])



    
#FIBONACCI ENCODING
def getfib(limit):
    arr = [1, 2]
    ind = 2
    while True:
        elt = arr[ind-1]+arr[ind-2]
        if elt > limit:
            break
        arr.append(elt)
        ind += 1
    return arr

arr = getfib(len(base))
arrsize = len(arr)

def num2fib(num):
    ind = arrsize-1
    res = 0
    while num != 0:
        if arr[ind] <= num:
            res |= 1 << ind
            num -= arr[ind]
        ind -= 1
    return res

def fib2num(fib):
    res = 0
    ind = 0
    while fib != 0:
        res += (fib % 2) * arr[ind]
        fib //= 2
        ind += 1
    return res    
    
code = []
for i in range(len(base)):
    code.append(num2fib(i))


#BUILDING OF INVERSED INDEX
index = {}
num = 0
for site in base:
    for word in site[1]:
        if word not in index:
            index[word] = set()
        index[word].add(code[num])
    num += 1
    
    
#PARSING AND REQUEST TREE
spec = '&()|!'
space = ' '
kdocs = len(base)

def get_docs(word):
    if word in index:
        return index[word]
    else:
        return set()
    
def make_not(word):
    res = set()
    S = get_docs(word)
    for i in range(kdocs):
        if code[i] not in S:
            res.add(code[i])
    return res

def parse(str):
    n = len(str)
    ind = 0
    NOT = False
    word = ''
    docs = []
    operations = []
    while True:
        if ind == n:
            if word != '':
                if not NOT:
                    docs.append(get_docs(word))
                else:
                    docs.append(make_not(word))
            break
        elif str[ind] == space:
            if word != '':
                if not NOT:
                    docs.append(get_docs(word))
                else:
                    docs.append(make_not(word))                        
            NOT = False
            word = ''
            ind += 1
        elif str[ind] == '!':
            NOT = True
            ind += 1
        elif str[ind] == '&':
            operations.append(2)
            ind += 1
        elif str[ind] == '|':
            operations.append(1)
            ind += 1
        elif str[ind] == '(':
            bracket = 1
            subind = ind+1
            subword = ''
            while True:
                if str[subind] == '(':
                    bracket += 1
                if str[subind] == ')':
                    bracket -= 1
                    if bracket == 0:
                        break
                subword += str[subind]
                subind += 1
            ind = subind+1
            docs.append(parse(subword))
            while ind < n and str[ind] == space:
                ind += 1
        else:
            word += str[ind]
            ind += 1
    size = len(operations)+1
    docs2 = []
    res = set()
    if len(docs) != 0:
        curset = docs[0]
        for ind in range(1, size):
            if operations[ind-1] == 1:
                docs2.append(curset)
                curset = docs[ind]
            else:
                curset = curset & docs[ind]
        docs2.append(curset)
        for elt in docs2:
            res = res | elt
    return res
    
    
#SEARCH FUNCTION
def search(request):
    S = parse(request)
    print(request)
    print(len(S))
    for elt in S:
        print(base[fib2num(elt)][0])
    print()
        

#CONSOLE "APP"
f = open('search.sh', 'r')
for line in f:
	str = ''
	length = len(line)
	if line[length-1] == '\n':
		str = line[:length-1]
	else:
		str = line
	search(str)
