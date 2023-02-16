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
        predict_number = np.random.randint(1,100)
        if number == predict_number:
            break # exit cycle on guessing right
    return count


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