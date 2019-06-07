# coding: utf-8

# # Class 2 Lecture/Demo Examples

# ### Primary new topics include lists, tuples, dictionaries, intro file I/O. More on debugging & exception handling

# ## Lists
# Lists are MUTABLE.  So we CAN change or assign to one or more items within an existing list.
# Lists can contain ANY mixture of data types, including other lists.  In other words, each ITEM in a list can be any data type, nested with no limits other than memory. So they are extremely flexible.

# In[1]:

fruit = ['apple', 'orange', 'banananana']
print(fruit)
fruit[2] = 'banana'  # correct the spelling of item #2
print(fruit)


# In[2]:

fruit.append('tomato')  # this is how to add an item to the end of a list.
print(fruit)


# In[3]:

fruit.append('starfruit', 'tangerine', 'kiwi')  # But this is invalid.


# Instead, to add multiple items to a list at once, just concatenate 2 lists:

# In[4]:

fruit += ['starfruit', 'tangerine', 'kiwi']
print(fruit)


# Lists are a "sequence" data type, so we can iterate through them:

# In[5]:

for f in fruit:
    print(f, 'is a fruit')


# We can also use the slicing / striding operations like we did on strings:

# In[6]:

print(fruit[::-1])   # compute the reverse of the list


# In[7]:

print(fruit)


# In[8]:

print(fruit[::3])  # extract every 3rd item from the list


# In[9]:

print(fruit[-3:])  # get the last 3 items


# **Copying lists requires that you are careful. In many situations you'll get another symbol pointing to the same object instead of what you expected:**

# In[10]:

other_fruits = fruit   # try to copy the list
print(other_fruits)    # check its contents
fruit[4] = 'kumquat'   # replace a member of fruit
print(other_fruits)    # what just happened!?  I didn't mean to modify other_fruits!


# Let's try that code in the Online Python Visualizer to help understand what's really happening.
# http://www.pythontutor.com/visualize.html#mode=edit

# ### Shallow Copies
# So, if you really mean to make a COPY of a list instead of just another pointer to it, usually the copy() method is what you need.  However, this is still what's called a "shallow copy":

# In[11]:

other_fruits = fruit.copy()  
print(other_fruits)
fruit.remove('tomato')   # modify the fruit list
print(fruit)
print(other_fruits)


# Yes!  Notice that now 'tomato' is gone from fruit but still exists in other_fruits.  But that only works when the list is NOT nested.

# ### Shallow Copies vs Deep Copies
# In more complex data structures, where there are nested objects within the list, to get a completely independent copy of the whole list, you'd need to use the copy module's deepcopy() function to work around that.  First, let's see how a fairly simple nested list is affected by the copy() method, to understand what a "shallow copy" is:

# In[12]:

a = [1, 2, 3, ['cat', 'dog', 'horse']]
print(a)
b = a.copy()

a.append(4)  # add something to list a to see if it shows up in b
a[3][1] = 'giraffe'  # modify a part of the nested list as a test

print(a)


# In[13]:

print(b)


# Clearly, modifying the 'dog' value in a's inner list still accidentally modified that part of list b, but the 4 that was appended does not show up because that was a new top-level item in a.  This also should make more sense when viewed through the Python Visualizer.
# 
# ### Demonstrating a true deep copy

# In[14]:

from copy import deepcopy  # import this standard function so we can use it

a = [1, 2, 3, ['cat', 'dog', 'horse']]
print(a)
b = deepcopy(a)  # make a DEEP copy of a this time.

a.append(4)  # add something to list a to see if it shows up in b
a[3][1] = 'giraffe'  # modify a part of the nested list as a test

print(a)
print(b)


# ## Tuples
# Tuples are IMMUTABLE like strings.  But they are still sequences of zero or more items, so they are iterable.
# Like lists, the items in tuples can be ANY data type, including other nested tuples. 
# They are created by enclosing comma-separated items in parethenses.

# In[15]:

deciduous = ('white oak', 'black walnut', 'red maple', 'silver maple', 'cottonwood')
evergreen = ('holly', 'white pine', 'red cedar', 'blue spruce', 'hemlock')
empty_tuple = ()
one_item_tuple = (1, )   # notice the strange hanging comma here. It's REQUIRED.
two_item_tuple = (1, 2)

