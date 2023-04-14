from chapters.ch4.vowel_counter import count_the_vowels


def test_count_with_actual_vowels():
    count_number = count_the_vowels('Hello World!')
    message = f'Number of vowels in your input = {count_number}'
    assert message == 'Number of vowels in your input = 3'


def test_count_with_no_vowels():
    count_number = count_the_vowels('rhythms')
    message = f'Number of vowels in your input = {count_number}'
    assert message == 'Number of vowels in your input = 0'


def test_count_with_all_vowels():
    count_number = count_the_vowels('AeIoU aEiOu')
    message = f'Number of vowels in your input = {count_number}'
    assert message == 'Number of vowels in your input = 10'
