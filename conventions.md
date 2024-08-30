# Name Conventions

- Use snake_case for variable and function names.
- Separate "words" within identifiers with underscores 
- Use meaningful variable and function names
  - For example, if your program needs a variable to represent the radius of a circle, call it `radius`, not `r` and not `rad`.
  - The use of obvious, common, meaningful abbreviations is permitted. For example, `number` can be abbreviated as `num` as in `num_students`.
  - The use of single-letter variables is forbidden except in loops
  - Do not use inappropriate language or descriptions that are too verbose to name your variables.

```python
# These are all terrible variable names... What do any of these mean?
a = 1234  
b = 5.67  
c = "??"  

# This is also bad
a_string_that_has_the_text_also_bad = "also bad..."
```

- Begin variable and function names with lowercase letters
- Names of constants should be in all caps with underscores between words
  - For example, `INTEREST = 0.7` or `MAX_NUM_BOOKS = 500`
- Do not use global variables


# Use of Constants
To improve readability, you should use constants whenever you are dealing with hard-coded values. Your code shouldn't have any "magic numbers" (numbers whose meaning is unknown).

For example:
```python
 total = subtotal + (subtotal * 0.06)   
```

In the code above, 0.06 is a magic number. What is it? The number itself tells us nothing; at the very least, this code would require a comment. However, if we use a constant, the number's meaning becomes obvious, the code becomes more readable, and no comment is required.

Here’s the updated code:
```python
TAX_RATE = 0.06
total = subtotal + (subtotal * TAX_RATE)    
```

Constants are typically placed near the top of the program so that if their value ever changes they are easy to locate to modify. Constants may be placed outside of the main() function – this makes them global constants, which means everything in the file has access to them. (Global variables are only allowed for constants!)


# Comments

Programmers rely on comments to help document the project and parts of the project. Do not use inappropriate language when writing your comments, it will result in a deduction of up to 70% of your assignment score. 

Generally, we categorize comments into one of three types:

1. File Header Comments

Every file should contain a multi-line comment at the top with the requested information. This is where you must disclose all collaboration outside of course materials and office hours. For example:
```
"""
Course  : CMPSC 131, Fall 2024
Name    : Griselda Conejo Lopez
GitHub User:   gris15

Collaboration Statement: I worked on this assignment by myself, using only course materials
"""
```

2. Function Comments

One of the goals of this course is to implement good problem-solving techniques which involves thinking about the problem before you try to solve it. Each function should contain a docstring (covered in Module 2) that includes the following:

- A description of what the function does
- A description of the function's inputs
- A description of the function's outputs
These comments should be written into your source code file before you start writing any executable commands.

For example:
```
def circle_area(radius):
    """
        Calculates the area of a circle from the radius

        Input:
        radius [int | float]: circle's radius

        Output: 
        [float] the circle's area
"""
```