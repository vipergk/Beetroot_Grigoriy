"""Task 1 Imports practice
Make a directory with 2 modules;
make a function in one of them;
then import this function in the other
module and use that in your script of choice."""
from mod1.mod1_world import  print_hello_world
"""imports function "print_hello_world'from directory 'mod1' """

def function1():
    print_hello_world()

function1()




