import scipy.interpolate as interp
import scipy.integrate as integ
import numpy as np
import logging
import matplotlib.pyplot as plt
import yaml

logging.basicConfig()

class PKGen(object):
    def __init__(self, func, x_range):
        '''
        PKGen Class

        Generate a dataset using a user defined PDF

        Arguments
        ---------

        func     (lambda)         A lambda representing the function to
                                  use during dataset generation

        x_range  (float, float)   Range for the normalisation
        '''
        self._logger = logging.getLogger('PKGen')
        self._logger.setLevel('INFO')
        self._range = x_range
        self._function = lambda x : self._norm_factor(func)*func(x)
        self._gen_func = self._inv_cdf()

    def _norm_factor(self, func):
        x = np.linspace(*self._range, 100)
        y = func(x)
        return pow(integ.trapz(y,x), -1)

    def _inv_cdf(self):
        x = np.linspace(*self._range, 100)
        y = self._function(x)
        cum_integ = integ.cumtrapz(y,x)
        return interp.interp1d(cum_integ, x[:-1], bounds_error=False)

    def generate(self, nevts, show_plot=100, save_data=False):
        '''
        Generate 'nevts' events using the PDF

        Arguments
        ---------

        nevts     (int)        Number of events to generate

        Optional Arguments
        ------------------

        show_plot   (int)      Either an integer or None depending on
                               whether you wish the results to be plotted
                               as a histogram

        save_data   (string)   Either a string representing the output yaml file
                               address or False if you do not want to save the data
        '''
        _data_set = [self._gen_func(np.random.uniform()) for i in range(nevts)]
        _data_set = np.array(_data_set)

        if show_plot:
            plt.hist(_data_set, bins=show_plot)

        if save_data:
            yaml.dump(_data_set, open(save_data, 'w'))
