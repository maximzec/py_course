from math import *
MAX_PRIORITY = 1000

class Pair():

    def __init__(self, key, value):
        self.value = value
        if(type(key) is not int):
            raise Exception("key is not int")
        if(key > MAX_PRIORITY):
            raise Exception("key is greater than max priority")
        self.key = key

    def setKey(self,key):
        if(type(key) is not int):
            raise Exception("key is not int")
        if(key > MAX_PRIORITY):
            raise Exception("key is greater than max priority")
        self.key = key

    def setValue(self, value):
        self.value = value

    def __str__(self):
        return "(" + str(self.key) + " -> " + str(self.value) + ")"


class PriorityRingBuffer():

    def __init__(self, size):
        self.stack = [Pair(MAX_PRIORITY,0)] * size
        self.cursor = 0
        
    def getSortKey(self , pair):
        if pair is not None:
            return pair.key
    
    def add(self, pair):
        if(type(pair) is not Pair):
            raise Exception("addable must be pair")
        if(self.cursor >= len(self.stack)):
            self.cursor = 0
        self.stack[self.cursor] = pair
        self.shuffle()
        self.cursor += 1

    def extract_minimum(self):
        pair = self.stack[0]
        self.stack[0] = Pair(MAX_PRIORITY , 0)
        self.shuffle()
        return pair
    
    def shuffle(self):
        self.stack = sorted(self.stack , key = self.getSortKey)

    def __getitem__(self,value):
        return self.stack[value]
    

    def __str__(self):
        s = ""
        for i in range(len(self.stack)):
            if(self.stack[i].key != MAX_PRIORITY):
                s += str(self.stack[i]) + " "
        return s

    




