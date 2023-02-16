import numpy as np

# This game lets a user guess the number and then hints them if
# their inaccurate guess is more or less than X.

number = np.random.randint(1,100) # Makes up a number

count = int() # Sets a counter for tries
predict_number = int(input('Guess the number 1 to 100!  >'))
while True:
    count += 1
    print()
    if predict_number == number:
        break # Win!
    if predict_number <= number:
        print('It\'s bigger than that!')
        predict_number = int(input('Guess once more!  >'))
    if predict_number >= number:
        print('It\'s lesser than that!')
        predict_number = int(input('Guess once more!  >'))
        
print('Congratulations! You\'ve done it in',count,'tries!')