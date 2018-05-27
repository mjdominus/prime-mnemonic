
from sys import stdin

class menu():
    def __init__(self, items, prompt="> ", label=None,
                 cols=3, width=80):
        self.items = items
        self.p = prompt
        self.label = label
        self.cols = cols
        self.width = width

    def prompt(self):
        print(self.p, end='', flush=True)

    def get(self):
        self.prompt()
#        import pdb; pdb.set_trace()
        while True:
            try:
                n = int(stdin.readline().strip())
                if n >= 0 and n < len(self.items):
                    return n
            except ValueError:
                print("Wat.")
                self.prompt()

    def show(self):
        n = 0
        col_wid = self.width // self.cols
        def pad_to(s, w):
            p = w - len(s)
            if p > 0:
                return s + " " * p
            else:
                return s
            
        while n < len(self.items):
            line = ""
            for c in range(self.cols):
                if n+c >= len(self.items):
                    break
                label = self.items[n+c]
                if self.label is not None:
                    label = label[self.label]
                item = "%2d. %s" % (n+c, label)
                line += pad_to(item, col_wid)
            n += self.cols
            print(line)
        
    def select(self, trailer=None):
        if len(self.items) == 1:
            return self.items[0]
        else:
            self.show()
            if trailer is not None:
                print(self.filled(trailer))
            return self.items[self.get()]

    def filled(self, items):
#        s = ", ".join(items)
        print("      ", str(items))

if __name__ == '__main__':
    m = menu("fish", "dog", "carrot")
    sel = m.select()
    print("selected: %s" % sel)
    
