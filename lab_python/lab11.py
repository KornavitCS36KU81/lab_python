"""
1
number = int(input())

for i in range(1,number+1):
    print("|{:^{}s}|".format("*"*(2*i-1),2*number-1))
"""

"""
2
word = input()
count = 0
for i in word:
    if i in 'aeiouAEIOU':
        count += 1
print(count)
"""
"""
3
word = input()
new_word = ''
for i in word:
    if i in 'aeiouAEIOU':
        pass
    else:
        new_word += i
print(new_word)
"""
"""
4
work = input()
count = 0
count_ch = []
while True:
    x = input()
    if x == "0":
        for i in work:
            if i in count_ch:
                count += 1        
        break
    else:
        count_ch.append(x)
    
print(count,"/",len(work),sep = "")
"""

"""
5
result = list(input())
f_result = input()

for i in result:
    if i == "[" or i == "]":
        result.remove(i)

check_result = []
for i in f_result:
    if i not in check_result:
        check_result.append(i)
        
count = 0
for i in result:
    if i in check_result:
        count += 1
        
print(count)
print("{:.2f}".format( (count * 100) / len(result) ))
"""

"""
6
#input
chracter_lu = input()
#process
new_char = ""
vowel = 'aeiou'
for i in vowel:
    x = i + 'p' + i
    chracter_lu = chracter_lu.replace(x , i)
print(chracter_lu)
"""