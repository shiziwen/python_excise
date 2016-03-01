import threading

class Singleton(object):
     def __new__(cls, *args, **kwargs):
         if not hasattr(cls, '_inst'):
             cls._inst = super(Singleton, cls).__new__(cls, *args, **kwargs)
         return cls._inst


class SingletonThread(object):
     _instance_lock = threading.Lock()

     def __new__(cls, *args, **kwargs):
         if not hasattr(cls, '_inst'):
             with cls._instance_lock:
                 if not hasattr(cls, '_inst'):
                     cls._inst = super(SingletonThread, cls).__new__(cls, *args, **kwargs)
         return cls._inst


class A(Singleton):
    def __init__(self, s):
        self.s=s

a=A('aaaa')
print 'a: ', id(a), a.s
b=A('bbbbb')
print 'b: ', id(b), b.s
print 'c: ', id(a), a.s


class SingletonMixin(object):
    _instance_lock = threading.Lock()
    _instance = None

    @classmethod
    def instance(cls):
        if not cls._instance:
            with cls._instance_lock:
                if not cls._instance:
                    cls._instance = cls()
        return cls._instance

class B(SingletonMixin):
    pass

x=B.instance()
y=B.instance()

print 'x:', id(x)
print 'y:', id(y)

class C(SingletonThread):
    def __init__(self,s):
        self.s = s

m = C('ccccc')
print 'm: ', id(m)
n = C('dddddddd')
print 'n: ', id(n)
print 'm: ', id(m)
