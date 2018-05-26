
import re

class dict():
    def __init__(self, df, is_good=None):
        self.w = []
        self.sel_cache = {}
        if is_good is None:
            rx = re.compile(r'^[a-z]{3,}$')
            def is_good(w):
                return rx.match(w)
                
        with open(df) as fh:
            while True:
                s = fh.readline().strip()
                if not s: break
#                print("--" , s)
                if is_good(s):
                    self.w.append(s)

    def count(self): return len(self.w)

    def select(self, pat):
        if pat not in self.sel_cache:
            f = filter(lambda s: pat.match(s),
                       self.w)
            self.sel_cache[pat] = list(f)
        return self.sel_cache[pat]


if __name__ == '__main__':
    d = dict("/usr/share/dict/words")
    s = d.select(re.compile(r'foot'))
    print(s)
    
