'''Bitonic search is an efficient searching algorithm designed specifically for bitonic arrays,
Unique arrays with a distinctive structure of first increasing and then decreasing elements.
ALGORITHMIC PROCESS:
1. Peak Idectification: First, locate the peak elements in the bitonic array.
2. Peak represents the transition point between increasing and decreasing sequences.
3. Achieved through modified binary search technique.
SEARCH STRATEGY:
1. Ascending Seach: Binary search in increasing part
2. Decreasing Search: Binary search in decreasing part.
'''
def find_peak(a):
    """Find peak element in bitonic array Iteratively."""
    left, right = 0, len(a) -1
    while left < right:
        mid = (left + right) // 2
        if a[mid] < a[mid+1]:
            left = mid+1
        else:
            right = mid
    return left
def binary_search_ascending(a,start,end,target):
    """Iterative binary search in ascending part
    """
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            start = mid + 1
        else:
            end = mid-1
    return -1
def binary_search_descending(a,start, end,target):
    """Iterativer binary search in descending part."""
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return mid
        if a[mid] < target:
            end = mid-1
        else:
            start = mid + 1
    return -1

def bitonic_search(a,target):
    """Non Recursive bitonic Search."""
    peak = find_peak(a)
    # Search in ascending part
    left_result = binary_search_ascending(a,0,peak,target)
    # If not foung in ascending part, search descending part
    if left_result == -1:
        return binary_search_descending(a,peak+1,len(a)-1)
    
    return left_result
def main():
    # Test bitonic arrays
    test_array = [1,3,5,7,9,11,8,6,4,2]
    target = 7
    result = bitonic_search(test_array,target) 
    if result != -1:
        print(f"Target {target} found at index {result}")
    else:
        print(f"Target {target} not found in array")
if __name__ == "__main__":
    main()


"""Find peak element in array.
A peak element in an array is an element that is greater than
or equal to its neighboring elements.
DEF:An element that is larger than its adjacent elements.
Can exist at the start or end of an array
An array can have multiple peak elements.
a[i] >= a[i-1] and a[i] >= a[i+1]
There can be multiple peak elements in an array but below program will
only give us 1st peak element it will find.
"""
#---This code below gives us 1st peak element we find out.
# a = [3,4,5,7,2,1,11,8,9]
# # a = [1,3,20,33,4,1]
# left = 0
# right = len(a) -1
# print(right, len(a))
# while left < right:
#     mid = (left + right) //2
#     print("mid value", mid,a[mid])
#     if a[mid] < a[mid+1]:
#         left = mid + 1
#     else:
#         right = mid
#         print("see where is our right pointer",a[right])
# print(a[left]) # This loop returns value '7', 
# i.e 5 < 7 > 2, Hence 7 is one of the peak element and we find it before anyone.
'''Find all the peak element that are present in array.
This method we are traversing through whole array 
like linear search to find all peak elements.'''
# a = [3,4,5,7,2,1,11,8,9]

# r = len(a)-1 
# peaks = []
# if r == 1:
#     print(a[0])
# # Check if the first element is a peak
# if a[0] >= a[1]:
#     peaks.append(a[0])
# # check if the last element is a peak
# if a[r-1] >= a[r-2]:
#     peaks.append(a[r-1])
# # use while loop to check for peaks in the middle of the array
# i = 1
# while i < r:
#     if a[i] >= a[i-1] and a[i] >= a[i+1]:
#         peaks.append(a[i])
#     i += 1
# print(peaks)
"""To incorporate binary search for finding peak elements
in an array using a while loop, we need to modify our approach
Here as we know in bitonic array it 1st increase and 
then decrease. hence there is only one peak element.
But if array is not necessarily bitonic, er can adapt the 
binary search concept to fing local peaks.
The ides is to use binary search to find peaks by comparing
elements with their neighbors.
"""
# def findpeaks_binary_search(a):
#     n = len(a)
#     peaks = []
#     left, right = 0, n-1
#     # Edge case for an array with only one element
#     if n == 1:
#         print(a[0])
#     # Use while loop to perform binary search
#     while left <= right:
#         mid = (left + right)//2
#         print(mid,a[mid])
#         # check if mid is peak element or not
#         if mid == 0 or a[mid] >= a[mid-1] and mid == n-1 or a[mid]>= a[mid+1]:
#             peaks.append(a[mid])
#             # Continue searching in both left and right half
#             left = mid+1 # Move to the right
#             right = mid-1 # Move to the left
#         elif a[mid] < a[mid+1]:
#             left = mid+1
#         else:
#             right = mid-1
#     print(peaks)
# a= [3,4,5,7,2,1,11,8,9]
# findpeaks_binary_search(a)
