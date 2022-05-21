import random

words = ['rope', 'food', 'review', 'disorder', 'develop', 'capture', 'not', 'seek', 'chapter' , 'mountain', 'grow', 'crucial', 'or', 'cooperation', 'stranger', 'load',
        'mrs', 'host', 'another', 'barrier', 'laboratory', 'evolution', 'parking', 'form', 'ceo', 'switch', 'bathroom', 'brick', 'absence', 'network', 'modern', 'as', 'channel',
        'refer', 'me', 'none', 'extra', 'reality', 'army', 'otherwise', 'pollution', 'often', 'experiment', 'psychologist', 'driver', 'building', 'universe', 'rocket', 'spaceship', 'economy',
        'contribution', 'accommodation', 'work', 'delivery', 'project', 'eventually', 'often', 'rarely', 'basically', 'inconvenient', 'television', 'frustration', 'gym', 'card', 'board',
        'confident']

word = random.choice(words)
setWord = set(word)
guessedLetters = []
lifePoints = 7
playerWord = str
playerLetter = str


print("""
        In this game you are going to guess either single letters or whole word.
        You only have 7 chances to guess. After that you lose the game.
        Every time you guess the letter that is not in selected work you lose one lifePoint.
        If you try to guess the whole word and miss you lose one lifePoint.
        To end the game enter the whole word.
        IMPORTANT - word 'lifePoints' is not included in words list.
        If you type word 'lifePoints' you will see how many lives you have left.
""")
print(word)
print(f'Your word has {len(word)} letters')
while lifePoints != 0:
    guess = str(input('Enter your guess: '))
    if guess == word:
        print(f'Congratulations you have guessed the word! {word}')
        break

    elif len(guess) > 1 and guess != word and guess != 'lifePoints':
        print('Unfortunately your word is incorrect. Try again.')
        lifePoints -= 1
        print(f'Length of the word - {len(word)}')
        print(guessedLetters)

    elif guess == 'lifePoints':
        print(f'You have {lifePoints} more lives')

    elif guess in setWord:
        print(f'You have guessed the letter - {guess} is in on the {word.index(guess) + 1} position')
        guessedLetters.insert(word.index(guess), guess)
        print(f'Length of the word - {len(word)}')
        print(guessedLetters)

    elif guess not in setWord:
        print(f'Missed {guess} letter is not in the word. Try again')
        lifePoints -= 1
        print(f'Length of the word - {len(word)}')
        print(guessedLetters)
