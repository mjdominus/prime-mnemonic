
from dict import dict
import re

class itt():
    def __init__(self, gen):
        self.gen = gen
    def __iter__(self):
        return self.gen()

class selector():
    def __init__(self, cmap=None, dictionary=None):
        self.cmap = [ "bb?", "s?[ckq]{1,2}", "d|nd", "ff?",
                      "g|ng", "h|th",  "ll?", "m|mm",
                      "nn?", "pp?", "rr?", "s|sh|sch|ss",
                      "tt?", "v",  "w", "x|zz?",
        ]
        assert len(self.cmap) == 16
        self.pats = [ re.compile("(%s)" % s)
                      for s in self.cmap ]
        self.vowel_pat = re.compile("[aeiouy]*")
        self.vowel_pat_plus = re.compile("[aeiouy]+")
        self.d = dictionary

    def set_dictionary(self, d):
        self.d = d

    # A sequence of numbers each 0-15
    def pat_for(self, *n):
        pats = [ self.vowel_pat ]
        for num in n:
            pats += [ self.pats[num], self.vowel_pat_plus ]
        pats.pop()
        pats.append(self.vowel_pat)
        pat = re.compile("^" + "".join([p.pattern for p in pats]) + "$")
        print(pat.pattern)
        return pat
        
    def words_for(self, *n):
        pat = self.pat_for(*n)
        words = self.d.select(pat)
        yield from [ (w, len(n)) for w in words ]

if __name__ == '__main__':
    s = selector(dictionary=dict("/usr/share/dict/words"))
    w = s.words_for(0b1111, 0b1010, 0b0101)
#    w = s.words_for(0b1111, 0b1010)
    for str in w: print(str)
    
