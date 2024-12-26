# WRITE HAS_UNIQUE_CHARS FUNCTION HERE #
#                                      #
#                                      #
#                                      #
#                                      #
########################################
def has_unique_chars(string):
    chars_set = set()
    for s in string:
        if s in chars_set:
            return False
        chars_set.add(s)
    return True



print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    True
    True
    False

"""