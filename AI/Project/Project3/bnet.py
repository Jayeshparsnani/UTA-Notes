import sys
import copy
from functions import *

def __main__(argv):
    # If there is some conditional probability.
    if "given" in argv:
        givenIndex = argv.index("given")
        denominator = argv[givenIndex+1:]
        numerator = argv[1:givenIndex] + denominator
        # print(givenIndex,denominator, numerator)
        # print(reqd_notations(numerator))
        
        # Function calling from other file (Functions.py).
        n = prob_compute(reqd_notations(numerator))
        d = prob_compute(reqd_notations(denominator))
        print("Probability = " + str(n/d))
    else:
        print("Probability = " + str(prob_compute(reqd_notations(argv[1:]))))

__main__(sys.argv)