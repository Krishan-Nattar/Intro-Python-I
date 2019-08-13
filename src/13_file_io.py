"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

f = open('foo.txt')
text = f.read()
# print(f)
f.close()
print(text)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

f = open('bar.txt', 'w')

f.write('testing this line\n')
f.write('testing this line2\n')
f.write('testing this line3\n')
# text2 = f.read()

f.close()
f=open('bar.txt')
text2 = f.read()
f.close()
print(text2)

