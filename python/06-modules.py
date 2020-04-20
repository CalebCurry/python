########## Intro to modules ########## 

#A module is just a fancy name for a python file
#By convention, they are often imported at the top of a file
#but you can do it anywhere
import math
import pickle
import queue
import heapq
import json
import random

print(pickle) 
#You will get a path like so (I'm on a mac)
#/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/pickle.py
#Explore this folder to see some other options.
#Or, check out this: https://docs.python.org/3/py-modindex.html

#We use the module with dot notation to access the functions or variables
#an object of type module
print(math.pi)
print(type(math))

#Here is another example
#Pseudorandom number 0-100 (inclusive)
print(random.randint(0, 100))

#You can see how this works by opening random.py 
#from random.py line 244:
#def randint(self, a, b):
#    """Return random integer in range [a, b], including both end points.
#    """
#    return self.randrange(a, b+1)


"""
This is a side note that we may get into in more detail later
When you create a file to be imported,
you can expose certain pieces as seen in random.py

line 786...
_inst = Random()
seed = _inst.seed
random = _inst.random
...
randrange = _inst.randrange

Then when we import random, we prefix with that module name:
random.randrange 

This will access .random on an instantiated Random object
Which is then exposed through __all__

"...is easier for the casual user than making them
# instantiate their own Random() instance."

As opposed to something like this:

test = random.Random()
print(test.randint(5,10))
"""


########## From module import Something ##########

#in the previous section we showed how to import something.
import random

print(type(random))
#Doing this requires us to access the module using the dot operator




########## Alias an import ##########
########## import * ##########
########## Creating a Module ##########
########## sys path ##########
########## Packages ##########

import sys

import math
print(math.pi)

#print (pi) NOPE
from math import pi
print(pi)

print(sys.path)

sys.path.append('/Users/calebcurry/Python')

import utils

print("Range:", utils.range([5, 3, 5, 1, 10]))

a, b, c, e, f, g = 0, 0, 0, 0, 0, 0

pi = 3.2
from math import pi
print(globals())
print(dir())


import json
