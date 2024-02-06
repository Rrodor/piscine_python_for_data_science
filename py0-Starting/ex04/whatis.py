import sys

if len(sys.argv) == 1:
    quit()

x = 0

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"
    if (sys.argv[1][0] == '-' and sys.argv[1][1:].isnumeric()):
        x = 1
    if sys.argv[1].isnumeric():
        x = 1

    assert len(sys.argv) < 3, "more than one argument is provided"
    assert x == 1, "argument is not an integer"

    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except AssertionError as e:
    print("AssertionError: {}".format(e))
