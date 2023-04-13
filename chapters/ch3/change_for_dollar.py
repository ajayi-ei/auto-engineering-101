print("Welcome to the Change for Dollar Game")


def sum_all_coins(pennies, nickels, dimes, quarters):
    global total
    total = int(pennies) + int(nickels)*5 + int(dimes)*10 + int(quarters)*25
    return sum


def generate_result():
    if total == 100:
        print('You win!')

    if total < 100:
        under = 100 - total
        print(f'You lose... You were under by {under} cents')

    if total > 100:
        over = total - 100
        print(f'You lose... You were over by {over} cents')


user_response = 'Y'
while user_response == 'Y':
    pennies = input("\nPlease enter the number of pennies you have: ")
    nickels = input("Please enter the number of nickels you have: ")
    dimes = input("Please enter the number of dimes you have: ")
    quarters = input("Please enter the number of quarters you have: ")
    sum_all_coins(pennies, nickels, dimes, quarters)
    generate_result()
    user_response = input("\nPlay again? 'Y' for Yes, 'N' for No: ")
    while user_response != 'Y' and user_response != 'N':
        user_response = input("Please enter a valid response. 'Y' for Yes, 'N' for No: ")




