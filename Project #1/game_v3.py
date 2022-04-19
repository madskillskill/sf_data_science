# This version of a program knows if it guessed way more or less
# and act accordingly

import numpy as np

number = np.random.randint(1,100)

def random_predict(number:int=1)->int:
    """It makes up a number and guess it at random
       using zero additional information.

    Args:
        number (int, optional): Made up number. Defaults to 1.

    Returns:
        int: A number of tries before the first right guess
    """
    count = 0
    while True: # initiate guessing
        count += 1
        predict_number = 50
        top_line = 100
        bottom_line = 1
        if number == predict_number:
            break # exit cycle on guessing right
        if number > predict_number:
            bottom_line = number
            number = int((top_line+number)/2)
        if number < predict_number:
            number = int((bottom_line+number)/2)
            top_line = number
            
    return count
print(random_predict(number))

def score_game(random_predict)->int:
    ''' Runs random_predict 1000 times'''
    count_tries = []
    np.random.seed(1) # Fixes the seed
    
    random_array = np.random.randint(1,100,size=(1000)) # Collects numbers to guess
    for number in random_array:
        count_tries.append(random_predict(number))
    # Applies random_guess to each element of array and gets back number of tries
    
    score = int(np.mean(count_tries)) # Gets the average number of tries
    print('On average, guessing took', score, 'tries.')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)