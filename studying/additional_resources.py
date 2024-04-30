# in and not in operator
s = 'foo'
t = 'That\'s food for thought.'

print(s in t) # prints true
print(s not in t) # prints false

# ord(c) returns an integer value for the character c
print(ord('a')) # returns the ascii value for a

# chr(n) is the reverse of ord()
print(chr(97)) # returns the character that corresponds to 97

# lens(s) returns the length of a string
s = 'cat'
print(len(s))

print(str(49.2)) # returns a string representation of an object
s = 'foobar'
print(s[0]) # prints the first character of the string
print(s[len(s) - 1]) # prints the last character
print(s[-2]) # prints the second to lalst character

# String slicing s[m:n] returns the portion of the string s
# starting with the position m and up to but not including n [m, n)
s = 'start'
print(s[1:3]) # prints ta
print(s[:3]) # prints sta   s[:n] === s[0:n]
print(s[1:]) # prints tart  s[m:] === s[m:len(s)]
print(s[-5:-1]) # prints star
# for any n, 0 <= n <= len(s)   s[:n] + s[n:] === s

s = 'longerstring'
print(s[0:7:2]) # the last index indicates the stride
# if the first and second indexes are omitted they default to the first and last character

apples_string = '12'
num_of_apples = int(apples_string) # transforms a string to an int