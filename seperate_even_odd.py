'''Given an array a, write a function that segregates even and odd numbers. The functions should put all even numbers first, and then odd numbers/
Time complexity = O(n)

'''
#--------------------This program is by using 2 pointers.-----------
# def seperateevenodd(a):
#     left = 0; right = len(a) -1
#     while left < right:
#         while(a[left]%2 ==0 and left < right):
#             left += 1
#         while(a[right]%2 == 1 and left < right):
#             right -= 1
#         if left < right:
#             a[left], a[right] = a[right], a[left]
#             left += 1
#             right -=1
# a = [12,34,45,9,8,90,3,11]
# seperateevenodd(a)
# print(a)
'''Another approach to seperate even and odd numbers here we use separate arrays to store our values.'''
# def seperateeven_odduisng_extra_space(a):
#     x = []
#     for i in range(0,len(a)):
#         if a[i] % 2 == 0:
#             # print(a[i])
#             x.append(a[i])
#     for i in range(0,len(a)):
#         if a[i] %2 == 1:
#             x.append(a[i])
#     print("This is new list where even and odd values of array 'a' are separated",x)
#     # this is a list of elements which are even

# a = [12,34,45,9,8,90,3,11]
# print("Array with unordered values.",a)
# seperateeven_odduisng_extra_space(a)
"""Simmilar problems on this same logic is just trying to seprate all the 0s and 1's in array so that all the 
'0's and all the '1's are together."""
# This approach uses extra space here we count number of zeros that are in array  and then we store them onto 
# new array and after then we will add all the 1's i.e (n-c) here 'n' is array length and 'c' is number of zeros.
# def seperate(a):
#     x = []
#     c = 0
#     n = len(a)
#     for i in range(n):
#         if a[i] == 0:
#             c += 1
#     ones = n - c
#     # now we loop for adding 0's to array
#     for i in range(c+1):
#         x.append(0)
#     # for adding 1's now use another loop
#     for i in range(ones):
#         x.append(1)
#     return x

# a =[0,1,1,0,1,0,0,0,1,1,0]
# print(seperate(a))
'''The problem with our approch that there are too many loops even though time complexity is still O(n) 
as each loop runs n times, But since we are using a new list to store the elements in seperation.
Now we wuld like to try to solve this problem using inplace method which is seperating 0's and 1's in the same array 
that we have given.
We accomplish this process by using 2 pointers left, right and we increment left and decrement right by interchanging
values so that all 0's come forward and all the 1's at back.
'''
# def seperate(a):
#     left = 0; right = len(a)-1
#     while left < right:
#         while a[left] == 0 and left < right:
#             left += 1
#         while a[right] == 1 and left < right:
#             right -= 1
#         if left < right:
#             a[left], a[right] = a[right], a[left]
#             left += 1
#             right -= 1
# a = [0,1,0,1,1,0,0,0,1,0,1,1,1,0]
# seperate(a)
# print(a)
""""""

