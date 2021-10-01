
##input
#n = int(input())
#charater1 = input()
#charater2 = input()
##process
#sumofcharater = (charater1+charater2) * (n+1)
#sumcharater = '{m:.{a}s}'.format(a = n,m = sumofcharater)

##output
#print(sumcharater)

















#      รับข้อมูลเลขจำนวนเต็มตัวแรกคือระยะทางที่แก้ว กับ ขวัญเดินทางเป็นกิโลเมตร
#      ความจุของถังน้ำมันเป็นลิตรซึ่งเป็นเลขจำนวนเต็มเช่นกัน
m = int(input())
liter = int(input())
#       15 กิโลเมตรต่อน้ำมัน 1 ลิตร
#process
car = liter * 15

#kew
sumliter = int(car - (car * 0.5))
# (540 12) -> 90
kew = (m // sumliter)+1

#kwan
sumliter = int(car - (car * 0.1))
kwan = (m // sumliter)+1

#output
print(kew)
print(kwan)

#input      output
#400 10     6 3
#540 12     7 4