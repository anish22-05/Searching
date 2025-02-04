'''First, the sequence as a look-and-say pattern, concluding
with 1211. This led to developing a python to determine
its next term.
The sequence you mentioned is known as the look-and-say 
sequence is generated by reading the previous term.
. "1" is read as "one 1" which becomes "11".
."11" is read as "two 1s" which becomes "21".
. "21" is read as "one 2,one1" which becomes "1211"

'''
def next_term(term):
    """Generate the next term in the look-and-say 
    sequence from the given seqence"""
    result = ""
    i = 0
    print("Tells us the length of current term.",len(term))
    while i < len(term):
        count = 1 # At least one occurrence of the current digit.
        # Count the number of times the same digit repeats consecutively.
        while i+1 < len(term) and term[i] == term[i+1]:
            count += 1
            i += 1
            print(term[i],term[i+1])
        # Append the count and the digit to the result
        result += str(count) + term[i]
        i += 1
    return result
# Starting sequence terms.
seq = ['1','11','21']
print("current sequence:")
for term in seq:
    print(term)
current_term = seq[-1]
next_seq = next_term(current_term)
print("\nThe next term in the sequence is:",next_seq)
