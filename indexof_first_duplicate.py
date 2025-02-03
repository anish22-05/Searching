"""Given sorted array a of n elements, possibly with duplicates, find the index of the first occurence of a number in O(logn).
Soln: To find the first occurence of a number we need to check for the following condition. 
Return the position if any one of the following is true.
"""
# def binarysearchfirstoccurence(a,target):
#     if a == None or len(a) == 0:
#         return -1
#     high = len(a) - 1
#     low = 0
#     lastfound = -1
#     mid =0
#     while 1:
#         if low > high: return lastfound
#         mid = (low + high) // 2
#         if a[mid] == target:
#             lastfound = mid; high = mid-1
#         if a[mid] < target: low = mid+1
#         if a[mid] > target: high = mid-1
#     return mid

# a = [5,6,9,12,15,15,21,22,34,45,57,70,84]
# target = 15
# print(binarysearchfirstoccurence(a,target))
'''Ginven a sortd array a of n elements, possobly with duplicates. Find the index of the last occurrence of a number in O(logn) time.
To find the last occurrence of a number we need to check for the following condition. Return the position if any one of the following
if true.
'''
# def binarysearchlastoccurrence(a,target):
#     if a == None or len(a) == 0:
#         return -1
#     high = len(a) -1 
#     low = 0
#     mid = 0
#     lastfound = -1
#     while 1:
#         if low > high :return lastfound
#         mid = (low+high)//2
#         if a[mid] == target:
#             lastfound = mid; low = mid + 1
#         if a[mid] < target: low = mid+1
#         if a[mid] > target: high = mid-1
#     return mid
# a = [5,6,9,12,15,21,21,34,45,57,70,84]
# target = 21
# print(binarysearchlastoccurrence(a,target))
'''Given a sorted array of n elements find the number of occurrneces
of a number.'''
# def linearsearchcount(a,data):
#     count = 0
#     for i in range(len(a)):
#         if a[i] == data:
#             count += 1
#     return count
# a = [7,3,6,3,3,6,7]
# print(linearsearchcount(a,3))
'''Improvement to above code to find number of occurences 
of repeated elements.
WE try to solve this with one binary search call and small scan.
1. Do a binary search for the data in the array. let us assume its positon k.
2. Now traverse towards left from k and count the number of 
occurrences of data. let this count be leftcount.
3. Traverse towards right and count the number of occurrences ofo data.
let this count be rightcount.
4. Total number of occurrences = leftcount + 1 + rightcount.'''
# def count_occurrences(a,target):
#     # 1: Binary search to find initial position
#     def binary_search(a,target):
#         left, right = 0, len(a)-1
#         while left <= right:
#             mid = (left + right) //2
#             if a[mid] == target:
#                 return mid
#             elif a[mid]< target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#         return -1
#     # Find initial position of target value.
#     k = binary_search(a,target)
#     # If target not found
#     if k == -1:
#         return 0
#     # 2: count left occurrences
#     leftcount = 0
#     left_index = k-1
#     while left_index >=0 and a[left_index] == target:
#         leftcount += 1
#         left_index -= 1
#     #3: count right occurrences
#     rightcount = 0
#     right_index = k+1
#     while right_index <= len(a) and a[right_index] == target:
#         rightcount += 1
#         right_index += 1
#     # 4: Total occurrences
#     total_occurrences = leftcount + 1 + rightcount
#     return total_occurrences

# a = [2,4,6,8,8,8,8,11,13]
# target = 8
# print(count_occurrences(a,target))
'''The alternate way to do this code is to find first 
occurrence of the number and the last occurence of the
respective number and then return last - first + 1.
and we will get total value of the number that is occuring 
multiple times.'''
def count_occurrences(a,target):
    def first_occurrence(a,target):
        left, right = 0, len(a)-1
        first = -1
        while left <= right:
            mid = (left+right)//2
            if a[mid] == target:
                first = mid
                right = mid - 1 # for first look at left
            elif a[mid] < target:
                left = mid + 1
            else:
                right = mid-1
        return first
    def last_occurrence(a,target):
        left, right = 0,len(a)-1
        last = -1
        while left <= right:
            mid = (left + right)//2
            if a[mid] == target:
                last = mid
                left = mid + 1 # for last look at right.
            elif a[mid] < target:
                left = mid+1
            else:
                right = mid -1
        return last
    first = first_occurrence(a,target)
    # Target not found
    if first == -1:
        return 0
    last = last_occurrence(a,target)
    # calculate total occurrences
    return last - first + 1
a = [ 2,3,5,5,5,6,8,8,10,11,11,11]
target = 11
print(count_occurrences(a,target))
            