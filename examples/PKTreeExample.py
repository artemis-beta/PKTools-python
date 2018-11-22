import sys

sys.path.insert(0, '../source/')

import pktools.PKTree as PKT
import pktools.PKPlot as PKP

import numpy as np

x = PKT.PKTree("My_Tree")
n = np.array([i**2 for i in range(300)])
m = np.array([i-6*7 for i in range(300)])
x.addBranch("K_MM", n, "MeV")
x.addBranch("K_DERP", m, "Od")
print(x)
print(x.getEntry(67))

hist = PKP.PKHist(x.getBranchData("K_MM"))
hist.setXLabel("x")
hist.setYLabel("y")
hist.setNBins(100)
hist.setTitle('Test Hist $ \\alpha$')
hist.Draw()
