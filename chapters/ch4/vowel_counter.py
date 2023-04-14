vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def count_the_vowels(user_input):
    count = 0
    for character in user_input:
        for vowel in vowels:
            if character == vowel:
                count += 1

    return count


def reveal_number():
    user_input = input('Please enter a word or sentence: ')
    number = count_the_vowels(user_input)
    print(f'Number of vowels in your input = {number}')


if __name__ == '__main__':
    reveal_number()