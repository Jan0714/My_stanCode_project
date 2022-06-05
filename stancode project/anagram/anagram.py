"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
file_lst = []                 # A list stores the lines in an dictionary
result_lst = []               # The anagrams of input word
anagrams_found = []           # The anagrams containing in the dictionary
count = 0                     # Numbers of the anagrams containing in the dictionary


def main():
    """
    This program requires user to input the word, and it will find the anagrams of the word which exists in the dictionary.
    """
    read_dictionary()
    global anagrams_found
    global count
    print("Welcome to stanCode \"Anagram Generator\" or " + str(EXIT) + ' to quit)?')
    while True:
        word = input('Find anagrams for: ')
        if word == EXIT:
            break
        find_anagrams(word)
        print(str(count)+' '+'anagrams:'+str(anagrams_found))
        count = 0
        anagrams_found = []
        time_start = time.time()
        time_end = time.time()
        print('time cost', time_end-time_start)


def read_dictionary():
    """
    This program loads dictionary file as a list of words.
    """
    global file_lst
    with open(FILE, 'r') as f:
        for line in f:
            dictionary_word = line.split()
            file_lst += dictionary_word


def find_anagrams(s):
    """
    :param s:str, given string to find its anagrams.
    :return:lst, anagrams list found in the dictionary.
    """
    a = []  # Create the empty list to hold the index of the word
    for i in range(len(s)):
        a.append(i)
    find_anagrams_helper(s, a, [], len(a), '')


def find_anagrams_helper(s, index_lst, current_lst, ans_len, result_str):
    """
    This method use recursion to find and return the anagrams of the word which is found in the dictionary.
    """
    global count
    # Base case is the length of the word, build the anagrams according to the index list.
    if len(current_lst) == ans_len:
        # Hold not repeating anagrams in the list and print the anagrams found in the dictionary.
        if result_str in result_lst:
            pass
        else:
            result_lst.append(result_str)
            if result_str in file_lst:
                count += 1
                anagrams_found.append(result_str)
                print('Searching...')
                print('Found: '+result_str)
    else:
        if has_prefix(result_str):
            for index in index_lst:
                if index in current_lst:
                    pass
                else:
                    # Choose
                    current_lst.append(index)
                    # Explore
                    find_anagrams_helper(s, index_lst, current_lst, ans_len, result_str + s[index])
                    # Un-choose
                    current_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s:(str) A substring of the input word and its anagrams
    :return:(bool) If there is any words with prefix stored in sub_s
    """
    for dictionary_word in file_lst:
        if dictionary_word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
