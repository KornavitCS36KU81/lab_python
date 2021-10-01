#lab_8
"""
def change(money, x):
    return money // x

money = int(input("Enter total money: "))
b500 = change(money, 500)
left = money- b500 * 500

b100 = change(left, 100)
left = left - b100*100

b20 = change(left, 20)
left = left - b20*20

b5 = change(left, 5)
left = left - b5*5

b1 = left

print("500: %d" %b500)
print("100: %d" %b100)
print(" 20: %d" %b20)
print("  5: %d" %b5)
print("  1: %d" %b1)
"""
"""
from math import pi
def circle(r):
    circle = pi * (r**2)
    return circle
def circumference(r):
    circumference =  2 * pi * r
    return circumference
def sphere(r):
    sphere = 4/3 * pi * (r**3)
    return sphere
    

r = float(input("Enter a radius: "))
print('Area of a circle with radius %.2f is %.2f.' % (r, circle(r)))
print('Circumference of a circle with radius %.2f is %.2f.' % (r, circumference(r)))
print('Volume of sphere with radius %.2f is %.2f.' % (r, sphere(r)))
"""
"""
def digit(num):
    return num % 10

def tens(num):
    num = num // 10
    return num % 10

def hundreds(num):
    num = num // 100
    return num %10

def thousands(num):
    return num // 1000

def sum_digits(num):
    i = 0
    sum_num = 0
    while i < 4:
        sum_num = sum_num + (num % 10)
        num //= 10
        i += 1
    return sum_num
    
n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % (sum_digits(n)))
"""
"""
def simple_interest(p, r, t):
    return p + (p*r*t)/100
def compound_interest(p, r, t):
    return p * ((1+r/100)**t)
    
p = int(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))
print('Return money for simple interest calculation is %.2f Baht.' % (simple_interest(p, r, t)))
print('Return money for compound interest calculation is %.2f Baht.' % (compound_interest(p, r, t)))
"""

"""
def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s

def time_elapsed(start_time, finish_time):
    total = finish_time - start_time
    h = total // 3600
    total = total - (h * 3600)
    
    m = total // 60
    total = total - (m * 60)
    return  "{:d} hours {:d} minutes {:d} seconds.".format(h,m,total)

def read_hour():
    h = int(input("Enter hour: "))
    return h
def read_minute():
    m = int(input("Enter minute: "))
    return m
def read_second():
    s = int(input("Enter second: "))
    return s
    
    
    
def read_time():
    print('>> ', end='')
    hour = read_hour()
    print('>> ', end='')
    minute = read_minute()
    print('>> ', end='')
    second = read_second()
    return to_seconds(hour, minute, second)

print('Start time:')
start_time = read_time()
print('Finish time:')
finish_time = read_time()
print('Elapsed time is', time_elapsed(start_time, finish_time))
"""