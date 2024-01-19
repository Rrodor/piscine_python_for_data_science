import sys


def main():
    assert len(sys.argv) <= 2, "more than one argument is provided"

    if len(sys.argv) == 1:
        text = input("What is the text to count?\n")
        text += "\r"
    else:
        text = sys.argv[1]

    print("The text contains {} characters".format(len(text)))
    print("{} upper letters".format(sum(1 for c in text if c.isupper())))
    print("{} lower letters".format(sum(1 for c in text if c.islower())))
    print("{} punctuation marks\
          ".format(sum(1 for c in text if c in ".,;:!?-")))
    print("{} spaces".format(sum(1 for c in text if c in " \r")))
    print("{} digits".format(sum(1 for c in text if c.isdigit())))


if __name__ == "__main__":
    main()
