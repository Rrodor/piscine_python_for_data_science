import sys
from ft_filter import ft_filter


def isValidString(string):
    """Check if a string does not contain any special characters"""
    for char in string:
        if not char.isalpha() and not char.isspace() and not char.isdigit():
            return False
    return True


def supWordSize(word, size):
    """check if the word is longer than the size"""
    return len(word) > size


def main():
    assert len(sys.argv) == 3 and isValidString(sys.argv[1]) \
        and sys.argv[2].isdigit(), "the arguments are bad"
    sentence = sys.argv[1].split()
    print(ft_filter(lambda x: supWordSize(x, int(sys.argv[2])), sentence))


if __name__ == "__main__":
    main()
