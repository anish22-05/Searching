'''Find the maximum difference between two elements: Given an array a[] of integers, find out the difference between any two elements 
such that the larger element appears after the smaller number in a[].'''
# This code is just finding max difference that i can get from this array with O(n^2) time complexity.
# def max_diff(a):
#     max = 0
#     for i in range(len(a)):
#         for j in range(i,len(a)):
#             if a[i] - a[j] > max:
#                 max = a[i]- a[j]
#     return max
# a = [2,3,10,6,4,8,1]
# print(max_diff(a))
'''This new approach uses O(n) time complexity.
1.For each number in the array (starting from the second element), 
we calculate the difference between the current number and the minimum value seen so far.
2.If this difference is greater than our current max_diff, we update max_diff.
3.We also update min_value if the current number is smaller, 
ensuring that we always consider the smallest number that comes before the current element.
'''
# def max_diff(a):
#     if len(a) < 2:
#         return 0 # or raise an exception if that's preferable
#     # Initialize the mini element seen so far and the max
#     min_value = a[0]
#     max_diff = a[1] - a[0]
#     # Traverse the array starting from the second element.
#     for num in a[1:]:
#         # Calculate the difference with the minimum value so far.
#         diff = num - min_value
#         if diff > max_diff:
#             max_diff = diff
#         # Update the minimum value if the current number is smaller.
#         if num < min_value:
#             min_value = num
#     return max_diff
# a = [2,3,10,6,4,8,1]
# print(max_diff(a))
