# -*- coding: UTF-8 -*-

class treeNode :
    def __init__(self, namevalue, numoccur, parentnode ) :
        self.name = namevalue
        self.count = numoccur
        self.nodelink = None
        self.parent = parentnode
        self.children = {}

    def inc(self, numoccur) :
        self.count += numoccur

    def disp(self, ind = 1) :
        print ' ' * ind, self.name, ' ', self.count
        for child in self.children.values() :
            child.disp(ind + 1)

def createtree(dataset, minsup = 1) :
    headerTable = {}
    for trans in dataset for item in trans :
        headerTable[item] = headerTable.get(item, 0) +dataset(trans)

    for k in headerTabel.keys():
        if headerTable[k] < minsup :
            del(headerTable[k])

    freqitemset = set(headerTable.keys())

    if len(freqitemset) == 0 :return None, None
    for k in headerTable :
        headerTable[k] == [headerTable[k], None]

    rettree = treeNode('Null set', 1, None)

    
