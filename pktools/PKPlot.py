import matplotlib.pyplot as plt

class PKHist:
    def __init__(self, x, bins=None, Range=None, normed=False, weights=None, cumulative=False, bottom=None, histtype='bar', align='mid', orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, hold=None, data=None):
        
        self._x = x
        self._bins = bins if bins else 10
        self._range = Range
        self._normed = normed
        self._weights = weights
        self._cumulative = cumulative
        self._bottom = bottom
        self._histtype = histtype
        self._align = align
        self._orientation = orientation
        self._rwidth = rwidth
        self._log = log
        self._colour = color
        self._name = label
        self._stacked = stacked
        self._hold = hold
        self._data = data
        self._xlabel = "x"
        self._ylabel = "y"
        self._title = ""

        self._histplot = None

        self._gen_hist()

    def _gen_hist(self):
        self._histplot = plt.hist( self._x           ,
                                   self._bins        ,
                                   self._range       ,  
                                   self._normed      ,
                                   self._weights     , 
                                   self._cumulative  ,
                                   self._bottom      ,
                                   self._histtype    ,
                                   self._align       ,
                                   self._orientation , 
                                   self._rwidth      ,
                                   self._log         ,
                                   self._colour      ,
                                   self._name        ,
                                   self._stacked     ,
                                   self._hold        ,
                                   self._data
                                   )
        plt.xlabel(self._xlabel)
        plt.ylabel(self._ylabel)
        plt.title(self._title)

    def setXLabel(self, label):
        self._xlabel = label
        plt.clf()
        self._gen_hist()

    def setYLabel(self, label):
        self._ylabel = label
        plt.clf()
        self._gen_hist()

    def setTitle(self, label):
        self._title = r'{}'.format(label)
        plt.clf()
        self._gen_hist()

    def getName(self):
        return self._name

    def setNBins(self, n_bin):
        plt.clf()
        self._bins = n_bin
        self._gen_hist()

    def setRange(self, Range):
        plt.clf()
        self._range = Range
        self._gen_hist()

    def Draw(self):
        plt.show()
