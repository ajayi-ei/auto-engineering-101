Feature: Checks if a word inputted is a palindrome or not and tells the user


Scenario: Not entering one word only returns not one word 'only'.
  Example:
    Given user_input = ''
    When I check if it is one word
    Then I should return 'Your input is not one word 'only''

  Example:
    Given user_input = 'hello madam'
    When I check if it is one word
    Then I should return 'Your input is not one word 'only''


Scenario: Entering a palindrome returns palindrome
  Example:
    Given user_input = 'madam'
    When I check if word is one word, then a palindrome
    Then I should return 'Your word is a palindrome'


Scenario: Entering a non-palindrome returns not a palindrome
  Example:
    Given user_input = 'hallo'
    When I check if word is a palindrome
    Then I should return 'Your word is not a palindrome'