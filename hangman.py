from distutils.command.build_scripts import first_line_re
import random

words = ['rope', 'food', 'review', 'disorder', 'develop', 'capture', 'not', 'seek', 'chapter' , 'mountain', 'grow', 'crucial', 'or', 'cooperation', 'stranger', 'load',
        'mrs', 'host', 'another', 'barrier', 'laboratory', 'evolution', 'parking', 'form', 'ceo', 'switch', 'bathroom', 'brick', 'absence', 'network', 'modern', 'as', 'channel',
        'refer', 'me', 'none', 'extra', 'reality', 'army', 'otherwise', 'pollution', 'often', 'experiment', 'psychologist', 'driver']

word = random.choice(words)
setWord = set(word)
guessedLetters = []
lives = 7
playerWord = str
playerLetter = str

print("""
        In this game you are going to guess either single letters or whole word.
        You only have 7 chances to guess. After that you lose.
        Every time you guess the letter that is not in selected work you lose one chance.
        Also when you will not guess the whole word you lose one chance.
""")
print(word)
print(f'Your word has {len(word)} letters')
while lives != 0:
    guess = str(input('Enter your guess: '))
    if guess == word:
        print(f'Congratulations you have guessed the word! {word}')
        break

    elif len(guess) > 1 and guess != word:
        print('Unfortunately your word is incorrect. Try again.')
        lives -= 1

    elif guess in setWord:
        print(f'You have guessed the letter - {guess} is in on the {word.index(guess) + 1} position')
        guessedLetters.insert(word.index(guess), guess)
        print(guessedLetters)

    elif guess not in setWord:
        print(f'Missed {guess} letter is not in the word. Try again')
        lives -= 1
