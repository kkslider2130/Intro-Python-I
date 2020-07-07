"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import getpass
import os
import platform
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
for a in sys.argv:
    print(a)

# Print out the OS platform you're using:
# YOUR CODE HERE

print(platform.platform())
# Print out the version of Python you're using:
# YOUR CODE HERE

print('current python version: ' + sys.version)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
print('processing id: ' + str(os.getpid()))

# Print the current working directory (cwd):
# YOUR CODE HERE
print('current dir: ' + os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE


print('login: ' + getpass.getuser())
