STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as poem:
        lines = poem.readlines()

        def list_to_string(x):
            new_string = ""
            return new_string.join(x)
        
        stringed_lines = list_to_string(lines).lower().replace("\n", " ")
        print(stringed_lines)

        def remove_punc(x):
            letters_and_space = "abcdefghijklmnopqrstuvwxyz "
            no_punc = ""
            for char in stringed_lines:
                if char in letters_and_space:
                    no_punc += char
            return no_punc

        no_punc = remove_punc(stringed_lines)
        print(no_punc)



if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
