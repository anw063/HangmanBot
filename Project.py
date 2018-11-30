from hangman import *
from dictionary import dictionary_list

bot = HangmanBot(dictionary_list)
bot.play_hangman()