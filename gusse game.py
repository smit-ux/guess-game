secret_number = 9
guess_count = 0
guess_limit = 3
print('##############################################')
print('#\t\t\t\tGUESS GAME                   #')
print('#   ^-^      BY: SMIT PRAJAPATI       ^-^    #')
print('##############################################')
while guess_count < guess_limit:
    guess = int(input('GUESS THE NUMBER:'))
    guess_count += 1
    if guess == secret_number:
        print('##############################################')
        print("#\t\t\tYOU WIN !!!!:)                   #")
        print('##############################################')
        break
else:
    print('##############################################')
    print("#\t\t\tYOU LOST :((                     #")
    print('##############################################')





