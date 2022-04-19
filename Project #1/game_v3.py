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
    predict_number = 50
    top_line = 100
    bottom_line = 1
    while True: # initiate guessing
        count += 1
        
        
        if predict_number == number:
            break # exit cycle on guessing right
        if predict_number < number:
            bottom_line = predict_number
            predict_number = int(np.mean(top_line+predict_number)/2)
        if predict_number > number:
            top_line = predict_number
            predict_number = int(np.mean(bottom_line+predict_number)/2)
    print(f'Загаданным числом было {number}, Понадобилось {count}')
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
    
    random_array = np.random.randint(1,100,size=(1000)) # Collects numbers to guess
    for number in random_array:
        count_tries.append(random_predict(number))
        
    # Applies random_guess to each element of array and gets back number of tries
    
    score = int(np.mean(count_tries)) # Gets the average number of tries
    print(f'1, {count_tries.count(1)}')
    print(f'2, {count_tries.count(2)}')
    print(f'3, {count_tries.count(3)}')
    print(f'4, {count_tries.count(4)}')
    print(f'5, {count_tries.count(5)}')
    print(f'6, {count_tries.count(6)}')
    print(f'7, {count_tries.count(7)}')
    print(f'8, {count_tries.count(8)}')
    print('On average, guessing took', score, 'tries.')
    return(score)

#if __name__ == '__main__':
#    score_game(random_predict)
score_game(random_predict)