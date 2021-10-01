"""
x = int(input("Enter a target (4-digit integer): "))
y = int(input("Enter your guess (4-digit integer): "))
a1 = 0
b1 = 0
c1 = 0
d1 = 0

a2 = 0
b2 = 0
c2 = 0
d2 = 0

a1 = x // 1000
b1 = (x - (a1 * 1000)) // 100
c1 = (x - (a1 * 1000 + b1 * 100)) // 10
d1 = x - (a1 * 1000 + b1 * 100 + c1 * 10)

a2 = y // 1000
b2 = (y - (a2 * 1000)) // 100
c2 = (y - (a2 * 1000 + b2 * 100)) // 10
d2 = y - (a2 * 1000 + b2 * 100 + c2 *10)

#positions
positions_count = 0
if a1 == a2:
    positions_count += 1                       
if b1 == b2:
    positions_count += 1
if c1 == c2:
    positions_count += 1
if d1 == d2:
    positions_count += 1
    
#digit
digit_count = 0
if a1 == b2 or a1 == c2 or a1 == d2:
    digit_count += 1
if b1 == a2 or b1 == c2 or b1 == d2:
    digit_count += 1
if c1 == a2 or c1 == b2 or c1 == d2:
    digit_count += 1
if d1 == a2 or d1 == b2 or d1 == c2:
    digit_count += 1
    
if positions_count == 4:
    print("Congratulations, you just mastered my mind!!")
else:
    #digit
    if digit_count ==  0:
        digit = "no digits"
    elif digit_count == 1:
        digit = "one digit"
    elif digit_count == 2:
        digit = "two digits"
    elif digit_count == 3:
        digit = "three digits"
    elif digit_count == 4:
        digit = "four digits"
        
    #positions
    if positions_count == 0:
        positions = "No positions"
    elif positions_count == 1:
        positions = "One position"
    elif positions_count == 2:
        positions = "Two positions"
    elif positions_count == 3:
        positions = "Three positions"
    print("{} correct, {} correct".format(positions,digit))


number = int(input())
while True:
    if number < 10:
        break
    total = 0
    
    while True:
        if number == 0:
            break
        total = total + (number % 10)
        number = number // 10
    number = total
print(number)

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
nmax = 0
nmin = 0
count = 0
if n2 > n1:
    nmax = n2
    nmin = n1
else:
    nmax = n1
    nmin = n2

while True:
    if nmin == 0:
        break
    else:
        a = nmax%nmin
        nmax = nmin
        nmin = a
x = (n1*n2)//nmax 

print("  >> gcd({}, {}) ={:7.0f}".format(n1, n2, nmax))
print("  >> lcm({}, {}) ={:7.0f}".format(n1, n2, x))


count = int(input("Enter a number: "))
if count <= 0 or count > 26:
    print("Invalid input, program terminates.")
else:
        
    i = 0
    while i < count:
        j = 0
        while j <= i:
            charater = ord('A') + j
            print(chr(charater),end = '')
            j += 1
        print()
        i += 1      
        
    i = 0
    while count > i:
        j = 0
        while j < count-1:
            charater = ord('A') + j
            print(chr(charater),end = '')
            j += 1
        print()
        count -= 1
"""

"""
x = int(input('Enter positive integer: '))
y = 2
if x <= 0:
    print('Invalid number.')
elif x == 1:
    pass    
else:
    while x != 1 :
        if x % y == 0 :
            x = x // y
            print(y)
            continue
        y += 1
"""