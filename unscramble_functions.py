"""CSC108/A08: Fall 2021 -- Assignment 1: unscramble

This code is provided solely for the personal and private use of
students taking the CSC108/CSCA08 course at the University of
Toronto. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Michelle Craig, Anya Tafliovich.

"""

# Valid moves in the game.
SHIFT = 'S'
SWAP = 'W'
CHECK = 'C'


# We provide a full solution to this function as an example.
def is_valid_move(move: str) -> bool:
    """Return True if move is valid"""
    return move == CHECK or move == SHIFT or move == SWAP


# Your turn! Provide full solutions to the rest of the required functions.

def get_section_start(section_number: int, section_length: int) -> int:
    """Return the starting index of the section"""
    return section_length * (section_number - 1)


def get_section(word: str, section_number: int, section_length: int) -> str:
    """Return the section, given the section number and section length"""
    section_start = get_section_start(section_number, section_length)
    return word[section_start:section_start + section_length]


def is_valid_section(word: str, section_number: int,
                     section_length: int) -> bool:
    """Return True if the section number and section
    length create a valid section"""
    return (len(word) / section_length).is_integer() and \
           section_length * section_number <= len(word)


def swap(word: str, start_index: int, end_index: int) -> str:
    """Return a string where the start index is swapped with the end index"""
    return word[0:start_index] + word[end_index - 1] + \
           word[start_index + 1:end_index - 1] + \
           word[start_index] + word[end_index:]


def shift(word: str, start_index: int, end_index: int) -> str:
    """Return a string where the start index is shifted to the end index"""
    return word[0:start_index] + word[start_index + 1: end_index] + \
           word[start_index] + word[end_index:]


def check(word: str, start_index: int, end_index: int,
          correct_word: str) -> bool:
    """return True if the current game state word at start index to end index is
    equal to the correct word at start index to end index"""
    return word[start_index:end_index - 1] == \
           correct_word[start_index:end_index - 1]


def check_section(word: str, section_number: int,
                  section_length: int, correct_word: str) -> bool:
    """return True if the section of the current game state
    word is equal to the section of the correct word"""
    return get_section(word, section_number, section_length) == \
           get_section(correct_word, section_number, section_length)


def change_section(word: str, move: str,
                   section_number: int, section_length: int) -> str:
    """Return the new game state word given the type of move,
    the section number to manipulate and the section length"""
    section = get_section(word, section_number, section_length)
    section_start = get_section_start(section_number, section_length)
    if move == SWAP:
        return word[0:section_start] + swap(section, 0, len(section)) + \
               word[section_start + section_length:]
    if move == SHIFT:
        return word[0:section_start] + shift(section, 0, len(section)) + \
               word[section_start + section_length:]
    return None


def get_move_hint(word: str, section_number: int,
                  section_length: int, correct_word: str) -> str:
    """Return SHIFT or SWAP depending on an
    algorithm that determines the next move"""
    word_section = get_section(word,
                               section_number, section_length)
    correct_word_section = get_section(correct_word,
                                       section_number, section_length)
    first_shift = shift(word_section, 0, len(word_section))
    if first_shift == correct_word_section or \
            shift(first_shift, 0, len(first_shift)) == correct_word_section:
        return SHIFT
    return SWAP


if __name__ == '__main__':
    import doctest

    doctest.testmod()
