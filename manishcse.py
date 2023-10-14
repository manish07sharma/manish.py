# a=5
# b=3
# c=a+b
# d=a-b
# e=a*b
# f=a/b
# g=a//b
# h=a%b
# i=a**b
# print("addition of a and b is ",c)
# print("substraction of a and b is ",d)
# print("multuplication of a and b is ",e)
# print("divition of a and b is ",f)
# print("floor division of a and b is ",g)
# print("module of a and b is ",h)
# print("exponential of a and b is ",i)




# a="12"
# b="21"
 # print(int(a)+int(b))
# a="1"
# b=int(a)
# print(b)
# a=input("enter  your name :")
# print("my name is ", a)



# a=int(input("enter a no."))
# b=int(input("enter 2nd no."))
# c=a+b
# print("the sum of two no.",c)
# d=int("3")
# print(d)
# a=int(input("enter the 1st no."))
# b=int(input("enter the 2nd no."))
# print("sum of a and b is ",a+b)
# print("minus of a and b is ",a-b)
# print("mul of a and b is ",a*b)
# print("div of a and b is ",a/b)



# name = "manish"
# name1='sharma'
# # print(name ,"+" ,name1)
# # print("hello\t", name)
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])

# for character in name1 :
#     print(character)
# name="manish sharma is a good boy "
# print(name[0:6])
# print(len(name))
# for character in name :
#     print(character)
# nm="harry"
# print(nm[-4:-2])




# import time
# # manish_time = time.strftime('%H:%M:%S')
# # print(manish_time)
# manish_time =int( time.strftime('%H'))
# print(manish_time)
# manish_time = int(time.strftime('%M'))
# print(manish_time)
# manish_time = int(time.strftime('%S'))
# print(manish_time)
# if ( "4:00:00<'%H':'%M':'%S'<10:59:59" ) :
#     print("good morning sir") 
# elif ( "12:00:00<'%H':'%M':'%S'<15:59:59" ) :
#     print("good afternoon sir") 
# elif ( "16:00:00<'%H':'%M':'%S'<19:59:59" ) :
#     print("good evening sir") 
# else:
#     print("good night sir") 



# import time
# manish_time = time.strftime('%H:%M:%S')
# print(manish_time)
# manish_time_hour =int( time.strftime('%H'))
# print(manish_time_hour)
# manish_time = int(time.strftime('%M'))
# print(manish_time)
# manish_time = int(time.strftime('%S'))
# print(manish_time)
# if (4<=manish_time_hour<12) :
#     print("good morning sir") 
# elif (12<=manish_time_hour<16) :
#     print("good afternoon sir") 
# elif (16<=manish_time_hour<20) :
#     print("good evening sir") 
# elif(20<=manish_time_hour<4):
#     print("good night sir") 
    
    
    
    
# a=int(input("enter the age"))
# print("your age is ",a)
# if(0<a<18):
#     print("you are not able to drive")
# elif(18<a<40):
#     print("you are mid range person")
# else:
#     print("you are expert driver")
#     print("you are above age")



# x=int(input("enter the value of x"))
# match x:
#     case 0:
#         print("the value of x is 0")
#     case 1:
#         print("the value of x is 1")
#     case 2:
#         print("the value of x is 2")
#     case 3:
#         print("the value of x is 3")
#     case _:
#         print("given a invalid value of x , enter the value of x between 0 to 3")    



# a="manish sharma "
# for i in a:
#     print(i)
#     if (i=='a'):
#         print("a stands for acha insaan ")
#     elif(i=='r'):
#         print("r stands for ram ")
#     elif(i=='s'):
#         print("s stands for shiv")
#     elif(i=='h'):
#         print("h stands for hanuman ")
#     elif (i=='i'):
#         print("i stands for insaan")
# for i in range(5)  :  
#     print(i)
    
# for h in range(1,5)  :  
#     print(h)
    
# for j in range(1,5,2)  :  
#     print(j)   



