# globals: injecting custom functions into python scripts and executing them

# our test function
def test():
    print("Hello")

# define global
globals()['test'] = test

# execute b.py which has the content "test()" which prints "Hello"
with open('b.py', 'r') as py:
    exec(py.read())
