
from dict import dict
import re

class itt():
    def __init__(self, gen):
        self.gen = gen
    def __iter__(self):
        return self.gen()

class selector():
    def __init__(self, cmap=None, dictionary=None):
        if cmap is None:
            self.cmap = [ "bb?", "s?[ckq]{1,2}", "d|nd", "ff?",
                          "g|ng", "h|th",  "ll?", "m|mm",
                          "nn?", "pp?", "rr?", "s|sh|sch|ss",
                          "tt?", "v",  "w", "x|zz?",
            ]
        else:
            self.cmap = cmap

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
        if len(n) == 0:
            yield ("", 0)
            return

        n = list(n)
        for n_consonants in range(len(n), 0, -2):
            these_consonants = n[:n_consonants]
            remaining_consonants = n[n_consonants:]
#            print("N:", n)
            pat = self.pat_for(*these_consonants)
            words = self.d.select(pat)
#            print("Selected %d words" % len(words))
            yield from [ (" ".join([w,s]), n_consonants+k)
                         for w in words
                         for s,k in self.words_for(*remaining_consonants)
            ]

if __name__ == '__main__':
    s = selector(dictionary=dict("/usr/share/dict/words"),
                 cmap = ["t", "n", "r", "s"])
    w = s.words_for(1, 2, 3)
#    w = s.words_for(0b1111, 0b1010)
    for str in w: print(str)
    