# i = int(input("Enter the number: "))
# print(i)
# while(i<=38):
#   i = int(input("Enter the number: "))
#   print(i)
# print("Done with the loop")
# manish=10
# a="i am inside loop"
# while(manish>0):
#    print(manish)
#    manish=manish-1
# else:
#   print(a)



# list_1 = [1,2,3,4]
# print(list_1)
# print(type(list_1))
# print(list_1[0])
# print(list_1[1])
# print(list_1[2])
# print(list_1[3])
# print(len(list_1))
# list_2 = [i for i in range(21) if i%2==0]
# print(list_2)
# print(len(list_2))
# print(list_2[:])
# print(list_2[1:-1:2])
# list_3 = [i*i for i in range(10) if i%2==0]
# print(list_3)
# l=[1,2,3,23,53,223,12,12,12,24,54,11,22,21,23,22,223,33,44,55,66,110]
# print(l)
# l.append(27)
# print(l)
# print(len(l))
# l.sort()
# print(l)
# l.sort (reverse=True)
# print(l)
# l.reverse()
# print(l)
# print(l.index(223))
# print(l.count(12))
# m=l.copy()
# print(m)
# l.insert(2,2673)
# print(l)
# print(len(l))
# m =[1000,2000,3000,4000]
# l.extend(m)
# print(l)
# print(len(l))
# k=l+m
# print(k)
# print(len(k))


# letter = "hey my name is {1} and i am from {0}"
# state="rajasthan"
# name="manish"
# print(letter.format(state,name))
# print(f"hey my name is {name} and i am from {state}")
# price=49.999
# txt=f"for only {price:.2f} dollars!"
# print(f"hey my name is {{name}} and i am from {{state}}")
# print(txt)


# def square (n):
#  '''this will calculate the square of any no.'''
#  print(n**2)
# square(5)
# print(square.__doc__)



# def factorial(n):
#  if (n==0 or n==1):
#   return 1
#  else:
#   return n*factorial(n-1)
# print(factorial(5))

# def Fibonacci(n):
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return 0  
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(int(input("enter the nth element "))))
# n=int(input("enter the nth term upto which u want the fibonacci series"))

# print("manish sharma1")
# import pywhatkit
# import pywhatkit as kit
# kit.playonyt("radhe albeli sarkar")


# a=5
# b=3
# a=int(input("enter the value of a"))
# o=input("enter the operation")
# b=int(input("enter the value of b"))
# if(o=="+"):
#     print("the sum of a and b is",a+b)
# elif(o=="-"):
#     print("the difference of a and b is",a-b)
# elif(o=="*"):
#     print("the multipliation of a and b is",a*b)
# elif(o=="/"):
#     print("the division of a and b is",a/b)
# elif(o=="**"):
#     print("the exponensial of a and b is",a**b)
# elif(o=="%"):
#     print("the module of a and b is",a%b)
# elif(o=="//"):
#     print("the floor division of a and b is",a//b)
# if (a<a/b):
#     print("it is correct")
# else:
#     print("nothing happend")

# def calGreater(a ,b):
#     if (a>b):
#         print("a is greater than b")
#     elif(a==b):
#         print("a and b are equal")
#     else:
#         print("b is greater")
        
# def callesser(a ,b):
#     if (a>b):
#         print("b is lesser than a")
#     elif(a==b):
#         print("a and b are equal")
    # else:
    #     print("a is lesser")

# def calGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)

# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# calGreater(a,b)
# callesser(a,b)
# calGmean(a,b)
# c=int(input("enter the value of c"))
# d=int(input("enter the value of d"))
# calGreater(c,d)
# callesser(c,d)
# calGmean(c,d)
# a=int(input("enter the value of a"))
# if (a%2==0):
#     print("given no. is even no")
# else:
#     print("it is an odd no.")
# if(a%5==0):
#         print("hello")
# else:
#     print("bye")

# if(a<=100):
#     print("no charges required")
# elif(a<200):
#     b=a-100
#     sum1=b*5
#     print("total bill amount is",sum1)
# else:
#     c=a-200
#     sum2=c*10
#     sum3=sum2+500
#     print("total bill amount is RS",sum3)

