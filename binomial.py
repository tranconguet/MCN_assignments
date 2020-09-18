import math


def prob(n, p, total):
    total_c_n = math.factorial(total) / (math.factorial(n) * math.factorial(total - n))
    return total_c_n * (p ** n) * ((1 - p) ** (total - n))


def infoMeasure(n, p, total):
    return - math.log(prob(n, p, total), 2)


def sumProb(N, p, total):
    s = 0
    for i in range(0, N + 1):
        s += prob(i, p, total)
    return s


''' sumProb with N = 3:  1.0 '''
''' sumProb with N = 5:  1.0 '''
''' sumProb with N = 10:  1.0 '''


def approxEntropy(N, p, total):
    s = 0
    for i in range(0, N + 1):
        s += prob(i, p, total) * infoMeasure(i, p, total)
    return s


''' entropy with N = 3 p = 0.5: 1.8112781244591327 '''
''' entropy with N = 10 p = 0.5: 2.706428963227331 '''
''' entropy with N = 100 p = 0.5: 4.369011409223017 '''

print(approxEntropy(100, 0.5, 100))
