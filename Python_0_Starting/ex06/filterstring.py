import sys
from ft_filter import ft_filter

def main(argv):
    try:
        assert len(argv) == 3, " the arguments are bad"
        text = argv[1]
        n = int(argv[2])
        assert isinstance(text, str) and isinstance(n, int), " the arguments are bad"
        textlist = list(ft_filter(lambda word: len(word) > n , text.split()))
        print(textlist)
    except AssertionError as msg:
        print(f'AssertionError: {msg}')
    except ValueError as error:
        print("ValueError:", error)


if __name__ == "__main__":
    main(sys.argv)