# a=int(input("enter the value of a"))
# last_digit=a%10
# if(last_digit%3==0):
#     print("the last digit is divisible by 3")
# else:
#     print("not divisible by 3")
# a=int(input("enter the marks"))
# if(a>90):
#     print("A grade")
# elif(a>80 and a<=90):
#     print("B grade")
# elif(a>=60 and a<=80):
#     print("C grade")
# elif(a>=40 and a<60):
#     print("D grade")
# else:
#     print("fail")
# a=int(input("enter the value of a"))
# if(a>=100000):
#     fine1=(a/100)*15
#     print("total fine amount is",fine1)
# elif(a>50000 and a<=100000):
#     fine2=(a/100)*10
#     print("total fine amount is",fine2)
# elif(a<=50000):
#     fine3=(a/100)*5
#     print("total fine amount is",fine3)
# a=int(input("enter the no:"))
# if (a==0):
#         print("enter tthe vvalid number")
# else:
#     for i in range(1,120):
#        print(a,"*",i,"=",a*i)
#        if (i>=10):
#         break
# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# if (a<b):
#     while(a<=b):
#         print("the sum of a+b until a==b ",a+b)
#         a=a+1
    
# elif(b<a):
#     while(b<=a):
#         print("the sum of a+b until b==a ",b+a)
#         b=b+1
    
# else:
#     print("both no is same")
# a=int(input("enter the number :"))
# for i in a:
#     if(i=="e"):
#         break
#     print(i)
# while(a<11):
#     print(a)
#     a=a+1
# else:
#     print("the number is already above 10")    
# a=int(input("enter the number: "))    
# for i in range (a):
#     i=+1
#     # print(i)    
#     print(a)



    
# a=int(input("enter the rows for star"))
# b=int(input("enter the rows for reverse star"))
# for i in range (1,a):
#     for j in range (1,i+1):
#         print("*",end=" ")
#     print()
# for k in range (b,0,-1):
#     for l in range(0,k-1):
#         print("*",end=" ")
#     print()
# i=1
# s=0
# while(i<=10):
#     a=int((input("enter the  number")))
#     s=s+a
#     print(s)
#     i=i+1
# print("the average of 10 numbers is",s/10)
# a=int(input("enter the starting point of prime numbers"))
# b=int(input("enter the ending point of prime numbers"))
# if (a>b):
#     print("enter a valid starting point")
# else:
#    while(a<=b):
#     print("manish sharma")
#     for i in range(2,a-1):
#         if(a%i==0):
#            print(a,"is not a prrime number")
#         elif(a%i!=0):
#             print(a,"is prime number")
#     a=a+1
#     print("the prime numbers are",a)
# def calculategmean(a,b):
#     gmean=(a*b)/(a+b)
#     print(gmean)
    
# a=9
# b=7
# # gmean=(a*b)/(a+b)
# calculategmean(a,b)
# c=int(input("enter the value of c"))
# d=int(input("enter the value of d"))
# calculategmean(c,d)


# function argument
# def avg(*number):
#   print(type(number))
#   sum=0
#   for i in number:
#        sum= sum +i
#   print(sum / len(number))
# avg(5,6,7,10)

# def avg(*num):
#   print(type(num))
#   s=0
#   for i in num:
#     s=s+i
#   return 5
#   return s/len(num)
# c=avg(5,6,7,8,15,13,34,234,342,43,34,542) 
# print(c)

# def name(**name):
#     print(type(name))
#     print("hello,", name['fname'], name['mname'], name['lname'])
# name(fname="manish",lname="sharma",mname="kr.")
# marks=["manish","sharma","shar"]
# print(marks[0])
# print(marks[2])
# print(marks[1])
# print(marks[1])
# if "manish" in marks:
#     print("yes")
# print(marks[:])
# print(marks[1:])
# print(marks[:1])
# print(marks[0:len(marks)])
# print(len(marks))
# lst=[i*2 for i in range(10)]
# lst1=[i*i for i in range(10) if i%2==0]
# lst2=[i*2 for i in range(10) if i%2==0]
# print(lst)
# print(lst1)
# print(lst2)
# tup=(1,2,3)
# print(type(tup))





