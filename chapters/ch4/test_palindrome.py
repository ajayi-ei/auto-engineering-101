from chapters.ch4.palindrome import check_palindrome, check_one_word


def test_is_not_one_word_1():
    one_word_or_not = check_one_word('')
    message = f'Your input is {one_word_or_not}'
    assert message == 'Your input is not one word \'only\''


def test_is_not_one_word_2():
    one_word_or_not = check_one_word('hello madam')
    message = f'Your input is {one_word_or_not}'
    assert message == 'Your input is not one word \'only\''


def test_is_palindrome():
    palindrome_or_not = check_palindrome('madam')
    message = f'Your word is {palindrome_or_not}'
    assert message == 'Your word is a palindrome'


def test_is_not_palindrome():
    palindrome_or_not = check_palindrome('hallo')
    message = f'Your word is {palindrome_or_not}'
    assert message == 'Your word is not a palindrome'
