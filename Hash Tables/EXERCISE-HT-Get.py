# HT: Get
# Implement the get_item method for the HashTable class that retrieves the value associated with a given key from the hash table.

# The method should perform the following tasks:

# Calculate the hash value of the given key by calling the private __hash method and store the result in a variable named index.

# Check if the data_map list at the calculated index is not None:

# If it is not, iterate through the key-value pairs stored in the list at the calculated index in data_map:

# For each key-value pair, compare the stored key (located at position 0) with the given key.

# If a match is found, return the corresponding value (located at position 1) of the key-value pair.

# If the given key is not found in the hash table, return None.

class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
      
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash  

    def print_table(self):
        for i, val in enumerate(self.data_map): 
            print(i, ": ", val)
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
    
    ## WRITE GET_ITEM METHOD HERE ##
    #                              #
    #                              #
    #                              #
    #                              #
    ################################
    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
        
# Compute the hash value of the key using the __hash() method.

# Check if the hash value maps to a non-empty bucket in the hash table.

# If the bucket is non-empty, iterate through the items in the bucket using a loop and check if the current item's key matches the input key.

# If you find a matching key, return the corresponding value. Otherwise, return None.

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print('Bolts:', my_hash_table.get_item('bolts'))
print('Washers:', my_hash_table.get_item('washers'))
print('Lumber:', my_hash_table.get_item('lumber'))



"""
    EXPECTED OUTPUT:
    ----------------
    Bolts: 1400
    Washers: 50
    Lumber: None

"""