# import time
# time1=time.strftime('%H:%M:%S')
# print(time1)
# time1=time.strftime('%H')
# print(time1)
# time1=time.strftime('%M')
# print(time1)
# time1=time.strftime('%S')
# print(time1)
# # time1=time.strftime('%H:%M:%S')
# hour=int(time.strftime('%H'))
# # print(hour)
# if(hour>4 and hour<12):
#     print("good morning manish")
# elif(hour>12 and hour<16):
#     print("good afternoon manish")
# elif(hour>16 and hour<20):
#     print("good evening manish")
# elif(hour>20 and hour<4):
#     print("good night manish")

# for i in range(10):
#     print(f"enter the {i} number")
# s=0
# for i in range (1,11):
#     a=int(input(f"enter the {i} number"))
#     s=s+a   
# print(s/10)

# def factorial(n):
#     if(n==1 and n==0):
#         return 1
#     else:
#         return n* factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

# manish={1,2,3,5,24,55,2,1}
# print(type(manish))
# print(manish)
# mani=set()
# print(type(mani))
# for value in manish:
#     print(value)


# s1={1,2,3,4}
# s2={4,5,6,3}
# # s1.update(s2)
# print(s1)
# print("this is s1",c)
# print(s1.union(s2))
# print(s1,s2)
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)
# print("this is s1 intersection update",d)
# c=s1.symmetric_difference(s2)
# print(c)
# c=s1.difference(s2)
# print(c)


# dic ={"manish":"sharma",
#       "gargi":"arya",
#       "suman":"saran"}
# dic1={"ankit":"sharma",
#       "yash":"mishra",
#       "samayak":"jain"}
# print(dic["manish"])
# print(dic)
# print(dic.get("manish"))
# print(dic.keys())
# print(dic.values())
# for key in dic.keys():
#     print(f"the full names are {key} {dic[key]}")

# print(dic.items())
# for key,values in  dic.items():
#     print(f"the full names are {key} {values}")
# dic.update(dic1)
# dic.clear()
# print(dic)
# print(type(dic))
# def take_input(num):
#    for i in range (4):
#        s=num[i]+num[i+1]
#        if s==target:
#            return [i,i+1]
#            break
#        else:
#            print("the target is not achived")

# target=int(input("enter the number of target"))  
# print(take_input(""))

# def two_sum(nums, target):
#     num_dict = {}
    
#     for i, num in enumerate(nums):
#         complement = target - num
        
#         if complement in num_dict:
#             return [num_dict[complement], i]
        
#         num_dict[num] = i
    
#     raise ValueError("No two numbers add up to the target")
# target=int(input("enter the number of target")) 
# nums=[]
# for j in range(1,6):
#     j=(input(f"enter the value of index {j} : "))
#     j=int(j)
#     nums.append(j)
# print(nums)
# two_sum(nums,target)
# print(two_sum)
    
# def take_inp 
    #    else:
    #        print("the target is not achived")
# target=int(input("enter the number of target")) 
# nums=[]
# for j in range(1,6):
#     j=(input(f"enter the value of index {j} : "))
#     j=int(j)
#     nums.append(j)
# print(nums)
# take_input(nums,target)
# print(take_input)
# def multiplecation_table(a):
#     try:
#         a=int(a)
#         for i in range(1,11):
#             print(a ,"*",i,"=",a*i)
#     except Exception as e:
#         print("given a wrong input")
#     # finally:
# print("my code are awesome ")
       
# a=input("enter the table no :  ")
# multiplecation_table(a)
# a=input("enter the value: ")
# if(a=="quit"):
#     print("you entered a correct word")
# else:
#     raise NameError("you entered a wrong word")


