import numpy as np
import scipy.stats as sps

class BaselineBF:
    """
    Implements the baseline Belief Function approach when no prior is given.
    The belief function the set of candidate parameter values is the likelihood
    based belief function.
    """

    def __init__(self, data, sigma2Lhd):
        self.data = data
        self.sigma2Lhd = sigma2Lhd
        self.N = len(self.data)

    def estimate(self):
        """
        returns the maximal plausible estimate (= MLE)
        """
        return np.mean(self.data)

    def interval(self, credibilityLevel):
        """
        return a centered interval with bel(I) = credibilityLevel
        """
        alpha = 1-credibilityLevel
        mle = self.estimate()
        semi_width = self.sigma2Lhd*np.sqrt(2*np.log(1/alpha)/self.N)
        lo = mle - semi_width
        hi = mle + semi_width
        return lo, hi
