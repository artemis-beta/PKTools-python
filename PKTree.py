
class PKLeaf:
    def __init__(self, var):
        self._val = var;

    def getVal(self):
        return self._val;

class PKBranch:
    def __init__(self, branch_name):
        self._branch_name = branch_name
        self._leaves = []

    def getEntry(self, index):
        return self._leaves[index];

    def getName(self):
        return self._branch_name

    def fillBranch(self, entries):
        self._leaves = entries

    def getSize(self):
        return len(self._leaves)

    def Print(self):
       _branch_str='''
**********************************************
  PKBranch :    {}       |        {}
**********************************************
       '''.format(self._branch_name, self.getSize())
       print(_branch_str)

class PKTree:
    def __init__(self, name="NewTree"):
        self._branches = []

    def getBranch(self, branch_name):
        for branch in self._branches:
            if branch._branch_name:
                return branch

    def addBranch(self, branch_name):
        self._branches.append(PKBranch(branch_name))

    def Print(self):
        for branch in self._branches:
            branch.Print()

if __name__ in "__main__":
    x = PKTree("DecayTree")
    x.addBranch("Ints")
    x.getBranch("Ints").fillBranch([i for i in range(100)])
    x.Print()
    x.getBranch("Ints").getEntry(3).getVal()
