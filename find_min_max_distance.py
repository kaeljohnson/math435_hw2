import pandas as pd
import numpy as np


if __name__ == '__main__':
    distances = pd.read_csv('distances_tra.csv').to_numpy()

    min_num = float('inf')
    max_num = -1
    for row in distances:
        for test_num in row:
            if(test_num > max_num):
                max_num = test_num
            if(test_num < min_num and test_num != 0):
                min_num = test_num

    print("Max is: " + str(max_num) + " Min is: " + str(min_num))
