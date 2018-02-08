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
        

def gen():
    end = 10
    start = 1
    while True:
        try:
            index = yield start
            start += index
            assert start < end
        except AssertionError:
            print("end")
            return start + end
        except GeneratorExit:
            print("exit")
            return start


# i = Iter()

#g = gen()
#next(g)
#print(g.send(3))
#print(g.send(11))

#for i in range(0, 3):
#    print(i)
a = {"p": {"q": 1}}

b = a["p"]["q"]
def t(a):
    a = 3
    return a
b = t(b)
print(b)
print(a)

def recurPrintPath(dic):
    for key in dic.keys():
	# 判断下一级是否还是字典，如果是字典继续递归
	if type(dic[key]) == type({}):
            recurPrintPath(dic[key])
	else:
            print(dic[key])


recurPrintPath(a)
