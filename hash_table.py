#-*-coding:utf-8-*-
class Array(object):
    def __init__(self,size = 32,init = None):
        self._size = size
        self._items = [init]*size
    def __getitem__(self,index):
        return self._item[index]
    def __setitem__(self,index,value):
        self._items[index] = value
    def __len__(self):
        return self._size
    def __iter__(self):
        for item in self._items:
            yield item
    def clear(self,value = None):
        for i in range(self._items):
            self._items[i] = value
            
class HashTable(object):
    UNUSED = None
    EMPTY = Slot(None, None)
    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0
