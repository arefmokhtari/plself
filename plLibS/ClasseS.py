#                   [   Plague Dr.  ]
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class Counter:
    def __init__(self):
        self.number = 0
    def get_num(self):
        self.number += 1
        return self.number
    def clear(self):
        self.number = 0
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #
class Base:
    def __init__(self, s, b):
        self.ns = Base.base(self, s, b)
    def charbase(self, n, base):
        s = '0123456789ABCDEF'
        if n < base:
            return s[n]
        else:
            return self.charbase(n//base , base) + s[ n % base]
    def base(self, s, base):
        ns = ''
        for ch in s:
            ns += self.charbase(ord(ch),base)+' '
        return ns
    def result(self):
        return self.ns
# - - - - - - - - - - - - - - - - - - - - - - - - - -  #