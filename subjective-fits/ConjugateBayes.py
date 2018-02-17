import numpy as np
import scipy.stats as sps

class ConjugateBayes:
    """
    Implements Gaussian-Gaussian conjugate model
    """

    def __init__(self, data, sigma2Lhd, muPrior=0, sigma2Prior=1):
        self.data = data
        self.sigma2Lhd = sigma2Lhd
        self.muPrior = muPrior
        self.sigma2Prior = sigma2Prior
        self.N = len(self.data)

    def estimate(self):
        """
        returns the posterior mean
        """
        self.muPosterior = 1/(1/self.sigma2Prior+self.N/self.sigma2Lhd) * (self.muPrior/self.sigma2Prior
                    +np.sum(self.data)/self.sigma2Lhd)
        return self.muPosterior

    def interval(self, credibilityLevel):
        """
        return a centered posterior credible interval with mass >= 1-alpha
        """
        self.estimate()
        self.sigma2Posterior = 1/(1/self.sigma2Prior+self.N/self.sigma2Lhd)
        lo, hi = sps.norm(loc=self.muPosterior, scale=np.sqrt(self.sigma2Posterior)).interval(credibilityLevel)
        return lo, hi
