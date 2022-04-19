import numpy as np

# This game lets a user guess the number and then hints them if
# their inaccurate guess is more or less than X.

number = np.random.randint(1,100) # Makes up a number

count = int(5.5) # Sets a counter for tries
print(count)

while True:
    count += 1
    predict_number = int(input('Guess the number 1 to 100!'))
    if predict_number == number:
        break # Win!
    if predict_number <= number:
        print('More')
    if predict_number >= number:
        print('Less')
        
print('Congratulations! You\'ve done it in',count,'tries!')