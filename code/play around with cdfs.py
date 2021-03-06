#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:29:10 2016

@author: zeromh
"""

import nsfg, thinkstats2, matplotlib.pyplot as pyplot, scipy
df = nsfg.ReadFemPreg()


live = df[df.outcome == 1]

weights = live.totalwgt_lb
cdf = thinkstats2.Cdf(weights)
thinkplot.Cdf(cdf)

mu = np.mean(cdf.Values())
sigma = np.std(cdf.Values())
model_sample = scipy.stats.norm.rvs(loc = mu, scale = sigma, size = len(weights))
model_cdf = thinkstats2.Cdf(model_sample)
thinkplot.Cdf(model_cdf)
