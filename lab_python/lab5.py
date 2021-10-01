#input
number = int(input())
if number <= 0:
    print("ERROR")
else:
    while True:
        if number == 0:
            break        
        integer = number % 10
        number = number // 10
        print(integer)


n = int(input())
i = 1
total_score = 0
n_40 = 0
while i <= n:
    score = float(input())
    if score >= 40:
        n_40 += 1
    total_score = total_score + score
    i += 1
print("{:.2f} {}".format(total_score/n,n_40))

count = 0
height = int(input('Enter height: '))
consume = height * 2 - 2
mid_space = 3

while count < height:
    space = 0
    while space < consume:
        print(end=' ')
        space += 1
    if count == 0:
        print('1')
    else:
        print('1',end='')
        print(mid_space*' '+'1')
        mid_space += 4
    count += 1
    consume -= 2



import math
count = 0
score_min = math.inf
score_max = -math.inf
sum_integer = 0
while True:
    integer = input()
    if integer == '':
        break
    integer = float(integer)
    #process
    if integer > score_max:
        score_max = integer        
    if integer < score_min:
        score_min = integer
        
    sum_integer+=integer
    count += 1
    
print("{:.2f} {:.2f}".format(score_max,score_min))    
print("{:.2f} {:.2f}".format(sum_integer,sum_integer/count))


hours = int(input("Enter number of hours: "))
minutes = int(input("Enter number of minutes: "))
buyAmt = int(input("Enter shopping amount: "))

if minutes > 0:
    hours = hours + 1
if hours < 0 or hours > 20 or minutes < 0 or minutes > 59:
    print('Invalid time.')
elif hours <= 2 or buyAmt > 3000:
    print("No charge, thank you.")
else:
    i = 2
    count_Baht = 0
    while i <= hours:
        if i == 3:
            count_Baht += 20
        elif i == 4:
            count_Baht += 20
        elif i >= 5:
            count_Baht += 50
        i += 1
    if buyAmt >= 300:
        count_Baht -= 40
            
    if count_Baht > 0:
        print("Total amount due is {} Baht, thank you.".format(count_Baht))
    else:
        print("No charge, thank you.")