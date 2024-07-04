"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Milan Komůrka

email: komurka.milan@email.cz

discord: mylca666

"""
# TEXTS import
from task_template import TEXTS

# Dict of users
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'

}

line = '-' * 40


# Sign in verification
def verification(user, password):
    if user in users and users[user] == password:
        return True
    else:
        return False


# Sign into analyzator
user = input('username: ')
password = input('password: ')
if verification(user, password):
    print(f'''
{line}
Welcome to the app, {user}
We have 3 texts to be analyzed.
{line}
''')
else:
    print(f'''
username: {user}
password: {password}
unregistered user, terminating the program...
''')
    exit()

# NO of text pickup
text_NO = int(input('Enter a number btw. 1 and 3 to select: '))
print(line)

text_0 = TEXTS[text_NO - 1]

# Split text to words
words = text_0.split()

# Text statistics
NO_words = len(words)
NO_titlecase_words = sum(1 for word in words if word.istitle())
NO_uppercase_words = sum(1 for word in words if word.isupper()
                         and not word[0].isdigit())
NO_lowercase_words = sum(1 for word in words if word.islower())
NO_numeric_strings = sum(1 for word in words if word.isdigit())
sum_numbers = sum(int(word) for word in words if word.isdigit())

# Results print
print(f'There are {NO_words} words in the selected text.')
print(f'There are {NO_titlecase_words} titlecase words.')
print(f'There are {NO_uppercase_words} uppercase words.')
print(f'There are {NO_lowercase_words} lowercase words.')
print(f'There are {NO_numeric_strings} numeric strings.')
print(f'The sum of all the numbers {sum_numbers}')
print(line)

# Dictionary for count frequency of lenght of words
len_words = {}
for word in words:
    lenght = len(word)
    if lenght in len_words:
        len_words[lenght] += 1
    else:
        len_words[lenght] = 1

# 'Stars' Bar chart
print('LEN|  OCCURENCES  |NR.')
print('-' * 40)
for lenght, frequency in sorted(len_words.items()):
    stars = '*' * frequency
    print(f'{lenght:3}|{stars:<14}|{frequency}')