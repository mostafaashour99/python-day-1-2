import sys

#sys.stdin = open('input.txt' , 'r')

# def two_arg(length, start):
#     l=[]
#     for i in range(start,length+1,1):
#          l.append(i)
#     return l
# print(two_arg(5,1))
# #
#
# def div_func(num):=
#     if (num % 3 == 0 and num % 5 == 0):
#         print("FizzBuzz")
#     elif (num%3==0):
#         print('Fizz')
#     elif (num%5==0):
#         print("buzz")
# div_func(15)
#
# def reverse_inpit():
#     s=input("enter string: ")
#     return s[::-1]
#
# print(reverse_inpit())
#
#
#
# def user_input():
#     while True:
#         name=input("enter your name: ")
#         if(name!='' and not(name.isdigit())):
#             break
#     mail=input("enter your mail: ")
#     print(f"name: {name} mail {mail}")
# user_input()
#
# import re
# def mail_validator(email):
#
#     regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#     if (re.search(regex, email)):
#         print("Valid Email")
#     else:
#         print("Invalid Email")
#
# mail_validator("mostafa.ashour@gmail.com")

# def alpha_func(name):
#     count=0
#     substring=''
#     maxSub=''
#     for i in range(0 , len(name)-1 ):
#         if(name[i]<=name[i+1]):
#             count+=1
#             substring+=name[i]
#         else:
#             substring+=name[i]
#             if(count >= len(maxSub)):
#                maxSub = substring
#             count=0
#             substring=''
#     print(maxSub)
# alpha_func('abdulrahman')





# def done_func():
#     count = 0
#     total = 0
#     avg = 0
#     while True:
#         x=input("enter num: ")
#         if (x.isdigit()):
#             count+=1
#             total+=int(x)
#         elif(not (x.isdigit()) and x!="done"):
#             print("erre")
#         elif (x=="done"):
#             break
#
#     print(f"total sum {total} and number of input {count} average {total/count}")
#
# done_func()
# #
import random

def hangman():
    words=["ahmed","ali","mostafa","mai","nader"]
    gussWord=random.choice(words)
    userWord='_'*len(gussWord)
    gussCorrect=0
    gussWrong=0
    userName=input("Enter your name: ")

    while (gussWrong!=7 ) and (gussCorrect!=len(gussWord)):
        x=input("guess any alphabe: ")
        if(x in gussWord and x not in userWord):
            for i in range(len(gussWord)):
                if (gussWord[i]==x):
                    gussCorrect+=1
                    userWord=userWord[:i]+x+userWord[i+1:]
            print(userWord)
            print(gussCorrect)
        else:
            gussWrong+=1
            print("sorry your guss is wrong "+ userWord)
            print("you have "+ str(7-gussWrong) +" times to try")
    if(gussWrong==7):
        print(f"sorry {userName}")
    elif(gussCorrect==len(gussWord)):
        print("correct")

hangman()