def print_items(n):
    # Start of the function that accepts 'n' as an argument.
 
    for i in range(n):  # Outer loop iterating over range 'n'.
        # 'i' takes values from 0 to 'n-1'.
 
        for j in range(n):  # Inner loop iterating over range 'n'.
            # 'j' takes values from 0 to 'n-1'.
 
            print(i,j)  # Prints the pair '(i, j)'.
            # This happens 'n' times for each 'i', 
            # printing all pairs where the first element 
            # is 'i' and the second element is any number
            # between '0' and 'n-1'.