import numpy as np
import scipy.stats as sps

class ConjugateBayes(data, sigma2Lhd, muPrior=0, sigma2Prior=1):
    """
    Implements Gaussian-Gaussian conjugate model
    """

    def __init__(self):
        self.data = data
        self.sigma2Lhd = sigmaLhd
        self.muPrior = muPrior
        self.sigma2Prior =sigmaPrior

    def estimate(self):
        """
        returns the posterior mean
        """
        n = len(self.data)
        self.muPosterior = 1/(1/self.sigma2Prior+n/self.sigma2Lhd) * (self.muPrior/self.sigma2Prior+
                    +np.sum(self.data)/self.sigma2Lhd)
        return self.muPosterior

    def interval(self, alpha):
        """
        return a centered posterior credible interval with mass >= 1-alpha
        """
        self.estimate()
        self.sigma2Posterior = 1/(1/self.sigma2Prior+n/self.sigma2Lhd)
        lo, hi = sps.norm(loc=self.muPosterior, scale=np.sqrt(sigma2Posterior)).interval(alpha)
        return lo, hi
