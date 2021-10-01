"""
print("recursive")
def recursive(n):
    if n == 0:
        return 0
    return n + recursive(n - 1)
recursive(5)
"""
"""
recursive(5)
5 + recursive(4)
5 + 4 + recursive(3)
5 + 4 + 3 + recursive(2)
5 + 4 + 3 + 2 + recursive(1)
5 + 4 + 3 + 2 + 1 + recursive(0)
5 + 4 + 3 + 2 + 1 + 0

5 + 10
.... 4 + 6
........ 3 + 2
............ 1 + 0
"""
"""
5
def fibo(n):
    if n <= 2:
        return 1
    else:
        fibo = 0
        f1 = 0
        f2 = 1
        i = 1
        while i != n:
            fibo = f1 + f2
            f1 = f2
            f2 = fibo
            i += 1
            
    return fibo

n = int(input("Enter n: "))
print("fibo(%d) = %d" %(n,fibo(n)))
"""

"""
1
def check_prime(n):
        i = 2
        while n % i > 0:
                i = i + 1
        if i == n:
            return n
"""
"""
3
def nb_year(p0, percent, aug, p):
    i = 0
    total_p0 = 0
    while p0 < p:
        total_p0 = round(p0 * (percent / 100) + aug)
        p0 += total_p0
        i += 1
    return i
print( nb_year(1500000, 0.25, 1000,  2000000) )
"""
"""
def factor_count(n):
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count

n = int(input("Enter n: "))
c = factor_count(n)
print(c)
"""
"""
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
n = int(input("Enter n: "))
print(f"{n}!", "=" , factorial(n))
"""
"""
6
def Alternating(n):
    i = 1
    count = 0
    while i <= n:
        if i % 2 == 0:
            count -= i
        else:
            count += i
        i += 1
    return count
n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to %d is %d" %(n,Alternating(n)))
"""