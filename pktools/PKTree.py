import PKPlot as PKP

class PKLeaf:
    def __init__(self, val):
        self._value = val

class PKBranch:
    def __init__(self, name, data=None, units=""):
        self._name = name
        self._data = data
        self._units = units

    def fillBranch(self, data):
        self._data = data

    def getName(self):
        return self._name

    def _branch_getEntry(self, i):
        return self._data[i]

    def getData(self):
        return self._data

    def __str__(self):
        out_str = '''
        {}/{}
        '''.format(self._name, self._units)
        return out_str

class PKEvent:
    def __init__(self, tree_, i):
            self._id = i
            self._parenttree = tree_
            for branch in self._parenttree._branches:
                setattr(self, self._parenttree._branches[branch].getName(), self._parenttree._branches[branch]._branch_getEntry(i))
         
    def __str__(self):
        out_str = '''
    ======================================
      PKTree_{}/PKEvent_{}
    ======================================
        '''.format(self._parenttree.getName(), self._id)

        for branch in self._parenttree._branches:
            out_str += '''
      {}:\t{}
            '''.format(self._parenttree._branches[branch].getName(), getattr(self, self._parenttree._branches[branch].getName()))
        out_str += '''
    --------------------------------------
        '''
        return out_str

class PKTree:
    def __init__(self, name="PKTree", branches=None):
        self._name = name
        if branches:
            self._branches = branches
        else:
            self._branches = {}
    
    def getName(self):
        return self._name

    def addBranch(self, branch_name, data=None, units=""):
        self._branches[branch_name] = PKBranch(branch_name, data, units)

    def getBranch(self, branch_name):
        return self._branches[branch_name]

    def getBranchData(self, branch_name):
        return self.getBranch(branch_name).getData()

    def getN(self):
        return len(self._branches[self._branches.keys()[0]]._data)

    def getEntry(self, i):
        return PKEvent(self, i)

    def __str__(self):
        out_str = '''
    **************************************
        PKTREE:   {}
        ENTRIES:  {}
    **************************************
        '''.format(self.getName(), self.getN())

        for branch in self._branches:
            out_str += '''
       {}
            '''.format(branch.__str__())
            out_str += '''
    --------------------------------------
            '''
        return out_str

    def Draw(self, branch_name):
        hist = PKP.PKHist(self.getBranchData(branch_name))
        hist.Draw()
