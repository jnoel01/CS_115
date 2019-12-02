############################################################
#Jessica Noel
#
#  CS115-B/C HW1 ~ Applications of Map & Reduce
#
#  Due : Sep. 20th, 2019
#
#  Pledge : I pledge my honor that I have abided by the Stevens Honor System
# 
############################################################

from functools import reduce
from math import factorial, sqrt

############################################################

def taylorApproxE(lastIter):
    '''will taylor approximate e^ a given number'''
    def add(x,y):
        return x+y
    def oneOver(x):
        return 1/factorial(x)
    return reduce(add, map(oneOver, range(lastIter+1)))

############################################################

def vectorNorm(vect1):
    '''will find the sqaure root of the sum of sqaures in a given list'''
    def sq(x):
        return x*x
    def add(x,y):
        return x+y
    return sqrt(reduce(add, map(sq, vect1)))


############################################################
def arithMean(vect1):
    '''will find the mean of numbers in a given list'''
    def add(x,y):
        return x+y
    return reduce(add, vect1)/len(vect1)



