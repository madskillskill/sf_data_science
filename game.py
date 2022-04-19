import numpy as np

number = np.random.randint(1,100)

count = 0

while True:
    count += 1
    predict_number = int(input('Guess the number 1 to 100!'))
    if predict_number == number:
        break
    if predict_number <= number:
        print('More')
    if predict_number >= number:
        print('Less')
print('Congratulations! You\'ve done it in',count,'tries!')

