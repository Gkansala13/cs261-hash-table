# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Grayson Kansala


class HashTable:
    def __init__(self , size = 10):
        self.size = size
        self.data= [[] for i in range(self.size)]
        self.keys=[]

    def __setitem__ (self, key, value):
        self.keys = key
        self.values = value
        self.data[2] = [[key,value]]
        
    def __getitem__ (self, key):
        for i in self.keys:
            if i == key:
                return self.data[i]

    def hash(self, value):
        return hash(value) % self.size






       