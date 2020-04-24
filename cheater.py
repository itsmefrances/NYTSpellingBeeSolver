

def word_builder():
	letter_set = input('What are the letters to play?   ')	
	main_letter = input('What is the middle letter?   ')
	list_of_words= []
	playable_words = [] 
	set(letter_set)
	with open("words.txt") as w:
	    for word in w:
	        list_of_words.append(word.rstrip('\n'))
	
	for word in list_of_words:
		if set(word).issubset(letter_set) and len(word) >= 4 and main_letter in word:
			playable_words.append(word)
		else:
			pass
	print(f'there are {len(playable_words)} playable words, the largest word is {max(playable_words, key=len)}')
	cheat = input('would you like to see the words? y/n... ')
	if cheat.lower() == 'y':
		print(playable_words)
	else:
		print(f'alright, better not to cheat')



word_builder()