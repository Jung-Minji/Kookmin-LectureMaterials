from math import factorial as fact
def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)  #2진수 -> 10진수
        # int(변환하려는 숫자, n) 두 번째 인자 -> n진수에서 10진수로 변환할 수 있다!
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    return 'dec -> Roman'



functions = {'factorial (!)': factorial, '-> binary' : decToBin, 'binary -> dec': binToDec, '-> roman': decToRoman}

