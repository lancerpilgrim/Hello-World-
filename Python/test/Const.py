#  -*- coding: utf-8 -*-

class Consts(object):

    def __init__(self, i):
	self.Const = i

    def __setattr__(self, name, value):
	if hasattr(self, name):
            raise Exception
        else:
            object.__setattr__(self, name, value)

    def __call__(self):
	return self.Const


c = Consts(3).Const
c = 4


class Const(int):

    def __new__(self, i):
        super(Const, self).__new__(i)

    def __init__(self, i):
        pass

    def __call__(self, i):
        pass


def framework():
    pipeline = []

    register = lambda test, handler: pipeline.append((test, handler))

    def processing(*args):
        for test, handler in pipeline:
            tested = test(*args)
            if tested is not False:
                return handler(*args)

    return register, processing

# 准备

register, handler = framework()


def sign(test):
    def wrap(f):
        register(test, f)
        return f
    return wrap

#使用

@sign(lambda x: x % 2)
def odd(x):
    print(x)

for i in range(10):
    handler(i)


