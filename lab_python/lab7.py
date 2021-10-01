"""
number = int(input("Enter a number: "))

if number < 0:
    print("Invalid input, program terminates.")
else:
    i = 0
    count = 1
    while i <= number:
        j = i
        print("{}! = ".format(i),end = '')
        
        if i <= count:
            print("1 = 1",end = '')
        
        else:
            total = 1
            while j >= count:
                total *= j
                if j == 1:
                    print("1",end = '')
                else:
                    print("{} x ".format(j),end = '')
                j -= 1
            print(" = {}".format(total),end = '')
        print()
        i += 1


while True:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Invalid input, try again.")
    elif number == 0:
        print("End of program, goodbye.")
        break
    elif number == 1:
        print("Invalid input, try again.")
        
    elif number == 2 or number == 3 or number == 5 or number == 7:
        print(f"{number} is a prime number.")
        #
    elif number % 2 == 0 or number % 3 == 0 or number % 4 == 0 or number % 5 == 0 or number % 6 == 0 or number % 7 == 0 or number % 8 == 0 or number % 9 == 0 or number % 10 == 0:
        print(f"{number} is not a prime number.")
        #
    else:
        print(f"{number} is a prime number.")


h = int(input("Enter height: "))
w = int(input("Enter width: "))

if h <= 0 or w <= 0:
    print("Invalid input, program terminates.")
else:
    i = 1
    while i <= h:
        if i % 2 == 0:
            print(' *'*w,end='')
        else:
            print('* '*w,end='')
        print()
        i += 1
"""

"""
integer = int(input("Enter positive integer: "))
if integer <= 0:
    print("Invalid number.")
elif integer == 1:
    pass
else:
    count_prime = 2
    while integer != 1:
        while True:
            if (integer % count_prime) != 0:
                break
            integer = integer // count_prime
            print(count_prime) 
        count_prime += 1
"""

number = int(input())
#exponent_2
c = number**2
count = 0
a = 1

while a <= number:
    b = 1
    while b <= number:
        if (a**2 + b**2) == c and (a < b):
            count+=1
        b+=1
    a+=1
print(count)