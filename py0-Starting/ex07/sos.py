import sys


def check_arg(arg):
    """Check if the argument is valid."""
    for x in arg:
        if not x.isalnum() and not x.isspace():
            return False
    return True


def main():
    """Convert a string to morse code."""
    NESTED_MORSE = {" ": "/ ",
                    "A": ".- ",
                    "B": "-... ",
                    "C": "-.-. ",
                    "D": "-.. ",
                    "E": ". ",
                    "F": "..-. ",
                    "G": "--. ",
                    "H": ".... ",
                    "I": ".. ",
                    "J": ".--- ",
                    "K": "-.- ",
                    "L": ".-.. ",
                    "M": "-- ",
                    "N": "-. ",
                    "O": "--- ",
                    "P": ".--. ",
                    "Q": "--.- ",
                    "R": ".-. ",
                    "S": "... ",
                    "T": "- ",
                    "U": "..- ",
                    "V": "...- ",
                    "W": ".-- ",
                    "X": "-..- ",
                    "Y": "-.-- ",
                    "Z": "--.. ",
                    "0": "----- ",
                    "1": ".---- ",
                    "2": "..--- ",
                    "3": "...-- ",
                    "4": "....- ",
                    "5": "..... ",
                    "6": "-.... ",
                    "7": "--... ",
                    "8": "---.. ",
                    "9": "----. "}

    try:
        assert len(sys.argv) == 2 and check_arg(sys.argv[1]), \
            "the argument is bad"
        string = "".join([NESTED_MORSE[c] for c in sys.argv[1].upper()])
        string = string[:-1]
        print(string)
    except AssertionError as e:
        print("AssertionError: {}".format(e))


if __name__ == "__main__":
    main()
