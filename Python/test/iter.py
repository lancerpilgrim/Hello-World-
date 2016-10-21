class Iter(object):
    
    def __init__(self):
        self.l = [1, 2]
        self.iter_count = 0

    def __iter__(self):
        return self

    def next(self):
        if self.iter_count < 2:
            self.iter_count += 1
            return self.l[self.iter_count-1]
        raise StopIteration
        

i = Iter()
print map(lambda x: x*2, i)

#for each in i:
#    print each
