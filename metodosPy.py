##Global Functions:

len(s): Returns the number of items in an object.
range(start, stop, step): Generates a sequence of numbers.
sorted(iterable, key=None, reverse=False): Returns a new sorted list from the elements of any iterable.
enumerate(iterable, start=0): Returns an enumerate object, adding a counter to an iterable.
zip(*iterables): Makes an iterator that aggregates elements from each of the iterables.

##String Methods:

trip(): Removes whitespace at the beginning and end of a string.
split(separator, maxsplit): Splits a string into a list using the separator (if provided); maxsplit defines the maximum number of splits.
join(iterable): Joins the elements of an iterable (like a list) into a single string, separated by the string on which join is called.
find(substring, start, end): Returns the lowest index in the string where substring is found.
replace(old, new, count): Replaces occurrences of the old string with the new string; count defines the maximum number of replacements.
upper(): Converts a string to uppercase.
lower(): Converts a string to lowercase.

##Mathematical Functions:

abs(x): Returns the absolute value of x.
round(number, ndigits): Rounds a number to a given precision in decimal digits.
pow(x, y): Returns x raised to the power y.
sum(iterable, start): Sums start and the items of an iterable from left to right and returns the total.
min(iterable, *args, key): Returns the smallest item in an iterable or the smallest of two or more arguments.
max(iterable, *args, key): Returns the largest item in an iterable or the largest of two or more arguments.

##List Methods:

append(element): Adds an element to the end of the list.
extend(iterable): Extends the list by appending all the items from the iterable.
insert(index, element): Inserts an element at a specified index.
remove(element): Removes the first occurrence of the element.
pop(index): Removes and returns the element at the given index (or the last item if the index is not specified).
index(element, start, end): Returns the index of the first occurrence of the element.
count(element): Returns the number of occurrences of the element in the list.
sort(key=None, reverse=False): Sorts the items of the list in place.
reverse()
copy()

##Dictionary Methods:+

get(key, default): Returns the value for the specified key; returns default if the key is not found.
keys(): Returns a view object displaying a list of all the keys in the dictionary.
values(): Returns a view object displaying a list of all the values in the dictionary.
items(): Returns a view object with tuples of each key-value pair in the dictionary.
update(other): Updates the dictionary with elements from another dictionary or from an iterable of key-value pairs.
pop(key, default): Removes the element with the specified key and returns its value; returns default if the key is not found.
clear()
popitems()

##Tuple Operations:

tuple.index(value): Returns the index of the first occurrence of a value.
tuple.count(value): Returns the number of occurrences of a value.

##Set Methods:

add(element): Adds an element to the set.
remove(element): Removes a specified element from the set; raises a KeyError if the element is not found.
discard(element): Removes a specified element from the set if it is a member; does nothing if the element is not a member.
pop(): Removes and returns an arbitrary element from the set; raises a KeyError if the set is empty.
union(set): Returns a new set with elements from the set and all others.
intersection(set): Returns a new set with elements common to the set and all others.

##Conversion Methods:

int(x): Converts x to an integer.
float(x): Converts x to a floating-point number.
str(x): Converts object x to a string representation.
list(iterable): Converts an iterable to a list.
tuple(iterable): Converts an iterable to a tuple.
set(iterable): Converts an iterable to a set.
dict(sequence): Converts a sequence of (key, value) pairs to a dictionary.

##Variable and Attribute Functions:

getattr(object, name[, default]): Returns the value of the named attribute of an object.
setattr(object, name, value): Sets the value of the named attribute of an object.
delattr(object, name): Deletes the named attribute from an object.
hasattr(object, name): Returns True if the object has the named attribute.

##File Handling:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None): Opens a file and returns a corresponding file object.
file.read(size=-1): Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes).
file.write(string): Writes the string to the file, returning the number of characters written.
file.close(): Flushes and closes the file object.

##Miscellaneous:

type(object): Returns the type of an object.
isinstance(object, classinfo): Returns True if the object is an instance or subclass of classinfo.
id(object): Returns the identity of an object.
dir()
help()
  



