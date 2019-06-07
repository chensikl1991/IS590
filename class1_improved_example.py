"""
IS590PR session 1

Example 2 "improved from example 1"

A simple program with user input and type conversions.
This is primarily a demonstration to show exception handling and
looping until a condition is met.

Pay attention to the indenting of lines, it's critical for
Python to work properly. """

while True:
    try:
        a = float(input('give me the first number.'))
        b = float(input('give me the second number.'))
        print('the sum is', a + b)
    except ValueError:
        # ValueError is the exact exception type thrown when the input
        # can't be converted into a floating point number.
        print('enter only valid numbers.\n')
    x = input('enter a Q to quit.')
    if x in ['q', 'Q', 'quit', 'Quit', 'QUIT']:
        break


#  Discussion:  What are some other things we can do to further improve the code above?

