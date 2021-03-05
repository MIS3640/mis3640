"""
Write a program that reads a word list from a file and prints all the sets of words that are anagrams. Here is an example of what the output might look like:
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']
    ['generating', 'greatening']
    ['resmelts', 'smelters', 'termless']

    Hint: you might want to build a dictionary that maps from a collection of letters to a list of words that can be spelled with those letters.
            How to represent the collection of letters in a way that can be used as a key?

Modify the program to prints the longest list of anagrams first, followed by the second longest, and so on.
"""

"""
Pseudo-code:

1. Read the file, the save the words into a list, and return it.

2. sort every word, convert the string to a sorted string/tuple:
'deltas' -> 'adelst'/('a', 'd', 'e', 'l', 's', 't')

3. Create a dictionary, key is the sorted string/tuple, value is a list of words that have the same sorted string/tuple.
{
    'adelst': ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'],
    'adein': ['aiden'],
    ... 
}

4. Get anagrams by getting the values only - we only want those lists that conatins more than one item. Return a list of lists, each sublist is anagrams.
[ 
    ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'], 
    ['generating', 'greatening'],
    ['resmelts', 'smelters', 'termless'],
     ...
    ]

5. print the lists from step 4

To solve the second question: Modify the program to prints the longest list of anagrams first, followed by the second longest, and so on.

6. create a dictionary like this:
{
    6: [['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled']],
    3: [['resmelts', 'smelters', 'termless']],
    2: [['retainers', 'ternaries'], ['generating', 'greatening']] 
}
7. print....

"""


def file_to_list():
    """Return a list of words"""


def sort_word(word):
    """Return a new sorted string, or a sorted tuple"""


def list_to_dict(word_list):
    """
    return  a dictionary, key is the sorted string/tuple, value is a list of words that have the same sorted string/tuple.
    {
        'adelst': ['deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'],
        'adein': ['aiden'],
        ...
    }

    we may need to use sort_word function
    """


def get_anagrams(word_dict):
    """return list of lists"""


def print_anagrams(list_of_anagrams):
    """"""
