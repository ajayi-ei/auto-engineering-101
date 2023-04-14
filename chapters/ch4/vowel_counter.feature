Feature: Count the number of vowels in an input string and returns the number to the user
Scenario: Entering a string with vowels returns the number of vowels present in it.
  Example:
    Given user_input = 'hello world!'
    When I count the number of vowels
    Then I should return 3

  Example:
    Given user_input = 'rhythms'
    When I count the number of vowels
    Then I should return 0

  Example:
    Given user_input = 'AeIoU aEiOu'
    When I count the number of vowels
    Then I should return 10