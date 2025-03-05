'''finding the number of trailing zeros in n!.'''
'''Naive approach using factorial computation.This approach 
computes n! using python math.factorial(), converts it to 
a string, and then counts the trailing zeros.
'''
# THIS APPROACH BRLOW HAVE TIME COMPLEXITY O(n logn).

# import math
# def trailing_zeros_naive(n):
#     # Compute factorial of n
#     fact = math.factorial(n)
#     print("using fact library",fact)
#     # This below value is factorial of n = 100
#     '''43816214685929638952175999932299156089414639761565182862536979208
#     27223758251185210916864000000000000000000000000'''
#     # Convert above factorial value to string.
#     fact_str = str(fact)
#     # rev = reversed(fact_str)
#     # print("Reversed factorial string", rev)
#     # Count trailing zeros by iterating from the end
#     count = 0 
#     for char in reversed(fact_str):
#         if char == '0':
#             count += 1
#         else:
#             break
#     return count
# n = 100
# print("Naive approach for trailing zeros",n,"!", trailing_zeros_naive(n))
'''Efficient Iterative approach using division by power of 5
The number of trailing zeros in n! is determind by the number
of times 10 is factored n!. Since 10 is made from 2 and 5.
and factors of 2 are more frequent.
Sum ⌊n5⌋+⌊n25⌋+⌊n125⌋+…⌊5n​⌋+⌊25n​⌋+⌊125n​⌋+… 
until n/(5k)n/(5k) is zero.
'''
# def number_ofzeros(a):
#     count = 0
#     if a < 0:
#         return -1
#     i = 5
#     while a/i > 0:
#         count += a/i
#         i *= 5
#     return count

# print(number_ofzeros(100)) # output is 24.
'''Recursive Approach: A recursive version of the efficient
works in a similar manner, dividing n by 5 recursively.
'''
# def rec_trailing_zero(n):
#     if n < 5:
#         return 0
#     return n // 5 + rec_trailing_zero(n // 5)
# n = 10
# print(rec_trailing_zero(n)) # o/p = 2
