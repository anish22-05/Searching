'''Finding out the element in array that is repeated majority of times.'''
# def count_majority(a):
#     n = len(a)
#     for i in range(n):
#         count = 1
#         for j in range(i, n):
#             if a[i] == a[j]:
#                 count += 1
#             if count >= n//2:
#                 print("Number of times element is repeated:",count)
#                 return a[i]
# a = [3,4,3,5,6,6,6,6]
# print("Majority repeated element is: ",count_majority(a))
'''We will try sorting the array and then traversing for majority elements
since we are looking for majority element which is repeated atleast n//2 times so we need count variable to count
its occurrences and majority varible to keep track of majority element value among all other elements.

'''
# def count_majority(a):
#     n = len(a)
#     current = a[0] # keeping var for current value.
#     count = 1 # since we are looking for similar elements of existing elemnets so the count must strt with 1.
#     majority = 0 # as it will be updated with the count value which is maximum for any element
#     majority_element = None
#     a.sort() # Here we are sorting the array now all the similar elements will be together, T.C= O(nlogn)
#     for i in range(1,n):
#         # If a[i] equal to current i.e a[0] then increase count
#         if a[i] == current:
#             count += 1
#         # This will run if adjacent element is not equal to current.
#         # here we compare majority and set its value if it is less then count
#         # also set majority_element variable.

#         else:
#             # 
#             if count > majority:
#                 majority = count
#                 majority_element = current

#             # Reset the new element
#             current = a[i]
#             count = 1
#     if count >majority:
#         majority = count
#         majority_element = current
#     if majority >= n//2:
#         print("Majority element is", majority_element,"With frequency",majority)
#     else:
#         print("No majority element is present in array.As no element is above or equal to threshold of n//2.")


# a = [3,6,2,6,6,6,5,4,6,2,6,9]
# print(len(a), len(a)//2)
# count_majority(a)
'''Boyer-Moor Majority vote algorithm used to find the majority
element (appears more than n/2 time) in an array.
This algorithm is frequently used for 
efficient pattern matching strings.
Steps:
1. Maintain a candidate for the majority element and a count
2. Traverse the array:
    . If the count is 0, set the current element as the candidate.
    . If the current element is the same as the candidate, increment the count.
    . Otherwise, decrement the count.
3. The candidate at the end may be the majority element,
but a second pass is needed to verify.
'''
# def majority_element(a):
#     candidate, count = None, 0
#     for i in a:
#         if count == 0:
#             candidate = i
#         # increase count if the current number is the candidate,
#         # otherwise decrese count.
#         count += 1 if i == candidate else -1
#     # Phase 2: Verify that the candidate is actually the majority element
#     if a.count(candidate) > len(a) // 2:
#         return candidate
#     else:
#         return None
    

# a = [3,3,4,2,3,3,3]
# majority = majority_element(a)
# if majority is not None:
#     print("Majority element is",majority)
# else:
#     print("No majority element found")

'''Steps: 1. Insert elements into a binary search tree.
2.Each node will store:
    .value(the number frim the array).
    . Count (how many times it appears).
    . Left and Right pointers (for bst structure).
3. While inserting, increment the count if the value already exists.
4. After insertion, traverse the BST to find the element with the highest frequency.
5. If an element's frequency is greater thatn n/2, it is the majority element.

    '''
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None
class BST:
    def __init__(self,value):
        self.root = None
    # Insert elements in BST and update frequency count
    def insert(self,value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root,value)
    def _insert_recursive(self,node,value):
        if value == node.value:
            node.count += 1 #increment count if value already exists
        elif value< node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left,value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right,value)
        # Find the majority element by traversing the BST.
    def find_majority(self,n):
            self.majority_element = None
            self.max_count = 0
            self._inorder_traversal(self.root,n)
            if self.max_count > n//2:
                return self.majority_element
            else:
                return "No majority element found."
    def _inorder_traversal(self,node,n):
        if node:
            self._inorder_traversal(node.left,n)
            if node.count > self.max_count:
                self.max_count = node.count
                self.majority_element = node.value
            self._inorder_traversal(node.right,n)
def majority_element_bst(a):
    n = len(a)
    bst = BST()
    # Insert elements into BST
    for num in a:
        bst.insert(num)
    return bst.find_majority(n)
# Test Case
a = [3,6,6,3,6,3,6,6]
print(majority_element_bst(a))


    
            