# a=input("enter the sentence whose code word you want to select: ")
# if a.isalpha:
#     b=a.split(" ")
#     # print(b)
#     for i in b:
#         c=i[1:]
#         d=i[0]
#         e=c+d
#         f=[]
#         for _ in range(len(e)>0):
#             f.append(e)
#         print(e) 
#     print(f)
# marks=[1,22,33,44,55,66,77,88,98]
# for index,mark in enumerate(marks,start=2):
#     print(index,mark)


# st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))
# import random
# import string
# print(dir(random))

# print(dir(string))
# import numpy 
# x,y=map(int,input("enter thae number").split(" "))
# z=x*y
# print(z)
# import numpy as np
# x=input("enter the number!").split(',')
# # print(x)
# z=[int(i) for i in x]
# print(z)
# w=z[0]*z[1]
# print(w)
# T=int(input("enter the input"))
# i=1
# while i<=T:
#     N,M=map(int,input("enter the value of N and M").split())
#     if M>=N:
#         print(N)
#     else:
#         O=N-M
#         print(O+N)
#     i=i+1
# x= input("enter the number : ").split(",")
# z=[int(i) for i in x]
# print(type(z))
# print(x)
# x.sort()
# print(x)
# print(type(x))
# print(z)
# z.sort()
# print(z)
# print(type(z))
# list=["manish","sharma","yash","mishra","ankit","sharma","samayak","jain"]
# list.sort()
# print(list)
# a=[7, 4, 1, 2, 5, 8, 9, 6, 3, 14, 12, 15, 77, 55, 22, 99]
# a.sort(reverse=False)
# print(a)
# t = int(input())
# for i in range(t):
#     N, k = map(int, input().split())
#     A = list(map(int, input().split()))
    
#     pos = 0
#     neg = 0
#     divk = 0
    
#     w = 0
#     #Loop through all elements of the array
#     while A[w]<len(A):
#         #Count the negative elements of the array
#         if w<0:
#             neg = neg + 1
#         #Count the positive elements of the array
#         elif A[w]> 0:
#             pos = pos + 1
#         #Count if the given element is divisible by k
#         if A[w] == 0:
#             divk = divk + 1
#         w=w + 1
    
#     print(pos,neg,divk)

# a=list(map(int,input().split()))
# A = list(map(int, input().split()))
# print(A)
# pos=0
# sam=0
# les=0
# for i in A:
#     if i<0:
#         les=les+1
#     elif i>0:
#         pos=pos+1
#     elif i==0:
#         sam=sam+1
# print(les,pos,sam)
# A = list(map(int, input("input").split()))
# # i=0
# # while i<len(A):
# #     print(A[i])
# #     i=i+1
# print(type(A))
# print(A)
# t = int(input())
# for i in range(t):
# n = int(input())
# A = list(map(int,input(f"enter {n} elements").split()))
# print(A)
# n = int(input("enter the length of array u want"))  # Specify the number of elements you want to enter
# min_value = 1  # Minimum allowed value
# max_value = 10  # Maximum allowed value

# A = []

# while len(A) < n:
#     try:
#         user_input = input(f"Enter element {len(A) + 1} (between {min_value} and {max_value}): ")
#         num = int(user_input)
#         if min_value <= num <= max_value:
#             A.append(num)
#         else:
#             print(f"Please enter a number between {min_value} and {max_value}.")
#     except ValueError:
#         print("Invalid input. Please enter a valid number.")

# print("Entered elements:", A)



# t=int(input("enter the test case : "))
# for i in range (t):
#     n=int(input("enter the length of array"))
#     A=list(map(int,input(f"enter the {n} elements").split()))
#     a_zero =A.count(0)
#     positive_num=0
#     negative_num=0
#     if a_zero>0:
#         print(0)
#         continue
#     for w in A:
#         if w>0:
#             positive_num=positive_num+1
#         elif w<0:
#             negative_num=negative_num+1
#     if positive_num==n:
#         print(0)
#     elif negative_num%2!=0:
#         print(1)
#     elif negative_num%2==0:
#         print(0)
# import random
# print(random.randint(1,100))
# N=int(input("enter the total no. of avengers: "))
# P=list(map(int,input("enter the power of avengers: ").split()))
# if (len(P)>N):
#     print("you given extra numbers of power")
# else:
#     print(N)
#     print(P)
# a=input()
# print(a)
# print(type(a))
# b=a.count("1")
# print(b)
# # for i in a:
#     print(i)
# t = int(input())
# for i in range(t):
#     n = int(input())
#     final_ans = []          
    
