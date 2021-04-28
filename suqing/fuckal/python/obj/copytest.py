# coding:utf8
import copy
class CopyTest(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


if __name__ == '__main__':
    obj = CopyTest(1, 2, 3, name = 'test_copy', type = 'a')
    print(obj.__reduce_ex__(5))
    obja = copy.deepcopy(obj)
    a = [1, 'hello', [99, 100]]
    b = copy.deepcopy(a)
