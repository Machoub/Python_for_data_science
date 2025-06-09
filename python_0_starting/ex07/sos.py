import sys

def ASCII_to_morse(text):
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    morse_text = []
    for char in text:
        if char in NESTED_MORSE:
            morse_text.append(NESTED_MORSE[char])
        else:
            raise AssertionError("Unsupported character: {}".format(char))
    return ' '.join(morse_text)

def main(argv):
    try:
        assert len(argv) == 2 and len(argv[1]) > 0 and isinstance(argv[1], str), " the arguments are bad"
        print(ASCII_to_morse(argv[1].upper()))

    except AssertionError as msg:
        print(f'AssertionError: {msg}')


if __name__ == "__main__":
    main(sys.argv)