test = (1 + 5) * 3
print(test)
print(one_item_tuple)
print(type(test))
print(type(one_item_tuple))


# In[16]:

x = ('some string')
print(x)


# We can use indexing and slicing just as with strings and lists:

# In[17]:

print(deciduous[0:3])


# In[18]:

trees = deciduous + evergreen  # we can concatenate tuples, they retain sequence.
print(trees)

# print(type(trees))


# In[19]:

tuple(sorted(trees))  # we can use the builtin sorted() function on any iterable type.


# ## type conversion
# It is easy to convert lists to tuples and vice versa:

# In[20]:

tree_list = list(trees)
print(tree_list)


# In[21]:

fruit_tuple = tuple(fruit)
# fruit_tuple
tuple(sorted(fruit_tuple))


# ## Mutability & Immutability
# What happens when mutable objects contain immutable objects?

# In[22]:

test = [5, 3.14159, 'string', ['a', 'b', 'c'], (1, 2, 3, 4)]
print(test)
test[3][1] = 'something completely different'
print(test[4][3])


# In[23]:

# this is not valid, because it tries to modify PART of a tuple stored within the list.
test[4][3] = 8   


# Note though we can delete or replace the WHOLE tuple without violating the immutability

# In[24]:

test[4] = (1, 2, 3, 8)


# In[25]:

del test[4]


# In[26]:

print(test)


# # Dictionaries
# Dictionaries in Python are essentially the same as data types called "Hash Maps" or "Associative Arrays" in other programming languages. They actually store a set of key/value pairs.  They work like a list or array except that their indexes (called "keys") can be arbitrary values that aren't necessarily integers. Also, the indexes don't have to be consecutive in any sense, and can even vary data types. Dictionaries turn out to be very handy for many common situations in coding. They are also generally fast in most operations, and efficient in storage.
# 
# Note that the keys MUST be unique within a dictionary, and that the _standard_ dictionary type does NOT preserve the order of keys or values.

# In[27]:

favorite_foods = {'Joe': 'pizza', 'Bob': 'beer', 'Gina': 'spaghetti', 'Anita': 'salad'}
favorite_foods['Bob'] = 'steak'
for name in sorted(favorite_foods):
    print("{}'s favorite food is {}".format(name, favorite_foods[name]))


# Dictionaries are mutable, so we can definitely add and remove items (key/value pairs) to and from existing dictionaries.  Notice though that we CREATE a dictionary with curly braces, but we still use the square brackets to do indexing, even in assignments:

# In[28]:

favorite_foods['George'] = 'banana'
favorite_foods['Anita'] = 'salad'
favorite_foods['Zelda'] = 'salad'
favorite_foods['Edward'] = 'steak'
favorite_foods['Edward, Jr.'] = 'steak'

print(favorite_foods.keys())
print(favorite_foods.values())


# In[29]:

print(favorite_foods)


# ### Sometimes we might want to invert a dictionary (swap the keys and values)

# In[30]:

flipped = {}
for k in favorite_foods.keys():
    v = favorite_foods[k]
    if v not in flipped:
        flipped[v] = k
    else:
        flipped[v] += ', ' +k 

print(flipped)
for food in sorted(flipped):
    print("{}'s favorite food is {}".format(flipped[food], food))


# There is a problem with the above code though...  what is it?
# 
# If more than one VALUE is the same, it will only retain the LAST associated key in the 'flipped' dictionary.  So we need to improve the algorithm to check for duplicate values (the food name) and store multiple names with that key.
# 
# One way to do it is like this:

# In[31]:

flipped = {}
for k in favorite_foods.keys():
    v = favorite_foods[k]
    if v not in flipped.keys():
        flipped[v] = k
    elif isinstance(flipped[v], str):
        flipped[v] = [flipped[v], k]
    else:
        flipped[v].append(k)

print(flipped)


# The problem with the previous solution though is it produces an inconsistent data structure, where some values are bare strings, and others are lists of strings.  
# 
# So a better and simpler approach is to make ALL the values into lists of strings, even if there's only one name in that list:

# In[32]:

flipped = {}
for k in favorite_foods.keys():
    v = favorite_foods[k]
    if v not in flipped.keys():
        flipped[v] = [k]
    else:
        flipped[v].append(k)

print(flipped)


# In[33]:

