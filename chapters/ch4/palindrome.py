def check_one_word(user_input):
    number_of_error_in_input = 0
    if user_input == '':
        number_of_error_in_input += 1
    for characters in user_input:
        if characters == ' ':
            number_of_error_in_input += 1
    if number_of_error_in_input != 0:
        return 'not one word \'only\''
    elif number_of_error_in_input == 0:
        return 'one word \'only\''


def check_palindrome(user_input):
    check = check_one_word(user_input)
    if check == 'one word \'only\'':
        word_as_list = list(user_input)
        reversed_word_as_list = word_as_list[:]
        reversed_word_as_list.reverse()

        i = 1
        number_of_non_matching_letters = 0
        for letters in word_as_list:
            if letters != reversed_word_as_list[i-1]:
                number_of_non_matching_letters += 1
            i += 1

        if number_of_non_matching_letters == 0:
            return 'a palindrome'
        else:
            return 'not a palindrome'


def reveal_if_palindrome():
    user_input = input('Please enter just one word without spaces: ')
    confirm_is_one_word = f'Your input is {check_one_word(user_input)}'
    print(confirm_is_one_word)
    if confirm_is_one_word == 'Your input is one word \'only\'':
        reveal = check_palindrome(user_input)
        print(reveal)


if __name__ == '__main__':
    reveal_if_palindrome()
