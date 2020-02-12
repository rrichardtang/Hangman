with open('rules.txt', 'r') as f:
    print(f.read())


import random
import string

words = open('words.txt', 'r').read().split()

word = random.choice(words)

print(' _ ' * len(word))
guessed_letters = []
correct_letters = ['_'] * len(word)


def pieces_of_word():
    for i in range(len(word)):
        original_letter = word[i]
        if letter == original_letter:
            print(letter, end = ' ')
            correct_letters[i] = original_letter
        elif original_letter in correct_letters:
            print(original_letter, end = ' ')
        else:
            print('_', end = ' ')
    if ''.join(correct_letters) == word:
        print('You win!')


def add_letter_to_guessed():
    guessed_letters.append(letter)
    print('You have guessed these letters so far: ' + str(guessed_letters))


counter = len(word) * 2

while counter > 0 and sorted(correct_letters) != sorted(word):
    letter = input('Guess a letter').lower()
    assert len(letter) == 1, 'You can only guess one letter at a time'
    assert letter in string.ascii_lowercase, 'You can only guess letters'
    
    if letter in guessed_letters:
        print('You already guessed this letter! Please try another letter')
    elif letter in word:
        add_letter_to_guessed()
        pieces_of_word()
    else:
        add_letter_to_guessed()
        pieces_of_word()
        counter -= 1
        print('You have {0} guesses left'.format(counter))


if counter == 0:
    print('Sorry, you did not guess the word in time!, the word was {0}'.format\
          (word))
