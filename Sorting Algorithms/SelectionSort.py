# We consider indexes
def selection_sort(my_list):
    # Iterate through the list up to the second-to-last element.
    for i in range(len(my_list)-1):
        min_index = i # Assume the current index has the minimum value.

        # Iterate through the unsorted portion of the list to find the minimum element.
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j # Update min_index if a smaller element is found.

        # Swap the current element with the minimum element found.        
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list

# Example usage of selection_sort to sort a list.
print(selection_sort([4,2,6,5,1,3]))


# It's worst case scenerio is O(n^2). So it's not effecient for large input size