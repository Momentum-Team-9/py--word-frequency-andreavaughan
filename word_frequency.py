STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


#def remove_punc(text):
    #turn list into one long string, make 
    # lowercase using .lower, and remove punc 
    # by looping through string and comparing to all_letters


def list_to_string(list):
    new_string = ""
    return new_string.join(list)


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    with open(file) as poem:
        lines = poem.readlines()
        list_to_string(lines)
        print(list_to_string(lines))


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
