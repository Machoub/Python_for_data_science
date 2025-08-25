import sys
from ft_filter import ft_filter


def main(argv):
    """
        Take a sys.argv input and output each word of sys.argv[1] that contains
        more characters then sys.argv[2]
    """
    try:
        assert len(argv) == 3 and argv[2].isdigit(), " the arguments are bad"
        text = argv[1]
        n = int(argv[2])
        assert isinstance(text, str) and isinstance(n, int), " the arguments\
            are bad"
        textlist = list(ft_filter(lambda word: len(word) > n, text.split()))
        print(textlist)
    except AssertionError as msg:
        print(f'AssertionError: {msg}')
    except ValueError as error:
        print("ValueError:", error)
    except Exception as msg:
        print(f"Error: {msg}")


if __name__ == "__main__":
    main(sys.argv)
