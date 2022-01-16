## C12 Tuples, sets and dictionaries
# Ex3 - Set List Performance Demo

import random
import time

NUMBER_OF_ELEMENTS = 10000

# Create a list
lst = list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)

# create a set from the list
s = set(lst)

# Test if an element is in the set
start_time = time.time()  # get start time
for i in range(NUMBER_OF_ELEMENTS):
    i in s
end_time = time.time()  # get the end time
run_time = ((end_time - start_time) * 1000)  # get test time
print("To test if", NUMBER_OF_ELEMENTS,
      "elements are in the set\n",
      "The runtime is", run_time, "milliseconds.")

# test if an element is on the list
start_time = time.time()
for i in range(NUMBER_OF_ELEMENTS):
    i in lst
end_time = time.time()
run_time = ((end_time - start_time) * 1000)  # get test time
print("\nTo test if", NUMBER_OF_ELEMENTS,
      "elements are in the list\n",
      "The runtime is", run_time, "milliseconds.")

# remove elements from a set one at time
start_time = time.time()
for i in range(NUMBER_OF_ELEMENTS):
    s.remove(i)
end_time = time.time()
run_time = ((end_time - start_time) * 1000)  # get test time
print("\nTo remove", NUMBER_OF_ELEMENTS,
      "elements from the set\n",
      "The runtime is", run_time, "milliseconds.")

# remove elements from a list one at time
start_time = time.time()
for i in range(NUMBER_OF_ELEMENTS):
    lst.remove(i)
end_time = time.time()
run_time = ((end_time - start_time) * 1000)  # get test time
print("\nTo remove", NUMBER_OF_ELEMENTS,
      "elements from the list\n",
      "The runtime is", run_time, "milliseconds.")

