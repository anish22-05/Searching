'''find two elements such that there 
sum is closer to target. This means values that addup to
equal to target value.'''
# def twosum(a,target):
#     for i in range(len(a)):
#         mid = target - a[i]
#         print("value - target",mid)
#         for j in range(i+1,len(a)):
#             if a[j] == mid:
#                 print(i,j)
# a = [2,4,3,6,1,8,5]
# target = 8
# twosum(a,target)
##---Since the array is unordered, 
##---we have time complexity of O(n^2).
'''Now we can try to sort array and 
use some binary search logic to find values closer to target.'''
# def twosum(a,target):
#     idx = a.copy()
#     a.sort()
#     middle = int(len(a)/2)-1
#     i = middle
#     j = i+1
#     sm = a[i] + a[j]
#     print(a,sm,a[middle])
#     while sm != target:
#         if sm > target and i!= 0:
#             i = i-1
#         elif sum < target and j!= len(a)-1:
#             j = j + 1
#         elif sm > target and i == 0:
#             j = j-1
#         elif sm < target and j == len(a)-1:
#             i = i + 1
#         sm = a[i] + a[j]
#     print(idx)
#     print(idx.index(a[i]), idx.index(a[j]))

# a = [3,5,1,2,17,12,14,19,20]
# target = 15
# twosum(a,target)
'''To improve our run time complexity, we need a more efficient way to
check if the complement exists in the array. we use hash table as it 
reduce the look up time from O(n) to O(1) by trading space for speed.
'''
# def twosum(a,target):
#     hashtable = {value: index for index, value in enumerate(a)}
#     print(hashtable)
#     for index, value in enumerate(a):
#         result = target - value
#         hash_index = hashtable.get(result)
#         if hash_index and hash_index != index:
#             return [index, hash_index]
# a = [3,5,2,1,17,12,14,19,20]
# target = 22
# print(twosum(a,target))
'''We can also do above process in one pass while we iterate and inserting elements into the table, we also look back to check if
current elements's complement already exists in the table. If it exists, we have found a solution and return immediately.'''
def twosum(a, target):
    dic = {}
    for i in range(len(a)):
        if a[i] in dic:
            # print(dic)
            return [dic[a[i]], i]
        else:
            dic[target-a[i]] = a[i]
    
a = [3,5,2,1,17,12,14,19,20]
target = 15
print(twosum(a,target))
