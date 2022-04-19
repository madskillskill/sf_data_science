import numpy as np

number = np.random.randint(1,100)

def random_predict(number:int=1)->int:
    """Случайное угадывание числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1,100)
        if number == predict_number:
            break
    return count
print('It took this amount of tries', random_predict())

def score_game(random_predict)->int:
    count_tries = []
    np.random.seed(1)
    random_array = np.random.randint(1,100,size=(1000))
    for number in random_array:
        count_tries.append(random_predict(number))
    score = int(np.mean(count_tries))
    print('tries attempted:', score)
    return(score)

if __name__ == '__main__':
    score_game(random_predict)