for food in flipped:
    print(food, 'is liked best by ', end='')
    for name in flipped[food]:
        print(name, end=', ')
    print()


# In[34]:

for food in flipped:
    print(food, 'is liked best by ', end='')
    print(', '.join(flipped[food]))


# # Converting dictionaries
# Note that although we can convert from dictionaries to other data types, it's not as straightforward. Python doesn't know what we really want to do with the data structure.

# In[35]:

list(favorite_foods)  # this ends up creating a list of the keys, and ignoring the values.


# In[36]:

list(favorite_foods.values())  # this is a way to make a list of the values (ignoring the keys)


# ## File Input/Output
# Many data files we use in Python are some type of "text" files.  These include plain text, CSV (comma-separated values), TSV (tab-separated values), and even XML or HTML files.  Python works with text files by applying "character encoding" to properly interpret and format the data characters.   

# In this example, we create (output) the list of tree species into a new file, one per line:

# In[37]:

tree_list = list(trees)


# In[38]:

with open('tree_species.txt', 'w') as f:
    for tree in tree_list:
        print(tree, file=f)


# Next, we read in the textfile into a list:

# In[39]:

with open('tree_species.txt', 'r') as input_file:
    print(type(input_file))
    new_tree_list = input_file.readlines()  
    # readlines() scoops every line into a string, stored as an item in a list
print(new_tree_list)


# Notice that worked, except it included the newline characters, keeping them at the end of each item.  We don't really want that in the data.  There are many ways to remove or avoid that behavior, one way is below:

# In[40]:

with open('tree_species.txt', 'r') as input_file:
    new_tree_list = input_file.read().splitlines(keepends=False) 
    # This approach reads the whole file as one string, then splits into a list
    # of individual lines in a separate step while discarding the line endings.

print(new_tree_list)


# In the next example, we read (input) that same file into a list, sort it, and then write a new file called 'sorted_tree_species.txt'

# In[41]:

with open('tree_species.txt', 'r') as input_file:
    new_tree_list = input_file.read().splitlines(keepends=False) 

with open('sorted_tree_species.txt', 'w') as output_file:
    for tree in sorted(new_tree_list):
        print(tree, file=output_file)


# ## Incremental file reading
# The above examples used the file methods read() and readlines(), both of which normally read the ENTIRE file into memory.  But for many situations, we don't want to read the whole data stream at once, or possibly we _can't_ because some other process is simultaneously adding data to the same file or stream.  So we must also be comfortable with incremental file processing, and I expect you to do this properly in Assignment 2.
# 
# The most common ways to do this are to:
#  * Read one line at a time and process it. (This works with text files only)
#  * Read (up to) a specified number of bytes at a time.

# Simple example of generating a big text file with an unknown quantity of numbers on each line:

# In[42]:

from random import randint

num_lines = randint(100,300)  # randomize the length of the file

with open('random_numbers.txt', 'w') as f:
    for i in range(num_lines):
        nums_per_line = randint(2, 8) # Randomize how many distinct numbers we put on this line
        s = '' # initialize a blank string
        for j in range(nums_per_line):
            # Generate a new random number between 1 & 1000, inclusive:
            n = randint(1, 1000)
            s += str(n) + ' '  # convert integer to string and concatenate with a space
        print(s, file=f)


# Simple example to read that file of numbers, *one line at a time* and process it to compute the sum for each line.

# In[43]:

with open('random_numbers.txt', 'r') as f:
    # We don't necessarily know how long the file is, but we can still use a for loop:
    for line in f:   # reads ONLY ONE line from the file, and stops when hits end of file.
        values_on_line = line.split()  # Split string at spaces into list of "words" which are number strings.
        line_total = 0  # initialize to zero
        
        for value in values_on_line:
            # check if it's convertible to an integer as expected:
            try:
                n = int(value)
            except ValueError:
                print('WARNING: ignoring invalid non-integer value found:', value)
                n = 0 
            line_total += n  # accumulate the line total
        print(line_total)  # output the line total


# ## Exception Handling / error-checking
# That code above worked properly, but it could be more robust. In other words, it doesn't have complete error-checking. For example, what if the file doesn't exist or can't be opened?  We'll look at that in PyCharm...
# 

# ## Debugging
# Debugging is arguably either limited or complicated in Jupyter Notebooks, depending on your point of view. Let's have a look at the stepping debugger tools in PyCharm...
