## Cap 6 - functions
#EX2 - Return the greater common divisor of two integers

def gcd(n1, n2):
    gcd = 1 #initial gdc is 1
    k = 2 #possible gdc

    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k #update gdc
        k += 1

    return gcd



