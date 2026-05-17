# Task 1

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
        
# Task 2

# for i in range(6):
#     print('*'*i)

# for k in range(4,0,-1):
#     print('*'*k)

# Task 3

rows = 3

for i in range(1, rows + 1):
    # Inner Loop 1: Print the spaces
    for j in range(rows - i):
        print("  ", end="")
        
    # Inner Loop 2: Print the stars
    for k in range(2 * i - 1):
        print("* ", end="")
        
    # Move to the next line after completing the row
    print()

# Task 4
    
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end='')
#     print()

# Task 5
# n=int(input("Enter the number n: "))
# x=float(input("Enter the number x: "))
# sum=1
# for i in range(2,n+1):
#     sum=sum+x**i/i

# print(sum)

# Task 6
# x=int(input("Enter the number x: "))
# sum=0
# for i in range(1,8):
#     term=1/i*((x-1)/x)**i
#     sum+= term

# print(sum)

# Task 7

# n = int(input("Enter the no: of terms: "))

# total_sum = 0
# series_string = ""
# current_term = 2


# for i in range(n):
   
#     total_sum += current_term
    
#     current_term = (current_term * 10) + 2

# print("Sum of above series is:", total_sum)

# Task 8

# decimal_num=int(input("Enter the decimal number: "))
# binary_string=""

# if decimal_num==0:
#     binary_string="0"
# else:
#     while decimal_num>0:
#         remainder=decimal_num%2

#         binary_string+=str(remainder)

#         decimal_num=decimal_num//2

# print(binary_string)

# Task 9
# num1=int(input("Enter the 1st num: "))
# num2=int(input("Enter the 2nd num: "))

# a=num1
# b=num2

# while b>0:
#     remainder=a%b

#     a=b
#     b=remainder

#     hcf=a

#     lcm=(num1*num2)//hcf

# print("HCF: ",hcf)
# print("LCM",lcm)

# Task 10

# str="Data science mentorship program by campusx"
# acronym_str=""

# words=str.split()

# for word in words:
#     acronym_str+=word[0].upper()

# print(acronym_str)

# Task 11
# str1="campusx"
# str2="data"

# mid_index=len(str1)//2

# first_half=str1[:mid_index]
# second_half=str1[mid_index:]

# result=first_half+str2+second_half

# print(result)

# Task 12


# str1="PyNaTive"

# str_upper=""
# str_lower=""

# for char in str1:
#     if char.islower():
#         str_lower+=char
#     else:
#         str_upper+=char


# result=str_lower+str_upper
# print(result)

# Task 13

str1="hel12304every093"

sum=0
count=0

for char in str1:
    
    if char.isdigit():
        sum+=int(char)
        count+=1

if count>0:
        average=sum/count
else: average=0
    
print("Sum",sum)

print("Avg",average)

# Task 14

# str1 = 'I am 25 years and 10 months old'

# str_nums=""

# for char in str1:
#      if char.isdigit():
#           str_nums+=char

# print(str_nums)

# Task 15

# str1="khikhi"

# middle_index=len(str1)//2

# first_half=str1[:middle_index]
# second_half=str1[middle_index:]

# if first_half==second_half:
#      print("String is symmetrical")
# else: print("String is not symmetrical")

# Task 16

# str1=input("Enter the string: ")

# words=str1.split()

# for i in range(len(words)-1,-1,-1):
#      print(words[i], end=" ")

# Task 17

# str1="We can learn data science through campusx mentorship program"

# sentences=str1.split()

# count=0
# for word in sentences:
#      count+=1
#      if word=="learn":
#           break
     
# print("Location of word campusx is: ",count)
          

# Task 18

# for i in range(1,5):
#      for j in range(1,5):
#           for k in range(1,5):
#                for l in range(1,5):
#                     print(i,j,k,l)

# Task 19

str1=input("Enter the string")

unique_str=""

for char in str1:
     
    if char not in unique_str:
         unique_str+=char

print(unique_str)