#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:29:10 2016

@author: zeromh
"""

import nsfg
df = nsfg.ReadFemPreg()

df['birthord_bin'] = df.birthord.apply \
    (lambda x: '1st' if x == '1ST BIRTH' else '2nd+')
live = df[df.outcome == 1]
multi_baby = live.groupby('caseid').filter(lambda x: len(x) > 1)

multi_baby.groupby(['caseid', 'birthord_bin']). \
    agg({'prglngth': np.mean}). \
    groupby(level = 'caseid'). \
    agg(lambda x: x.iloc[0] - x.iloc[1]). \
    mean()
