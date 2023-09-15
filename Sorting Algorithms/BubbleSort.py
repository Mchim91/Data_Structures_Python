def bubble_sort(my_list):
    # Iterate through the list in reverse order.
    for i in range(len(my_list) - 1, 0, -1):
        # Inner loop to compare and swap adjacent elements.
        for j in range(i):
            # Compare the current element with the next element.
            if my_list[j] > my_list[j + 1]:
                # Swap the elements if they are in the wrong order.
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    # Return the sorted list.
    return my_list

# Example usage of bubble_sort to sort a list.
print(bubble_sort([4,2,6,5,1,3]))

# It's worst case scenerio is O(n^2). So it's not effecient for large input size