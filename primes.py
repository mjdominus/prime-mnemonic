class primes():
    def __init__(self, n=None):
        self.p = { 2, 3 }
        self.max = 3
        if n is not None:
            self.extend_max(n)

    def is_prime(self, n):
        self.extend_max(n)
        return n in self.p

    def extend_max(self, n):
        while n > self.max:
            self.check_next()
        return

    def check_next(self):
        self.max += 1
        n = self.max
        for p in self.p:
            if p * (n//p) == n:
                return          # composite
        self.p.add(n)           # prime

    def list(self, n=None):
        if n is not None:
            self.extend_max(n)
        return sorted(self.p)
