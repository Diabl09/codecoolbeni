import sys

if len(sys.argv) >= 2:
    for arg in sys.argv[1:]:
        print("Hello " + arg + "!")
else:
    print("Hello World!")