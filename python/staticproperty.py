class staticproperty(object):
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, owner):
        return staticmethod(self.fget).__get__(None, owner)()


class Foo(object):
    @staticproperty
    def bar():
        print('hai')
        return 9001


print(Foo.bar)

output = '''
hai
9001
'''
