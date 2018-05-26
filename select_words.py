
from dict import dict
import re

class itt():
    def __init__(self, gen):
        self.gen = gen
    def __iter__(self):
        return self.gen()

class selector():
    def __init__(self, cmap=None, dictionary=None):
        self.cmap = [ "b", "ck", "d", "f",
                      "g", "h",  "l", "m",
                      "n", "pq", "r", "s",
                      "t", "v",  "w", "xz",
        ]
        assert len(self.cmap) == 16
        self.pats = [ re.compile("[%s]" % s)
                      for s in self.cmap ]
        self.vowel_pat = re.compile("[aeiouy]*")
        self.d = dictionary

    def set_dictionary(self, d):
        self.d = d

    # A sequence of numbers each 0-15
    def pat_for(self, *n):
        pats = [ self.vowel_pat ]
        for num in n:
            pats += [ self.pats[num], self.vowel_pat ]
        pat = re.compile("^" + "".join([p.pattern for p in pats]) + "$")
        print(pat.pattern)
        return pat
        
    def words_for(self, *n):
        n = list(n)
        while len(n) > 0:
#            print("N:", n)
            pat = self.pat_for(*n)
            words = self.d.select(pat)
#            print("Selected %d words" % len(words))
            yield from [ (w, len(n)) for w in words ]
            n.pop()

if __name__ == '__main__':
    s = selector(dictionary=dict("/usr/share/dict/words"))
    w = s.words_for(0b1111, 0b1010, 0b0101)
#    w = s.words_for(0b1111, 0b1010)
    for str in w: print(str)
    
