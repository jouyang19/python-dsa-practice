# HT: Set
# Implement the set_item method for the HashTable class that inserts a key-value pair into the hash table.

# The method should perform the following tasks:

# Calculate the hash value of the given key by calling the private __hash method (to be implemented separately) and store the result in a variable named index.

# Check if the data_map list at the calculated index is None:

# If it is, create an empty list at that index in data_map.

# Append the key-value pair as a list containing two elements [key, value] to the list at the calculated index in data_map.

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  
    
    ## WRITE SET_ITEM METHOD HERE ##
    #                              #
    #                              #
    #                              #
    #                              #
    ################################

# To implement this, you can first compute the hash value of the key using the __hash function.

# Then, you can check if the index in the data_map list corresponding to the hash value is None.

# If it is, you can initialize it as an empty list.

# Finally, you can append the key-value pair to the list at the appropriate index in the data_map.
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  [['bolts', 1400], ['washers', 50]]
    5 :  None
    6 :  [['lumber', 70]]

"""