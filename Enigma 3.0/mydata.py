"""
"mydata.py" module for Enigma 3.0 will do -
 - Generates the 6 special keys to be used in encryption
 - To be used as core database and to be used at many places for data
 - It has data like special keys, lists of characters used in keys/decryption token and
 list of values of every key
"""

#Importing modules
import random
import string

#Making vars of characters
letters = string.ascii_letters
punctuation_for_list = string.punctuation
digits = string.digits

#Making lists, to be used for dicts and decryption token
var_for_keys = list(letters + punctuation_for_list + digits + " ")
var_for_values = list(letters + punctuation_for_list + digits + " ")
random.shuffle(var_for_values) # Shuffling the values
# Here I have added spaces coz they aren't in those chars

# Making some function that will return all six special keys to be used in encryption
# Func. For keys
def key1():
    """Generating a special key which will be used as key1"""
    random.shuffle(var_for_values)
    var_for_key1 = dict(zip(var_for_keys, var_for_values))
    return var_for_key1


def key2():
    """Generating a special key which will be used as key2"""
    random.shuffle(var_for_values)
    var_for_key2 = dict(zip(var_for_keys, var_for_values))
    return var_for_key2

def key3():
    """Generating a special key which will be used as key3"""
    random.shuffle(var_for_values)
    var_for_key3 = dict(zip(var_for_keys, var_for_values))
    return var_for_key3

def key4():
    """Generating a special key which will be used as key4"""
    random.shuffle(var_for_values)
    var_for_key4 = dict(zip(var_for_keys, var_for_values))
    return var_for_key4

def key5():
    """Generating a special key which will be used as key5"""
    random.shuffle(var_for_values)
    var_for_key5 = dict(zip(var_for_keys, var_for_values))
    return var_for_key5

def key6():
    """Generating a special key which will be used as key6"""
    random.shuffle(var_for_values)
    var_for_key6 = dict(zip(var_for_keys, var_for_values))
    return var_for_key6
