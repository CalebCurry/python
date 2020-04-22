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

#As an alternative, we can import one specific thing from the module

from random import randint, seed
print("from random import randit:", randint(5,5)) #always 5 lol

#This replaces anything locally called randint:
randint = "SUPER IMPORTANT DATA DON'T DELETE!!!!"
from random import randint

print("RIP data:", randint)


########## Alias an import ##########


import random as r

print("r.randint:", r.randint(6,6))

#This can be used to preserve data locally:

randint = "SUPER IMPORTANT DATA DON'T DELETE!!!!"
from random import randint as ri

print("ri:", ri(7,7))
print("NOT LOST!", randint)

########## import * ##########

#We now we can bring one specific item from a module using 
from random import randint
#This puts it directly in our symbol table replacing anything called randint
#You will see sometimes importing everything, even though it's not recommended
#100% guarentee 30% of the time to yeet out something important:

seed = "watermelon"
from random import *

print("Today we are going to plant", seed, "seeds! Yay!") #Not what we wanted. 

#We can get a better picture of this by printing the output of dir()
#which shows the identifiers in scope

a, b, c, e, f, g = 0, 0, 0, 0, 0, 0 #find these:
print(dir())

########## Creating a Module ##########


#We can easily create our own module by just creating a python file
#Any variables or functions will be imported
#See utils.py
import utils
print("Range (high-low):", utils.stats_range([5, 3, 5, 1, 10]))


########## sys path ##########


#When we created the utils module, it came from the same directory.
#This is part of the default search path
#You can see the places modules are searched for by importing a special module
#https://docs.python.org/3/tutorial/modules.html#standard-modules

import sys 

#always available, work directly with interpreter
#unlike some other modules. 
#import winreg doesn't work for me (im on mac...maybe on windows)
#docs give this example:
sys.ps1 = 'C> ' #(Try it in interactive mode if needed)

print(sys.path)

#path prints locations searched for modules. 

#We could move utils up a directory (or anywhere we want)
#and import it like so:
sys.path.append("/Users/calebcurry/Python")

#There are ways you can do this more dynamically
#https://stackoverflow.com/questions/30218802/get-parent-of-current-directory-from-python-script/39618108
from os.path import dirname, abspath
d = dirname(dirname(abspath(__file__)))
sys.path.append(d)