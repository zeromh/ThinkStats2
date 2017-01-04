"""This file contains code used in "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import pandas

import thinkplot
import thinkstats2
import matplotlib.pyplot as pyplot
import scipy


def Clean(s):
    """Converts dollar amounts to integers."""
    try:
        return int(s.lstrip('$').replace(',', ''))
    except ValueError:
        if s == 'Under':
            return 0
        elif s == 'over':
            return np.inf
        return None


def ReadData(filename='hinc06.csv'):
    """Reads filename and returns populations in thousands

    filename: string

    returns: pandas Series of populations in thousands
    """
    data = pandas.read_csv(filename, header=None, skiprows=9)
    cols = data[[0, 1]]
        
    res = []
    for _, row in cols.iterrows():
        label, freq = row.values
        freq = int(freq.replace(',', ''))

        t = label.split()
        low, high = Clean(t[0]), Clean(t[-1])

        res.append((high, freq))

    df = pandas.DataFrame(res)
    # correct the first range
    df[0][0] -= 1
    # compute the cumulative sum of the freqs
    df[2] = df[1].cumsum()
    # normalize the cumulative freqs
    total = df[2][41]
    df[3] = df[2] / total
    # add column names
    df.columns = ['income',  'freq', 'cumsum', 'ps']
    return df


def main():
    df = ReadData()
    print(df)
    
    print('Evaluate income as pareto distribution:')
    pyplot.plot(df.income, 1-df.ps)
    pyplot.yscale('log')
    pyplot.xscale('log')
    pyplot.show()

    incomes = np.repeat(df.income, df.freq)
    incomes.sort_values(inplace=True)
    # Can also evaluate using thinkstats2 cdf:
#    cdf = thinkstats2.Cdf(incomes)
#    thinkplot.Cdf(cdf, complement=True)
#    thinkplot.Show(yscale='log', xscale='log')
    
    print('Evaluate income as lognormal distribution:')
    sample = scipy.stats.norm.rvs(size = len(incomes))
    sample.sort()
    pyplot.plot(sample, incomes)
    pyplot.yscale('log')
    pyplot.show()


if __name__ == "__main__":
    main()