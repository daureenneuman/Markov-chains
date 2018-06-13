"""Generate Markov text from text files."""
import random
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path)
    file = file.read()

    return file


def make_chains(text_string, n):

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    
    chains = {}
   
    text_string_list = text_string.split()


    # Make a tuple of two adjecnt words
    for i in range(len(text_string_list)-n):
        chain_key = []
        for num in range(n):
            chain_key= text_string_list[i:i+n]
            key_tuple = tuple(chain_key)
            #print(key_tuple)
            value = text_string_list[i+n]
            #print(value)
        if key_tuple in chains:
            chains[key_tuple].append(value)
        else:
            chains[key_tuple] = [value]

    print(chains)

def make_text(chains):
    """Return text from chains."""
    keys_list = list(chains.keys())
    
    key = random.choice(keys_list)
    words = list(key)
    value = random.choice(chains[key])
    words.append(value)
    key = (key[1], value)
    while True:

        if  key in chains:
            word = random.choice(chains[key])
            words.append(word)
            key = (key[1], word)
        else:
            break
    print(" ".join(words))
   


#
# Open the file and turn it into one long string
#input_text = open_and_read_file(input_path)

input_file = sys.argv[1]
file_txt = open_and_read_file(input_file)
# Get a Markov chain
chains = make_chains(file_txt,3)

# Produce random text
random_text = make_text(chains)






 # # Make a tuple of two adjecnt words
 #    for i in range(len(text_string_list)-2):
 #        chain_key = (text_string_list[i], text_string_list[i+1])
 #        value = text_string_list[i+2]
 #        if chain_key in chains:
 #            chains[chain_key].append(value)
 #        else:
 #            chains[chain_key] = [value]

 #    return chains