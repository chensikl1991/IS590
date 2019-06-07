"""
From 590PR, session 1

These are miscellaneous code fragments illustrating some common features of Python
and some of its unusual aspects.

This is not an example of well-formed program coding as a whole.
"""

# looping and counting in Python.
# Each of these next 3 loops will output integers from 0 to 9:

# the "traditional" kind of loop you'll see in many languages:
i = 0
while i < 10:
    # adding the end parameter to print here with no newline in it keeps the output
    #  all on one line:
    print(i, end=' ')
    i += 1
print()

# A variation as an infinite loop with a conditional break in the middle that
# will exit the loop.

# Use this loop style when you don't know ahead of time how many times
# a loop must iterate:
i = 0
while True:
    print(i, end=' ')
    if i >= 9:
        break
    i += 1
print('\nfinished.')


# the most "Pythonic" way to loop with integer counters:

for i in range(10):
    print(i, end=' ')
print()


# The range() function is extremely common, so memorize how it works.

# It has up to 3 parameters, START, STOP, and STEP.
# Remember the range never includes the STOP value but quits iterating
# JUST BEFORE it reaches it.

# count forward by even numbers 2 - 10:
for i in range(2, 12, 2):
    print(i)

print()


# count backward by tens:
for i in range(100, 0, -10):
    print(i)

# range() actually returns a special "range" data type (object), which is
# a type of iterator.  So if you print it directly, you don't get what you
# expect at all.
print(range(10), '\n')

# You can force it to generate the whole range of values it will produce
# by converting it to a list first:
print(list(range(10)))


# Python has unlimited integer size

def factorial(n):
    f = 1  # initialize at 1
    for x in range(1, n + 1):
        f *= x  # Notice the augmented assignment operator. Not all languages have these.
    return f


print('5! = ', factorial(5))

# Demonstrate the function we just defined:
for i in range(1, 1001):
    print('{:4}! = {}'.format(i, factorial(i)))

"""
What would happen in C, C++, Java, C#, or most other
languages if we tried calculating this?   

Answer:  An "overflow error" would occur.
"""
print('1000! = ', factorial(1000))



# Fortunately, range() parameters work just like the indexing and slicing operations
# with square brackets on any sequence data type (strings, lists, tuples, and many more).

s = 'the quick brown fox'
print(s)

# Because strings are "iterable sequences", we can even loop through its characters,
# like this:

for a in s:
    print('Character:', a)

# we can extract part(s) of a string with indexing:

print(s[0:3])  # chars 0-2
print(s[4:9])

"""
A handy feature to get parts at or near the end...
(like the last 3 characters, 'fox')
by using negative index as the start, and a colon to indicate continuing
to the end: """

print(s[-3:])

"""
Mutable vs Immutable data types

Strings, integers, floats, and several other built in data types are 'immutable'.
This means we can't change an item or part of the value without replacing the
whole value.

For example, we CAN'T do this to replace the fox with dog in string s:

s[-3:] = 'dog'

So to replace 'fox' with 'dog' we have to create a brand new string and then
assign that to the same variable.  It will disconnect variable s from the
previous value. """

# this way uses one of the built-in string methods:
s = s.replace('fox','dog')
print(s)

# this way uses string concatenation to construct a NEW string without 'fox', plus 'dog'
if s[-3:] == 'fox':
    s = s[0:-3] + 'dog'
print(s)


# Python has no "case" or "switch" keywords like you would find in
#  C, Java, or many other languages.  To do something similar, just
#  create a series of if ... elif ... elif ... else like this:

w = input('\ngive me a word or phrase: ')
if 'x' in w:
    print('x!')
elif 'y' in w:
    print('y!')
elif 'a' in w:
    print('a!')
elif 'p' in w:
    print('p!')
elif 'r' in w:
    print('r!')
else:
    print("I didn't find any of the expected letters.")

print('\n\n')


"""
Here's an interesting "under-the-hood" question:
If we have a VERY large range(), will it be fast or slow to test membership?

For example...  """

if 34534503452 in range(918, 10000000000000000000000000000, 2):
    print('Yes!')
else:
    print('No!')




"""
But if I try to do the same thing with a list containing the exact same
data, the computer will crash after exhausting memory, and not determine the
answer at all.  The example below is commented because it would crash even 
though it's legal and logically valid."""

if 34534503452 in list(range(250000, 100000000000000000000, 2)):
    print('Yes!')
else:
    print('No!')



"""
For comparison, in C, C++, or Java we might construct a typical counting loop with a for loop like this:

/* A C function that loops:  */
int main() {
    int i;

    for (i = 0; i < 10; i++) {
        printf("%d\n", i);
    }
}

/* A Java class with a main function that loops: */
class demo
{
    public static void main(String args[])
    {

        for (int i = 0; i < 10; i++)
        {
            System.out.println(i);     # like print(), in Java
        }
    }
}
"""
