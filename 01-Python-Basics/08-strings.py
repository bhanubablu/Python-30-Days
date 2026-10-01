# ==========================================
# STRINGS IN PYTHON
# ==========================================

name = "Bhanu Prakash"


# 1. STRING INDEXING
# Indexing is used to access individual characters in a string.
# Python indexing starts from 0.
#
# Example:
# P  Y  T  H  O  N
# 0  1  2  3  4  5
#
# Negative indexing starts from the end:
#  P   Y   T   H   O   N
# -6  -5  -4  -3  -2  -1

print(name[0])    # First character: B
print(name[-1])   # Last character: h


# 2. STRING SLICING
# Slicing is used to get part of a string.
#
# Syntax:
# string[start:stop]
#
# The start position is included.
# The stop position is NOT included.
#
# Example:
# word = "Python"
# word[0:3] gives "Pyt"
#
# 0 -> P  included
# 1 -> y  included
# 2 -> t  included
# 3 -> h  stop (not included)

print(name[0:5])   # Bhanu


# 3. STRING LENGTH
# len() returns the total number of characters.
# Spaces are also counted as characters.

print(len(name))


# 4. STRING METHODS
# upper() converts all letters to uppercase.
# lower() converts all letters to lowercase.
# title() converts the first letter of each word to uppercase.

print(name.upper())
print(name.lower())
print(name.title())


# 5. REPLACE
# replace() replaces one part of a string with another.

message = "I am learning Java"

print(message.replace("Java", "Python"))


# 6. F-STRINGS
# F-strings are used to insert variables directly inside a string.
# Put 'f' before the string and variables inside {}.

age = 23

print(f"My name is {name} and I am {age} years old.")