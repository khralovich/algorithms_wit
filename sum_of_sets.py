"""
Given two arrays A and B (n-element and m-element) with elements that are natural numbers. The arrays are in ascending order.
Construct an algorithm to determine the number of elements belonging to AUB (sum of sets, ie. each element can occur once).
E.g. A = {1, 2, 2, 3, 3, 5, 8}, B = {1, 3, 4, 8, 9, 10}, AUB = {1, 2, 3, 4, 5, 8, 9, 10}, so the number you are looking for is 8.
"""


# Assuming A, B, M, N are given


A = [1, 2, 2, 3, 3, 5, 8]
B = [1, 3, 4, 8, 9, 10]
N = len(A)
M = len(B)


# Step 1: combine two lists

def combined_lists(list_of_lists):
    combined_index = M+N
    combined = [0] * combined_index
    k = 0
    for list in list_of_lists:
        for i in list:
            combined[k] = i
            k += 1
    return combined, k


comb_out, comb_out_len = combined_lists([A, B])

print(comb_out)

# Step 2: sort ascending using bubble sorting


def bubble_sort(list):
    i = 0
    n = comb_out_len
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if list[j] > list[j + 1]:
                # Swap the elements
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
            j += 1
        i += 1


bubble_sort(comb_out)
print(comb_out)


# Step 3: remove duplicates

k = 0

for l in comb_out:
    i = 0
    if k == 0:
        final_list = [None] * (i + 1)
        final_list[k] = comb_out[i]
        k = 1
    else:
        

