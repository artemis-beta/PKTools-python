import matplotlib.pyplot as plt

class PKHist:
    def __init__(self, x, xlabel = "x", ylabel = "y", title = "", bins = None,  **kwargs):
        
        self._x = x
        self._bins = bins if bins else 10
        self._xlabel = "x"
        self._ylabel = "y"
        self._title = ""
        self._args = kwargs

        self._histplot = None

        self._gen_hist()

    def _gen_hist(self):
        self._histplot = plt.hist( self._x                  ,
                                   histtype    = 'bar'      ,
                                   orientation = 'vertical' ,
                                   align       = 'mid'      ,
                                   **self._args             ,
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
