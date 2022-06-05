"""
File: boggle.py
Name:Jan Guo
----------------------------------------
This program create a Boggle Game recursively finds all the words
from the 4*4 boggle board that user input letters for each row.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
file_lst = []     # A list stores the words in the FILE
boggle = []       # boggle board
words_found = []  # A list stores the word combination existed in the FILE


def main():
	"""
	This programs requires user to input four rows of letters, and it will find the word combination existed
	in the dictionary, the word consist of at least four characters.
	"""
	read_dictionary()
	for x in range(4):
		letter = input(f"{x + 1} row of letters: ")
		# Case-insensitive
		letter = letter.lower()
		if len(letter) != 7:
			print('Illegal input')
			break
		for ch in range(len(letter)):
			if ch % 2 == 1 and letter[ch] != " ":
				print('Illegal input')
				break
			if ch % 2 == 0 and not letter[ch].isalpha():
				print('Illegal input')
				break
		row_of_letter = letter.strip().split(' ')
		boggle.append(row_of_letter)
	find_words()


def find_words():
	"""
	This function goes over the boggle board and let each letter as the starter, to find out all the existed
	words combination.
	"""
	for r in range(len(boggle)):
		for c in range(len(boggle[0])):
			find_words_helper(boggle[r][c], r, c, [(r, c)])
	if len(words_found) != 0:
		print(f'There are {len(words_found)} words in total.')


def find_words_helper(word, r, c, visited):
	"""
	:param word:str, given letter used to lineup the words.
	:param r:int, the row coordinates of letter.
	:param c:int, the column coordinates of letter.
	:param visited:lst, the visited cell of current cell.
	"""
	global words_found
	# Check if words in the dictionary use the word combination found in boggle as its prefix.
	if not has_prefix(word):
		return
	# Hold not repeating words in the list and print the words found in the dictionary.
	if word in file_lst and len(word) >= 4 and word not in words_found:
		words_found.append(word)
		print(f'Found  "{word}"')
	# Check for all eight possible movements from the current cell and find next word.
	for dx in range(-1, 2, 1):
		for dy in range(-1, 2, 1):
			new_r = r + dx
			new_c = c + dy
			if (new_r, new_c) not in visited and is_in_board(new_r, new_c):
				# Choose
				visited.append((new_r, new_c))
				# Explore
				find_words_helper(word+boggle[new_r][new_c], new_r, new_c, visited)
				# Un-choose
				visited.remove((new_r, new_c))


def is_in_board(new_r, new_c):
	"""
	This function make sure the new coordinate is inside the boggle.
	:param new_r: int, the row value of new coordinate
	:param new_c: int, the column value of new coordinate
	:return: (bool) If the new coordinate is inside the boggle
	"""
	if 0 <= new_r < len(boggle) and 0 <= new_c < len(boggle[0]):
		return True
	else:
		return False


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global file_lst
	with open(FILE, 'r') as f:
		for line in f:
			dictionary_word = line.split()
			file_lst += dictionary_word


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for dictionary_word in file_lst:
		if dictionary_word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
