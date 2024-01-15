"""
Given two arrays A and B (n-element and m-element) with elements that are natural numbers. The arrays are in ascending order.
Construct an algorithm to determine the number of elements belonging to AUB (sum of sets, ie. each element can occur once).
E.g. A = {1, 2, 2, 3, 3, 5, 8}, B = {1, 3, 4, 8, 9, 10}, AUB = {1, 2, 3, 4, 5, 8, 9, 10}, so the number you are looking for is 8.
"""

# Assuming A, B, M, N are given

A = [9, 6, 19]
B = [6, 6, 0, 2, 2, 2, 2]
N = len(A)
M = len(B)


# Step 1: combine two lists

def combined_lists(list_of_lists):
    combined_index = M+N
    combined = [None] * combined_index
    k = 0
    for list in list_of_lists:
        for i in list:
            combined[k] = i
            k += 1
    return combined, k


comb_list, comb_list_len = combined_lists([A, B])
print(comb_list)

# Step 2: sort ascending using bubble sorting


def bubble_sort(list):
    i = 0
    n = comb_list_len
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
            j += 1
        i += 1
    return list


sorted_list = bubble_sort(comb_list)
print(sorted_list)
# Step 3: remove duplicates


def remove_duplicates(list):
    k = 0
    i = 0
    temp = None

    while i < comb_list_len:
        if k == 0:
            temp = list[i]
            k = k+1
            i = i+1
        else:
            if list[i] == temp:
                i = i+1
            else:
                temp = list[i]
                k = k+1
                i = i+1
    return k


dedup_list_len = remove_duplicates(sorted_list)

print(dedup_list_len)
