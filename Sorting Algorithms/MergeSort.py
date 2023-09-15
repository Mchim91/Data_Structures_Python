# The time complexity of Merge Sort in the worst-case scenario is O(n log n), where "n" is the 
# number of elements in the input list. This time complexity is consistent regardless of the 
# initial order of the elements because Merge Sort always divides the list into halves and then 
# merges them back together in a sorted manner.
# Space complexity for merge sort is O(n)
# Time complexity for merge sort is (Breaking apart is O(log n) Putting back together O(n))


# When we talk about sorting algorithms we consider
# O(n^2) and O(n log n)
# O(n log n) - It's the most effeicient for sorting multiple data's
###### Creation of Merge function
# N/B: Merge is not Merge Sort

# Helper function to merge two sorted lists.
def merge(list1, list2):
    combined = [] # Initialize an empty list to store the merged result.
    i = 0 # Initialize a pointer for list1.
    j = 0 # Initialize a pointer for list2.

    # Compare elements from both lists and add the smaller element to the combined list.
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1

    # Add any remaining elements from list1 to the combined list.
    while i < len(list1):
        combined.append(list1[i])
        i += 1

    # Add any remaining elements from list2 to the combined list.
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


print(merge([1,2,7,8], [3,4,5,6]))


# Recursive function to perform Merge Sort.
def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list # Base case: A list with a single element is already sorted.
    mid_index = int(len(my_list) / 2) # Find the middle index of the list.

    # Recursively sort the left and right halves of the list.
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    # Merge the sorted left and right halves to produce the final sorted list.
    return merge(left, right)


original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)