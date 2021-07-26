class Node:
    def __init__(self):
        self.terminal = None
        self.children = dict()
    
class BOR:
    def __init__(self):
        self.root = Node()
    
    def b_insert(self, word, cur_node):
        for symb in word:
            if symb not in cur_node.children:
                cur_node.children[symb] = Node()
            cur_node = cur_node.children[symb]
        
        cur_node.terminal = word
    
    def insert(self, word):
        self.b_insert(word, self.root)
    
    def b_nearest_words(self, cur_node, word, max_dist, prev_lev, symb, res):
        n2 = len(word) + 1
        lev = []
        
        lev.append(prev_lev[0] + 1)
        
        for j in range(1, n2):
            var1 = lev[j-1]+1
            var2 = prev_lev[j]+1
            var3 = prev_lev[j-1]
            if symb != word[j-1]:
                var3 += 1
            lev.append(min(var1, var2, var3))
            
        if cur_node.terminal is not None and lev[n2-1] <= max_dist:
            res.append([cur_node.terminal, lev[n2-1]])
            
        flag = False
        for elt in lev:
            if elt <= max_dist:
                flag = True
                break
            
        if flag:
            for symb in cur_node.children:
                self.b_nearest_words(cur_node.children[symb], word, max_dist, lev, symb, res)
                
    def nearest_words(self, word, max_dist):
        n1 = len(word)+1
        lev = []
        for i in range(n1):
            lev.append(i)
        res = []
        for symb in self.root.children:
            self.b_nearest_words(self.root.children[symb], word, max_dist, lev, symb, res)
        return res  
