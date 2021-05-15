def numPrimo(num):
    if (num < 2):
        return False
    else:
        for n in range(2, num):
            if num % n == 0:
                return False
        return True
        