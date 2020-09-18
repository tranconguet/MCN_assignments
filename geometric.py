import math


def prob(n, p):
    return p ** n


def infoMeasure(n, p):
    return - math.log(prob(n, p), 2)


def sumProb(N, p):
    s = 0
    for i in range(1, N + 1):
        s += prob(i, p)
    return s


''' sumProb with N = 5, p = 0.5:  0.96875 '''
''' sumProb with N = 10, p = 0.5:  0.9990234375 '''
''' sumProb with N = 20, p = 0.5:  0.9999990463256836 '''


def approxEntropy(N, p):
    s = 0
    for i in range(1, N + 1):
        s += prob(i, p) * infoMeasure(i, p)
    return s


''' entropy with N = 5, p = 0.5: 1.78125  '''
''' entropy with N = 10, p = 0.5:  1.98828125 '''
''' entropy with N = 20, p = 0.5:  1.999979019165039 '''

print(approxEntropy(20, 0.5))
