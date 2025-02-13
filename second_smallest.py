'''The brute force method to find the second smallest element
in an array involver comparing each element with every 
other element in the array. The goal is to identify the
smallest and second elements by performing pairwise comparisions
T.C = O(n^2)'''
# def second_smallest(a):
#     n = len(a)
#     min1 , min2 = float('inf'), float('inf')
#     for i in range(n):
#         for j in range(i+1,n):
#             if a[i]<a[j]:
#                 # Update min1 and min2 
#                 if a[i] < min1:
#                     min2 = min1
#                     min1 = a[i]
#                 elif a[i] < min2 and a[i] != min1:
#                     min2 = a[i]
#             else:# THis will run if above if stmt is false.
#                 # Update min1 and min2 
#                 if a[j]<min1:
#                     min2 = min1
#                     min1 = a[j]
#                 elif a[j] < min2 and a[j] != min1:
#                     min2 = a[j]
#     return min2 if min2 != float('inf') else None
# a = [13,4,2,7,9,6]
# print(second_smallest(a))
'''Another approach, sort array 1st and then return a[1]
T.C= O(nlogn)'''
# def second_smallest(a):
#     if len(a) < 2:
#         return None
#     # sort the array
#     a.sort()
#     print(a[1])
# a = [12,13,4,2,3,7,5,9,6]
# second_smallest(a)
'''single pass approach , T.C= O(n)'''
# def second_smallest(a):
#     if len(a) < 2:
#         print('None')
#     min1 = float('inf')
#     min2 = float('inf')
#     for num in a:
#         # min is infinity so any num,
#         #  will be minimum then infinity
#         if num < min1:
#             min2 = min1
#             min1 = num
#         elif num < min2 and num!= min2:
#             min2 = num
#     print(min2 if min2 != float('inf')else None)
# a = [12,13,4,2,1,7,5,6,9]
# second_smallest(a)
"""Two-pass approach, T.C = O(n)"""
# def second_smallest(a):
#     if len(a) < 2:
#         print("None")
#     # 1st pass we find minimum value by using min function.
#     min1 = min(a)
#     # 2nd pass: find 2nd smallest value
#     min2 = float('inf')
#     for num in a:
#         if num<min2 and num!= min1:
#             min2 = num
#     print(min2 if min2 != float('inf') else None)
# a = [12,13,4,2,1,7,5,6,9]
# second_smallest(a)
'''Tournament method: Assume that the numbers are distinct and that n is a power of 2, We pair the keys and compare the pairs in rounds 
until only one round remains. If the input has eight keys, there are four comparisons in the first round, two in the second, and one in 
the last. The winner of the last round is the largest key.

'''
# def second_smallest(a):
#     if len(a) < 2:
#         return None
#     n = len(a)
#     winners = []
#     # Tournament method
#     # here we create a tournament like environmnet between 2 elements
#     # just to find smaller vlaue hence we need to increment our for loop by 2.
#     for i in range(0,n,2):
#         if i + 1 < n:
#             winners.append(min(a[i],a[i+1]))
#         else:
#             winners.append(a[i])
#     # Find smallest and second smallest
#     smallest = min(winners)
#     second_smallest = float('inf')
#     for num in a:
#         if num < second_smallest and num != smallest:
#             second_smallest = num
#     return second_smallest
# a = [12,14,11,19,9,2,17,13,16,18]
# print(second_smallest(a))
'''We can also turn the questions to finding largest value.
1. Find the largest element in array of size n.
This is brute force method with time complexity of O(n)
'''
# def largest(a):
#     n = len(a)
#     max = 0
#     for i in range(n):
#         if a[i] > max:
#             max = a[i]
#     return max
# a = [12,34,556,23,56,457,753,123,43,4,68]
# print(largest(a))
'''Find the smallest and largest in an array of size n.
this program also give time complexity of O(n), Number of comparisions are (n-1) for finding maximum element
and (n-1) are for minimum element so in all totality in worst case we will have 2(n-1) comparision.'''
# def find_smallest_largest(a):
#     max = 0
#     min = float('inf')
#     for i in range(len(a)):
#         if a[i] > max:
#             max = a[i]
#         elif a[i] < min:
#             min = a[i]
#     print("Smallest AND Largest value:",min,max)
# a = [12,34,556,23,56,457,753,123,43,4,68]
# find_smallest_largest(a)
'''Hence for any unsorted array the time complexity will remain 
O(n), but we can try to reduce number of comparisions.
are (3n/2-1).
'''
# def findmin_max(a):
#     min = a[0]
#     max = a[0]
#     for i in range(0,len(a)-1,2):
#         first = a[i]
#         second = a[i+1]
#         if first < second:
#             if first < min: min = first
#             if second > max: max = second
#         else:
#             if second < min: min = second
#             if first > max: max = first
#     print("Minimim and Maximum element:",min, max)
# a = [12,13,143,67,3,5,76,89,3,5,10,4,32,75,34]
# findmin_max(a)
"""Finding second largest element in the given input list of elements
Find largest element in the given input list of elements.
"""
def second_largest(a):
    max = 0
    max_index = None
    print(len(a))
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
            max_index = i
    max = max - a[max_index]
    del(a[max_index])
    
    # print("after deleting max value",len(a))
    for i in range(len(a)):
        if a[i] > max:
            max = a[i]
    print("This is the second largest element",max)
a = [12,13,143,76,44,58,3,7,34,78,23,12]
second_largest(a)
