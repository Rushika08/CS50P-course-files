class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError()
        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if (n<0) or not (isinstance(n, int)) or ((self.cookies + n) > self.capacity):
            raise ValueError
        else:
            self.cookies = self.cookies + n

    def withdraw(self, n):
        if (n<0) or not (isinstance(n, int)) or ((self.cookies - n) < 0):
            raise ValueError
        else:
            self.cookies = self.cookies - n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
