require_explanation = input('Hello, welcome to hangman! Type y if you would like me to explain the rules or n if you '
                            'are ready to play.')

if require_explanation == 'y':
    print('Hangman is very simple. I will think of a random word. I will give you the number of letters in my word '
          'indicated by _s. You will then try to guess my word by trying letters one at a time. If the letter you '
          'guessed is in my word I will fill in the corresponding blank. If not, you get one strike. You have 6 '
          'strikes total. Good luck!'
    )


import random


words = ('earpiece',
         'laptop',
         'clock',
         'pastry',
         'telephone',
         'basketball',
         'warrior',
         'jacket',
         'ostrich',
         'xylophone'
)

word = random.choice(words)
print(' _ ' * len(word))

guessed_letters = []
correct_letters = ['_'] * len(word)


def pieces_of_word():
    for index in range(len(word)):
        original_letter = word[index]
        if letter == original_letter:
            print(letter)
            correct_letters[index] = original_letter
        elif original_letter in correct_letters:
            print(original_letter)
        else:
            print('_')
    if ''.join(correct_letters) == word:
        print('You win!')


def add_to_list():
    guessed_letters.append(letter)
    print('You have guessed these letters so far: ' + str(guessed_letters))


counter = 6


while counter > 0 and sorted(correct_letters) != sorted(word):
    letter = input('Guess a letter')
    if letter in guessed_letters:
        print('You already guessed this letter! Please try another letter')
    elif letter in word:
        add_to_list()
        pieces_of_word()
    else:
        add_to_list()
        pieces_of_word()
        counter -= 1
        print('You have ' + str(counter) + ' guesses left')


if counter == 0:
    print('Sorry, you did not guess the word in time!')
