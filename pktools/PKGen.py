import scipy.interpolate as interp
import scipy.integrate as integ

import numpy as np

import logging

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

    def generate(self, nevts):
        '''Generate 'nevts' events using the PDF'''
        _data_set = [self._gen_func(np.random.uniform()) for i in range(nevts)]
        return np.array(_data_set)
