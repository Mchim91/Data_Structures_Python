# Start with the second item and compare it with the item before it
def insertion_sort(my_list):
    # Iterate through the list, starting from the second element (index 1).
    for i in range(1, len(my_list)):
        temp = my_list[i] # Store the current element to be inserted.
        j = i - 1 # Initialize a pointer to the previous element.

        # Compare the current element with elements in the sorted part of the list.
        # Move elements greater than 'temp' one position to the right.
        while temp < my_list[j] and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1 # Move the pointer to the left.

            
    return my_list

print(insertion_sort([4,2,6,5,1,3]))

# It's worst case scenerio is O(n^2). So it's not effecient for large input size