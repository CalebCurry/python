age = 25
print(age)

#this is a comment

age1 = 1
age_2 = 2
#invalid name -> age-3 = 3
#invalid name -> 4age = 4
Age = 6 #not recommended
age_of_user = 7 #recommend underscores for multiple words based on this guide:
#https://www.python.org/dev/peps/pep-0008/#function-and-variable-names

#return = 5 --> Cannot assign to keywords
#https://docs.python.org/3/reference/lexical_analysis.html#keywords

########## OPERATORS ##########
result = 20 / 3 #6.6666....
print(result) 

print("Here is a floor version (crop decimal):", 20 // 3) #6

result = 5**2 #raising a number to a power (5^)
print(result)

#You can use round instead. 
print(round(20/3), 0)

print(result / age) #can use variables in place of literals. This will not change variable values

#guess the output:
print(20 / 3 + 1)

#think of it like this because of operator precedence:
print((20 / 3) + 1)

#You can, however, force certain operations to happen first with ()
print(20 / (3 + 1))

######### MODULUS AND POWER ############

#5 * 5 * 5 * 5* 5
print(5**5)

#The remainder of 78 / 11 is 1.
print(78 % 11)

Notes:

It can be 16 bits or 32 bits depending on the platform.

Changed in version 3.9: array('u') now uses wchar_t as C type instead of deprecated Py_UNICODE. This change doesn’t affect its behavior because Py_UNICODE is alias of wchar_t since Python 3.3.

Deprecated since version 3.3, will be removed in version 4.0.

The actual representation of values is determined by the machine architecture (strictly speaking, by the C implementation). The actual size can be accessed through the itemsize attribute.

The module defines the following type:

class array.array(typecode[, initializer])
A new array whose items are restricted by typecode, and initialized from the optional initializer value, which must be a list, a bytes-like object, or iterable over elements of the appropriate type.

If given a list or string, the initializer is passed to the new array’s fromlist(), frombytes(), or fromunicode() method (see below) to add initial items to the array. Otherwise, the iterable initializer is passed to the extend() method.

Raises an auditing event array.__new__ with arguments typecode, initializer.

array.typecodes
A string with all available type codes.

Array objects support the ordinary sequence operations of indexing, slicing, concatenation, and multiplication. When using slice assignment, the assigned value must be an array object with the same type code; in all other cases, TypeError is raised. Array objects also implement the buffer interface, and may be used wherever bytes-like objects are supported.

The following data items and methods are also supported:

array.typecode
The typecode character used to create the array.

array.itemsize
The length in bytes of one array item in the internal representation.

array.append(x)
Append a new item with value x to the end of the array.

array.buffer_info()
Return a tuple (address, length) giving the current memory address and the length in elements of the buffer used to hold array’s contents. The size of the memory buffer in bytes can be computed as array.buffer_info()[1] * array.itemsize. This is occasionally useful when working with low-level (and inherently unsafe) I/O interfaces that require memory addresses, such as certain ioctl() operations. The returned numbers are valid as long as the array exists and no length-changing operations are applied to it.

Note When using array objects from code written in C or C++ (the only way to effectively make use of this information), it makes more sense to use the buffer interface supported by array objects. This method is maintained for backward compatibility and should be avoided in new code. The buffer interface is documented in Buffer Protocol.
array.byteswap()
“Byteswap” all items of the array. This is only supported for values which are 1, 2, 4, or 8 bytes in size; for other types of values, RuntimeError is raised. It is useful when reading data from a file written on a machine with a different byte order.

array.count(x)
Return the number of occurrences of x in the array.

array.extend(iterable)
Append items from iterable to the end of the array. If iterable is another array, it must have exactly the same type code; if not, TypeError will be raised. If iterable is not an array, it must be iterable and its elements must be the right type to be appended to the array.

array.frombytes(s)
Appends items from the string, interpreting the string as an array of machine values (as if it had been read from a file using the fromfile() method).

New in version 3.2: fromstring() is renamed to frombytes() for clarity.

array.fromfile(f, n)
Read n items (as machine values) from the file object f and append them to the end of the array. If less than n items are available, EOFError is raised, but the items that were available are still inserted into the array.

array.fromlist(list)
Append items from the list. This is equivalent to for x in list: a.append(x) except that if there is a type error, the array is unchanged.

array.fromunicode(s)
Extends this array with data from the given unicode string. The array must be a type 'u' array; otherwise a ValueError is raised. Use array.frombytes(unicodestring.encode(enc)) to append Unicode data to an array of some other type.

array.index(x[, start[, stop]])
Return the smallest i such that i is the index of the first occurrence of x in the array. The optional arguments start and stop can be specified to search for x within a subsection of the array. Raise ValueError if x is not found.

Changed in version 3.10: Added optional start and stop parameters.

array.insert(i, x)
Insert a new item with value x in the array before position i. Negative values are treated as being relative to the end of the array.

array.pop([i])
Removes the item with the index i from the array and returns it. The optional argument defaults to -1, so that by default the last item is removed and returned.

array.remove(x)
Remove the first occurrence of x from the array.

array.reverse()
Reverse the order of the items in the array.

array.tobytes()
Convert the array to an array of machine values and return the bytes representation (the same sequence of bytes that would be written to a file by the tofile() method.)

New in version 3.2: tostring() is renamed to tobytes() for clarity.

array.tofile(f)
Write all items (as machine values) to the file object f.

array.tolist()
Convert the array to an ordinary list with the same items.

array.tounicode()
Convert the array to a unicode string. The array must be a type 'u' array; otherwise a ValueError is raised. Use array.tobytes().decode(enc) to obtain a unicode string from an array of some other type.

When an array object is printed or converted to a string, it is represented as array(typecode, initializer). The initializer is omitted if the array is empty, otherwise it is a string if the typecode is 'u', otherwise it is a list of numbers. The string is guaranteed to be able to be converted back to an array with the same type and value using eval(), so long as the array class has been imported using from array import array. Examples:

array('l')
array('u', 'hello \u2641')
array('l', [1, 2, 3, 4, 5])
array('d', [1.0, 2.0, 3.14])
See also
Module struct
Packing and unpacking of heterogeneous binary data.

Module xdrlib
Packing and unpacking of External Data Representation (XDR) data as used in some remote procedure call systems.

NumPy
The NumPy package defines another array type.






