import numpy as np


'''This will resize the hashtable and reinsert the old values  '''
def resize(array):
    new_array = hashing(array)
    print('resized!')
    print('new array ', new_array)
    return new_array

'''hash function that converts the string to an index '''
def name_hash_index(key, size):
    total_num = 0
    for my_char in key:
        try:
            total_num += ord(my_char)
        except ValueError:
            total_num += int(my_char)

    hash_index = total_num % size
    return hash_index

'''Enters an (key , value) pair into the hashtable '''
def hashtable_entry(pair, hashtable):
    hop = True
    loop_break = 0
    size = len(hashtable)
    key = pair[0]
    value = pair[1]
    index = name_hash_index(key,size)
    while(hop):
      if hashtable[index] == 0:
          hashtable[index] = (key,value)
          hop = False
      else:
          index = (index + 1)%size
          loop_break += 1
          if loop_break > len(hashtable) +1:  # stops infinite loop
              print("your key ", key, " has failed to be inputted")
              break
    return hashtable

''' Takes a list of pairs and puts them into a hash table '''
def hashing(pair_list):
    size = 2*len(pair_list)   # so we can have 50% load factor initially
    hashtable = np.zeros((size), dtype = object)
    for pair in pair_list:
        try:
            pair[0] # to exclude  non pairs
            hashtable = hashtable_entry(pair, hashtable)
        except TypeError:
            print('You need a key and value pair')
    return hashtable

''' enters one key,value pair at a time'''
def hashtable_update(pair, hashtable):
    filled_cells = np.count_nonzero(hashtable)
    size = len(hashtable)
    load_factor = filled_cells / size  # percentage of occupancy
    hashtable = resize(hashtable) if (load_factor >= .7 ) else  hashtable
    hashtable = hashtable_entry(pair, hashtable)

    return hashtable

''' spits out the value for a given key '''
def hashtable_lookup(key, hashtable):
    size = len(hashtable)
    hop = True
    counter = 0
    index = name_hash_index(key, size)
    while(hop):
        try:
            if hashtable[index][0] == key:
                value = hashtable[index][1]
                return value
            else:
                index = (index + 1 )% size
                counter += 1
                if counter >= size + 1:
                    print("something went wrong")
                    break

        except TypeError:  # if it encounters no pair
            index = (index + 1 )% size
            counter += 1

    return
