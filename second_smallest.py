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
def second_smallest(a):
    if len(a) < 2:
        print("None")
    # 1st pass we find minimum value by using min function.
    min1 = min(a)
    # 2nd pass: find 2nd smallest value
    min2 = float('inf')
    for num in a:
        if num<min2 and num!= min1:
            min2 = num
    print(min2 if min2 != float('inf') else None)
a = [12,13,4,2,1,7,5,6,9]
second_smallest(a)