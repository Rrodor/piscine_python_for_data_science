import sys


def isValidString(string):
    """Check if a string does not contain any special characters"""
    for char in string:
        if not char.isalpha() and not char.isspace() and not char.isdigit():
            return False
    return True


def main():
    assert len(sys.argv) == 3 and isValidString(sys.argv[1]) \
        and sys.argv[2].isdigit(), "the arguments are bad"
    print([word for word in sys.argv[1].split()
           if len(word) > int(sys.argv[2])])


if __name__ == "__main__":
    main()
