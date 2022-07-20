import random
num = '1658277721'

def probablyPrime(num, k):
    """Using Miller-Rabin primality test"""
    if num == 2 or num == 3:
        return True
    if num < 2:
        return False
    if not num & 1:
        return False

    # find s and d such that n−1 = (2**s)*d with d odd
    d = (num-1) >> 1
    s = 1
    while not (d & 1):
        d = d >> 1
        s += 1

    # run k times
    for _ in range(k):
        a = random.randint(2, num-2)
        x = pow(a, d, num)  # more efficient than  x = a**d % num
        if not (x == 1 or x == num-1):
            for _ in range(s-1):
                x = (x**2) % num
                if x == 1:
                    return False
                if x == num-1:
                    break
            if not x == num-1:
                return False
    return True


def largestPrime(num):
    num_list = set([])
    for i in range(0,len(num)+1):
        for j in range(i+1,len(num)+1): 
            inum = int(num[i:j])
            # Don't append numbers that have already appeared
            if inum not in num_list:
                num_list.add(inum)

    # Convert to list and sort
    num_list = list(num_list)
    num_list.sort(reverse=True)

    for num in num_list:
        print('Checking ' + str(num))
        if probablyPrime(num,100):
            print('\n' + str(num) + ' is probably the largest prime!')
            return

largestPrime(num)