import sys
import string


def main(argv):
    """
    Take a user input or a sys.argv input and count characters,
    upper, lower, ponctuation marks, spaces and digits.
    """
    try:
        assert len(argv) <= 2, (
            "Too many arguments. Usage: python3 <script.py> <'string'>"
        )
        if len(argv) == 1 or not argv[1]:
            print("What is the text to count?")
            message = sys.stdin.readline()
        else:
            message = argv[1]
        print("You entered: " + message.rstrip("\n"))
    except AssertionError as msg:
        print(f'AssertionError: {msg}')
        sys.exit(1)
    except (EOFError, KeyboardInterrupt):
        print("No data provided to input function")
        sys.exit(1)
    except ValueError:
        print("Invalid input")
        sys.exit(1)
    except Exception as msg:
        print(f"Error: {msg}")
        sys.exit(1)
    upper = 0
    lower = 0
    punc_marks = string.punctuation
    punc = 0
    ws = 0
    digits = 0
    print(f'The text contains {len(message)} characters:')
    for i in message:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            ws += 1
        elif i.isdigit():
            digits += 1
        elif i in punc_marks:
            punc += 1
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{punc} punctuation marks')
    print(f'{ws} spaces')
    print(f'{digits} digits')


if __name__ == "__main__":
    main(sys.argv)
