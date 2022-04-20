# This version of a program knows if it guessed way more or less
# and act accordingly

import numpy as np

number = np.random.randint(1,100)

def random_predict(number:int=1)->int:
    """Guesses a number in a 1-100 range by knowing,
       if previous guess higher or lower than needed.
       It tracks highest and lowest possible answer,
       and always go for the mean number between them,
       e.g. (top+bottom)/2

    Args:
        number (int, optional): Made up number. Defaults to 1.

    Returns:
        int: A number of tries before the first right guess
    """
    count = 0
    predict_number = 50 # setting the first guess strict
    top_line = 100
    bottom_line = 1
    while True: # initiate guessing
        count += 1
        if predict_number == number:
            break # exit cycle on guessing right
        if predict_number < number:
            bottom_line = predict_number # cut off numbers that are too low
            predict_number = int((top_line+predict_number)/2) # makes mean prediction
        if predict_number > number:
            top_line = predict_number # cut off numbers that are too big
            predict_number = int((bottom_line+predict_number)/2) # makes mean prediction
    return count

def score_game(random_predict)->int:
    """Brings the average number of tries the first function needs to guess right. Sample size = 1000

    Args:
        random_predict (int): guesses the right number

    Returns:
        int: the average of cycles in 1000 tries to guess
    """    
    count_tries = []
    np.random.seed(1) # Fixes the seed
    
    random_array = np.random.randint(1,100,size=(1000)) # Collects the array numbers to guess
    for number in random_array:
        count_tries.append(random_predict(number))
        
    # Applies random_predict to each element of the array and gets back number of tries
    
    score = int(np.mean(count_tries)) # Gets the mean number of tries
    return(score)

if __name__ == '__main__':
    print(score_game(random_predict)) # runs if executed directly