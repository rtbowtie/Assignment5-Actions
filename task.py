import math


def firstrun():
    return "success"


def area(radius):
    pi = math.pi
    mid = pow(radius, 2)
    area = pi*mid
    return area

def listFunc(list):
    var1 = list[0]
    num = len(list)
    var2 = list[num - 1]
    list2 = [var1, var2]
    return list2
