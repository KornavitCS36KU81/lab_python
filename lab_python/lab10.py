"""
1
scores = []
while True:
    score = int(input("Enter score: "))
    if score > 10 or score < 0:
        print("Score is out of range.")
    else:
        scores.append(score)
    if len(scores) == 20:
        break
    
print("Original list:")
print(scores)

for i in range(11):
    count = 0
    for j in scores:
        if i == j:
            count += 1
    print("{:>2d} {}".format(i,"*"*count))
"""
"""
2
def accum_sum(l):
    total = 0
    for i in l:
        total += i
        print(total)
        
numbers = []
while True:
    number = int(input("Enter a number (0 to end): "))
    if number == 0:
        break
    elif number < 0 or number > 999:
        print("Number is out of range.")
    else:
        numbers.append(number)
print("Original list:\n{}".format(numbers))
print("Accumulative Sum:")
accum_sum(numbers)
"""
"""
3
def find_sd(l):
    sum_x = 0
    aver = sum(l) / len(l)
    for i in l:
        sum_x += (i-aver)**2
    return (sum_x / (len(l)-1))**0.5

scores = []
while True:
    score = float(input("Enter score: "))
    if score == -1:
        if scores:
            print("Maximum score is {:.2f}.".format( max(scores) ))
            print("Minimum score is {:.2f}.".format( min(scores) ))
            print("Average score is {:.2f}.".format( sum(scores) / len(scores) ))
            print("Standard deviation is {:.2f}.".format( find_sd(scores) ))
        break
    elif score > 100 or score < 0:
        print("Score is out of range.")
    else:
        scores.append(score)
"""
"""
6
def remove_duplicates(t):
    new_list = []
    for i in t:
        if i not in new_list:
            new_list.append(i)
    return new_list

t = [2, 2, 2, 2, 1, 1, 2, 1, 1, 3, 3, 3]
remove_duplicates(t)
"""
"""
5
sort_original = []
while True:
    number = int(input())
    
    if number == -1:        
        sort_process = []
        divi = 0
        for i in sort_original:
            if i > divi:
                divi = i
                sort_process.append(divi)
        print(sort_process)
        break
    
    sort_original.append(number)
"""

"""
4
def find_mode(l):
    check = []
    c_count = []    
    for cc in range(11):
        c_count.append(l.count(cc))
        
    for j in range(len(l)):
        if l.count(j) >= max(c_count):
            check.append(j)
            
    for k in range(len(check)):
        print(check[k])

scores = []
for i in range(20):
    score = int(input("Enter score: "))
    if score > 10 or score < 0:
        print("Score is out of range.")
    else:
        scores.append(score)
        
print(f"-----\nOriginal list:\n{scores}\nMode of scores:")
find_mode(scores)
"""