# Task 1

# angle1=float(input("Enter the first angle of the triangle: "))
# angle2=float(input("Enter the second angle of the triangle: "))
# angle3=float(input("Enter the third angle of the triangle: "))

# if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
#     print("The angles form a valid triangle.")
# else: print("These angles do not form a valid angle")

# Task 2

# cp=float(input("Enter the cost price: "))
# sp=float(input("Enter the selling price:"))

# if sp>cp:
#     print("Profit of:",sp-cp)
# else: print("Loss of:",cp-sp)

# Task 3



# isTrue=True

# while isTrue:
#     print("1. cm to ft")
#     print("2. km to miles")
#     print("3. USD to PKR")
#     print("4. exit")

#     option=int(input("Select option: "))

#     if option==1:
#         cm=float(input("Enter the value of cm: "))
#         ft=cm/30.48
#         print('cm',cm)
#         print("ft: ",ft)

#     elif option==2:
#         km=float(input("Enter kilometers: "))
#         mile=km/1.609344
#         print('km',km)
#         print('miles:',mile)

#     elif option==3:
#         usd=float(input("Enter USD: "))
#         pkr=usd*290
#         print('$',usd)
#         print('Rs.',pkr)
    
#     elif option==4:
#         isTrue=False
#         print("Shutting Down.....")

#     else:
#         print("Invalid choice!")

# Task 4

# n=10
# num1=0
# num2=1
# for i in range(n):
#     print(num1,end=" ")

#     next_num=num1+num2

#     num1=num2
#     num2=next_num
        
# Task 5

# n=int(input("Enter the number: "))
# product=1
# for i in range(1,n+1):
#     product*=i

# print(product)

# Task 6

# num=78962
# reversed_no=0
# while num>0:
#     last_digit=num%10

#     reversed_no=(reversed_no*10)+last_digit

#     num=num//10

# print(reversed_no)

# Task 7

# n=int(input("Enter the no: "))

# i=1
# sum=0
# while i<=n:
#     if i%5==0:
#         i+=1
#         continue
        
    
#     sum+=i
    

#     if sum > 300:
        
#         break


#     i+=1
    

# print(sum)

# Task 7

# isTrue=True
# sum=0
# count=0
# while isTrue:
#     num=int(input("Enter the num: "))
#     if num==0:
#         isTrue=False
#         break
#     else:
#         sum+=num
#         count+=1

# print("Sum: ",sum)
# print("Avg: ",sum/count)


# Task 8

# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i,end=', ')

# Task 9

# import math


# x=0
# y=0

# print("Enter the movements (e.g., 'UP 5'). Enter '!' to stop:")
# while True:
#     user_input=input()

#     if user_input =='!':
#         break

#     parts=user_input.split()
#     direction=parts[0].upper()
#     steps=int(parts[1])

#     if direction=="UP":
#         y+=steps
#     elif direction=="DOWN":
#         y-=steps
#     elif direction=="LEFT":
#         x-=steps
#     elif direction=="RIGHT":
#         x+=steps

# distance=math.sqrt((x**2+y**2))

# print(round(distance))

# Task 10

# num=int(input("Enter the number: "))

# if num<=1:
#     print("Not a prime number")
# else:

#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
    
    
#     if is_prime:
#         print("It is a prime number")
#     else: print("Not a prime number")

# Task 11

hour=int(input("Enter the hour: "))
minute=int(input("Enter the minute: "))

if hour==12:
    hour=0

minute_angle=minute*6
hour_angle=(hour*30)+(minute*0.5)

angle_difference=abs(hour_angle-minute_angle)

if angle_difference>180:
    angle_difference=360-angle_difference

print(angle_difference)

