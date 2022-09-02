import sys

sys.stdin = open('input.txt', 'r')

s="iti is a biggest place iti one of the best places that support students after grad. iti iti itit"

#------Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.

# l= ["a", "e", "i", "o", "u"]
# count=0
# for i in s :
#     if(i in l):
#         count+=1
# print(count)
# #
#
# n= input("enter size of array: ")
# arr=[]
#
# for i in range(int(n)):
#     x=int(input())
#     arr.append(x)
#
# arr.sort()
# print(arr)
# arr.reverse()
# print(arr)
#
# for i in arr:
# #     print(i)


#-----------Write a program that prints the number of times the string 'iti' occurs in anystring
 # print(s.count("iti "))
#
# print(s.count('i'))
# print(s.index("b"))

#-----------Write a program that remove all vowels from the input word and generate a brief version of it.

# vowels=["a","o","e","u","i"]
# brief=""
# for i in s:
#     if(i not in vowels):
#         brief += i
# print(brief)


##-----------Writea program that prints the locations of "i" character  in any string you added.
# places=[]
# count=0
# for i in s:
#     if(i=="i"):
#         places.append(count)
#     count+=1
# print(places)
#

#-------Write a program that generate a multiplication table from 1 to the number passed.
# n=int(input())
# final=[]
# for i in range(1,n+1):
#     l=[]
#     for x in range(1,i+1):
#         l.append(i*x)
#     final.append(l)
#
# print(final)

#--------Write a program that build a Mario pyramid like below:
# #
# n=int(input())
# for i in range(1,n+1):
#     s=" "*(n-i)+"*"*i
#     print(s)


