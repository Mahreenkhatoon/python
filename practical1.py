# WAP to demonstrate operations on String in Python

s= "  Python is a pure object oriented programming language.  "
s2="Programming"

print("Original String:", s)

# 1. Length of string
print("Length:", len(s))

# 2.Reverse the string
print("Reversed:", s2[::-1])

# 3. Trimming - remove spaces from both sides
print("Trimmed String:", s.strip())

# 4. Left trimming
print("Left Trim:", s.lstrip())

# 5. Right trimming
print("Right Trim:", s.rstrip())

# Store trimmed string
s = s.strip()


# 6. String slicing
print("First 5 characters:", s[1:5])
print("Last 8 characters:", s[-9:-1])
print("Every 2nd Character:", s[::2])

# 7. Concatenation
s1 = "Hello"
s2 = "World"
print("Concatenation:", s1 + " " + s2)
# joining string with separator
print("-".join(s2))

# 8. Repetition
print("Repetition:", s1 * 3)


