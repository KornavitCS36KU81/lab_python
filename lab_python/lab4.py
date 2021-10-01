#x = int(input("Enter your guess (0 - 100): "))

#if x == target:
    #print("Congratulations, your guess is correct.")
    
#else:
    #if x >= 0 and x <=100:
        #print("Sorry, your guess is wrong, try again later.")
    #else:
        #print("Sorry, out of range, try again later.")
        
##BMI
#kg = float(input("Weight (kg): "))
#m = float(input("Height (m): "))

#BMI = kg / m**2
#print("BMI is {:.1f}".format(BMI))
#if BMI < 18.5:
    #print('Underweight')
#elif BMI >= 18.5 and BMI < 25:
    #print('Normal weight')
#elif BMI >= 25 and BMI < 30:
    #print('Overweight')
#else:
    #print('Obesity')
    
#บริษัท ACME
#x = float(input("Enter buying amount: "))

#if x < 1000:
    #pass
#elif x >= 1000 and x < 3000:
    #b = x * 10 / 100
    #x = x - b
#elif x >= 3000:
    #b = x * 15 / 100
    #x = x - b
    
#print("Amount due after discount is {:.2f} baht.".format(x))

#stamp
#x = float(input('Total Price: '))
#print("You got: {:.0f}".format(x // 50))

#Admin Account

#ADMIN_USERNAME = 'admin'
#ADMIN_PASSWORD = 'Ad31n15Tr@t012'

#username = input('Username: ')
#password = input('Password: ')

#if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
    #print('Welcome, admin.')
#else:
    #print('You are not admin.')
    
#Calculate f(x)

#import math
#x = float(input("Enter x : "))

#if x < 0:
    #y = math.sqrt(x**2 + 1)
#elif x == 0:
    #y = x
#elif x > 0 and x <= 99:
    #y = 3*x**2 - ((1-x)**2)
#elif x > 99:
    #y = 2*x**3 - (x/math.sqrt(x+1))
#y = math.ceil(y)
#print("f({:.2f}) = {:.0f}".format(x,y))

#ค่าจอดรถ

#import math
##input
#h = int(input("Enter number of hours: "))
#m = int(input("Enter number of minutes: "))

#if h < 0 or m < 0 or m >= 60: #รับค่าผิด
    #print("Input Error!")
#else:
    #raw = math.ceil(m / 60) # จับนาทีที่มาเป็น รอบ ทําให้ได้ 1
    #price = 10 # ประกาศค่า
    
    #if h == 0 and m <= 15:# จอดรถเเค่ 15 นาทีหรือน้อยกว่านั้น
        #print('No charge, thanks.')
    #elif h == 0 and m <= 60:# มากกว่า 15 นาทีจากเงิน 10 บาท
        #print('Total amount due is {} Bahts.'.format(price))
    #elif h >= 1 and h <= 2 and m == 0:# อยู่ในช่วง 1-2 ชั่งโมง
        #print('Total amount due is {} Bahts.'.format(price))
    #elif h >= 1 and h <= 2 and m > 0:#  อยู่ในช่วง 1-2 ชั่งโมงเเต่มี นาทีเกินมานิดหน่อย ก็ปัดขึ้น
        #print('Total amount due is {} Bahts.'.format(price * 2))
        
    #else: # มากกว่า 2 ชั่งโมง
        #if h > 2 and h >= 3 and m == 0:# อยู่ในช่วง 2-3 ชั่งโมง 
            #print('Total amount due is {} Bahts.'.format(price + (h - 2)*10))
        #elif h > 2 and h >= 3 and m > 0:# อยู่ในช่วง 2-3 ชั่งโมง เเละ มีจํานวนนาทีมากกว่านั้น
            #print('Total amount due is {} Bahts.'.format(price + ((h - 2) + raw)*10))
        #else:# ไม่เข้าเงื่อนไขอันไหนเลย
            #print('No charge, thanks.')