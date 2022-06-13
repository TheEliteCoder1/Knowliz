"""
Name: Knowliz
Description: A Word Guessing Game, Where you have to Guess a Word given 4 Hints.
Author: DaEliteCoder1
Language: Python
Type: Shell Program
"""

import os
import time
import sys
import colorama
import random
import collections
from colorama import Fore, Back
import requests
colorama.init(autoreset=True)

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
words = [word for word in response.text.splitlines() if len(word) > 2]
word = random.choice(words)
playing = True
duplicates = [(k, v) for k,v in collections.Counter(list(word)).items() if v > 1]
attempt = 1
word_num = 1
wrongs = 0
corrects = 0
asked_for_awnser = 0
if sys.platform == 'linux':
	clear = lambda: os.system('clear')
elif sys.platform == 'win32':
	clear = lambda: os.system('cls')
while playing:
	try:
		print(word)
		print(Fore.CYAN + f"Word #{word_num}\n")
		print(Fore.GREEN + f"Hint [1]: The Word is {len(word)} characters long.\n")
		if len(duplicates) > 0:
			duplicate_hint = "There are"
			for i, d in enumerate(duplicates):
				if i != len(duplicates)-1:
					duplicate_hint += f" {d[1]} {d[0]}'s,"
				else:
					if len(duplicates) != 1:
						duplicate_hint += f" and {d[1]} {d[0]}'s"
					else:
						duplicate_hint += f" {d[1]} {d[0]}'s"
			duplicate_hint += "."
		else:
			duplicate_hint = "There are no duplicate characters."
		print(Fore.GREEN + f"Hint [2]: {duplicate_hint}\n")
		print(Fore.GREEN + f"Hint [3]: The Word starts with an {word[0]}.\n")
		print(Fore.GREEN + f"Hint [4]: The Word ends with an {word[-1]}.\n")
		print(Fore.YELLOW + f"What is the Word ?\n")
		guess = input(f"Attempt {attempt}: ")
		if guess != word and guess != 'show_awnser' and guess != 'finish_game':
			attempt += 1
			wrongs += 1
			print(Fore.RED + "Incorrect ❌")
			print(Fore.RED + "Retrying...")
			time.sleep(0.5)
			clear()
		elif guess == word and guess != 'show_awsner' and guess != 'finish_game':
			word = random.choice(words)
			word_num += 1
			corrects += 1
			attempt = 0
			duplicates = [(k, v) for k,v in collections.Counter(list(word)).items() if v>1]
			print(Fore.CYAN + "Correct! ✅")
			print(Fore.CYAN + "Moving Up to Another Word...!")
			time.sleep(0.5)
			clear()
		elif guess == "show_awnser" and guess != 'finish_game':
			print(Fore.YELLOW + "How do you know know this 🤦‍♂️ ?")
			print(Fore.GREEN + Back.WHITE + word)
			print(Fore.RED + "...")
			word = random.choice(words)
			word_num += 1
			asked_for_awnser += 1
			attempt = 0
			duplicates = [(k, v) for k,v in collections.Counter(list(word)).items() if v>1]
			time.sleep(2)
			clear()
		elif guess == 'finish_game':
			clear()
			try:
				score = (corrects / (wrongs + corrects)) * 100
				if score < 50:
					print(Fore.WHITE + Back.RED + f"Score: {corrects} / {corrects + wrongs}")
					print(Fore.WHITE + Back.RED + f"You did very poor with only {round(score, 2)}% correct 😭")
				if score >= 50 and score <= 60:
					print(Fore.WHITE + Back.YELLOW + f"Score: {corrects} / {corrects + wrongs}")
					print(Fore.WHITE + Back.YELLOW + f"You passed by with a mere {round(score, 2)}% correct 😢")
				if score > 60 and score < 70:
					print(Fore.WHITE + Back.MAGENTA + f"Score: {corrects} / {corrects + wrongs}")
					print(Fore.WHITE + Back.MAGENTA + f"You almost nailed it with {round(score, 2)}% correct 🥺")
				if score >= 70 and score < 80:
					print(Fore.WHITE + Back.GREEN + f"Score: {corrects} / {corrects + wrongs}")
					print(Fore.WHITE + Back.GREEN + f"You proved your sanity with {round(score, 2)}% correct 😀")
				if score >= 80 and score <= 90:
					print(Fore.GREEN + Back.WHITE + f"Score: {corrects} / {corrects + wrongs}")
					print(Fore.GREEN + Back.WHITE + f"I am truly Impressed...because...you...got...{round(score, 2)}% correct 😀!")
				if score >= 90 and score <= 100:
					print(Fore.MAGENTA + Back.WHITE + f"Score: {corrects} / {corrects + wrongs}")
					print(Fore.MAGENTA + Back.WHITE + f"All Hail Supreme Nerd....I am left speechless by your {round(score, 2)}% correct 🤴!")
				if asked_for_awnser > 0:
					print(Fore.CYAN + f"Although I have seen your score, you have not known a word for" + Fore.RED + f" {asked_for_awnser} times.")
					print("🤦‍♂️")
				playing = False
			except ZeroDivisionError:
				clear()
				print(Fore.RED + "Too early to see results and end game.")
	except KeyboardInterrupt:
		clear()
		print(Fore.MAGENTA + "[Game Closed] 👍")
		playing = False
		