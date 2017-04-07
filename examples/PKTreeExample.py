import sys

sys.path.insert(0, '../source/')

import PKTree as PKT
import PKPlot as PKP

x = PKT.PKTree("My_Tree")
n = [i**2 for i in range(300)]
m = [i-6*7 for i in range(300)]
x.addBranch("K_MM", n, "MeV")
x.addBranch("K_DERP", m, "Od")
print(x)
print(x.getEntry(67))

hist = PKP.PKHist(x.getBranchData("K_MM"))
hist.Draw()
