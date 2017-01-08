#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 23:46:08 2016

@author: zeromh
"""
import thinkstats2
from nsfg import *

df = ReadFemPreg()

df['birthord_bin'] = df.birthord.apply(lambda x: \
                        'first' if x == 1 else 'other')

print 'The average weight of first and non-first babies is:'
print df.groupby('birthord_bin').totalwgt_lb.mean()

first = df[df.birthord_bin == 'first'].totalwgt_lb
other = df[df.birthord_bin == 'other'].totalwgt_lb

print "Cohen's d for this difference is:", \
    thinkstats2.CohenEffectSize(first, other)

# This is a very small difference.
# Additionally, this effect shows that first babies weigh slightly
# LESS than other babies, even though we learned in the book chapter that
# first babies are slightly LATE. This is odd.