#     while n>0:
#         final_ans.insert(0, (n%10)) 
#         print(final_ans)    
#         n = n//10           
#     print(*final_ans)
# print(type(final_ans))
# a=[1,2,3,4]
# a=1234
# print(*a)
# Define an integer number
# number = 12345
# digit_list = [int(digit) for digit in str(number)]
# print(digit_list)
# print(type(digit_list))
# class Solution:
#     def twoSum(self, nums: List[int], target: int):
#         pass
# manish: list[int]
# nums=list(map(int,input().split()))
# target=int(input())
# for i in nums:
#     j=i+1
#     while j<=len(nums):
#         if i==nums[j]:
#             print(i,j)
#             break
#         else:
#             print("no target found")
#             break
# nums=list(map(int,input().split()))
# target=int(input())
# for i in range(0,len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             x=[i,j]
# print(nums)
#             break     
# def twoSum(self, nums: list[int], target: int) -> list[int]:
#     for i in range(0,len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                x=[i,j]
#                print(x)
#                break
# twoSum
# list1=list(map(int,input().split()))
# print(list1)
# for i in range(9):
#     print(i)
# n=int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*",end="")
#     print()
# for l in range(n):
#     for k in range(n-l,0,-1):
#         print("*",end="")
#     print()
# B=list(map(int,input().split()))
# print(B)
# print(type(B))

# N=int(input())
# A=list(map(int,input().split()))
# A.sort(reverse=True)
# x=A[0]
# B=[i for i in A if i!=x]
# y=B[0]


# print(A)
# print(x)
# print(B)
# print(x+y)

# import statistics

# stocks = {
#     'info': [600,630,620],
#     'ril': [1430,1490,1567],
#     'mtl': [234,180,160]
# }

# def print_all():
#     for stock,price_list in stocks.items():
#         avg = statistics.mean(price_list)
#         print(f"{stock} ==> {price_list} ==> avg: ",round(avg,2))


# def add():
#     s = input("Enter a stock ticker to add:")
#     p = input("Enter price of this stock:")
#     p=float(p)
#     if s in stocks:
#         stocks[s].append(p)
#     else:
#         stocks[s] = [p]
#     print_all()


# def main():
#     op=input("Enter operation (print, add or amend):")
#     if op.lower() == 'print':
#         print_all()
#     elif op.lower() == 'add':
#         add()
#     else:
#         print("Unsupported operation:",op)

# if __name__ == '__main__':
#     main()
# N=int(input())
# A=list(map(int,input().split()))
# B=list(map(int,input().split()))
# A_count=0
# A_count_list=[]
# for i in range(N):
#     if A[i]>0:
#         A_count=A_count+1
#         # print(A_count)
#     else:
#         A_count=0
#         # print(A_count)
#         continue
        
#     A_count_list.append(A_count)
#     z=max(A_count_list)
# print(A_count_list)
# print(z)
T=int(input())
for _ in range(T):
    N=int(input())
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    A_count=0
    B_count=0
    A_count_list=[]
    B_count_list=[]
    for i in range(N):
        
        if A[i]>0:
            A_count=A_count+1
        else:
            A_count=0
            continue
        A_count_list.append(A_count)
    for j in range(N):  
        if B[j]>0:
            B_count=B_count+1
        else:
            B_count=0
            continue
        
        B_count_list.append(B_count)
    print(A_count_list)
    print(B_count_list)
    print(A_count)
    print(B_count)
    x=max(A_count_list)
    y=max(B_count_list)
    if x>y:
        print("om")
    elif y>x:
        print("Addy")
    else:
        print("draw")