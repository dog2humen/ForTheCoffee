# coding:utf8

"""
    RingBuffer简单实现
"""
class RingBuffer(object):

    def __init__(self, size = 10):
        self.size = size
        self.data = []
    class __FULL(object):
        def append(self, ele):
            self.data[self.cur] = ele
            self.cur = (self.size + 1) % self.size

        def get(self):
            res = self.data[self.cur:] + self.data[:self.cur]
            return res


    def append(self, ele):
        self.data.append(ele)
        if len(self.data) == self.size:
            self.__class__ == self.__FULL
            print(self.__FULL)
            print(self.__class__)
            self.cur = 0


    def get(self):
        return self.data

    


if __name__ == '__main__':
    obj = RingBuffer()
    for i in range(11):
        obj.append(i)
    
    res = obj.get()
    obj.append(11)
    res = obj.get()
