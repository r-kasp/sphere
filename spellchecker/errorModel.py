from GeneratorBOR import BOR

class ErrorModel():
    
    def __init__(self, alpha = 0.5):
        self.alpha = alpha
        self.tree = BOR()
        
    def add_to_bor(self, word):
        self.tree.insert(word)
        
    def lev_dist(s1, s2):
        n1 = len(s1)+1
        n2 = len(s2)+1
        lev = []
        for i in range(n1):
            lev.append([0]*n2)
        for i in range(1, n1):
            lev[i][0] = i
        for i in range(1, n2):
            lev[0][i] = i
        for i in range(1, n1):
            for j in range(1, n2):
                var1 = lev[i-1][j]+1
                var2 = lev[i][j-1]+1
                var3 = lev[i-1][j-1]
                if s1[i-1] != s2[j-1]:
                    var3 += 1
                lev[i][j] = min(var1, var2, var3)
        return lev[n1-1][n2-1]
    
    def get_nearest(self, word, max_dist):
        nearest = self.tree.nearest_words(word, max_dist)
        res = []
        for elt in nearest:
            res.append([elt[0], self.alpha ** (-elt[1])])
        return res
