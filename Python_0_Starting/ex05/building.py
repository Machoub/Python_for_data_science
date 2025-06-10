import sys
import string

def main(argv):
    try:
        assert len(argv) <= 2, "Too many arguments. Usage: python3 <script.py> <'string'>"
        if len(argv) == 1 or not argv[1]:
            user_input = input("Please provide a string: ")
        else:
            user_input = argv[1]
        print(f"You entered: {user_input}")
    except AssertionError as msg:
        print(f'AssertionError: {msg}')
        exit (1)

    except (EOFError, KeyboardInterrupt):
        print("No data provided to input function")
        exit(1)

    upper = 0
    lower = 0
    punc_marks = string.punctuation
    punc = 0
    ws = 0
    digits = 0
    print(f'The text contains {len(user_input)} characters:')
    for i in  user_input:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            ws += 1
        elif i.isdigit():
            digits += 1
        elif i.find(punc_marks):
            punc += 1
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{punc} punctuation marks')
    print(f'{ws} spaces')
    print(f'{digits} digits')

if __name__ == "__main__":
    main(sys.argv)