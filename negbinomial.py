import math


def prob(n, p, r):
    n1_c_r1 = math.factorial(n - 1) / (math.factorial(n - r) * math.factorial(r - 1))
    return n1_c_r1 * (p ** r) * ((1 - p) ** (n - r))


def infoMeasure(n, p, r):
    return - math.log(prob(n, p, r), 2)


def sumProb(N, p, r):
    s = 0
    for i in range(r, N + 1):
        s += prob(i, p, r)
    return s


''' sumProb with N = 5, r = 2, p = 0.5:  0.8125 '''
''' sumProb with N = 10, r = 2, p = 0.5:  0.9892578125 '''
''' sumProb with N = 20, r = 2, p = 0.5:  0.9999799728393555 '''


def approxEntropy(N, p, r):
    s = 0
    for i in range(r, N + 1):
        s += prob(i, p, r) * infoMeasure(i, p, r)
    return s


''' entropy with N = 10, r = 2, p = 0.5:  2.6178901263724024 '''
''' entropy with N = 20, r = 2, p = 0.5:  2.7111142477765284 '''
''' entropy with N = 50, r = 2, p = 0.5: 2.7114687242185123 '''

print(approxEntropy(50, 0.5, 2))
