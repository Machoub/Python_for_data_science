import sys

def is_nbr(nbr: int):
    if nbr % 2 == 0:
        return "I'm even"
    else:
        return "I'm Odd"

def main(argv):
    try: 
        assert len(argv) <= 2, " more than one argument is provided"
        if len(argv) > 1:
            assert (argv[1][0] == '-' and argv[1][1:].isdigit()) or argv[1][0].isdigit(), " argument is not an integer"
            print(is_nbr(int(argv[1])))
    except AssertionError as msg:
        print(f'AssertionError: {msg}')
        exit(1)


if __name__ == "__main__":
    main(sys.argv)
