import scipy
import pandas as pd
import numpy as np


#def predictedFunction(parameter_list):
#    return 1 if (parameter_list[0] != parameter_list[1]) == parameter_list[2] else 0

def create_binary_input_data(shape_a, shape_b):
    input_data = np.zeros((shape_a, shape_b))
    for x in range(input_data.shape[0]):
        for y in range(input_data.shape[1]):
            input_data[x][y] = np.random.randint(0, 2)
    return input_data

def create_binary_output_data(input_data, func):
    output_data = np.zeros((input_data.shape[0], 1))
    for x in range(output_data.shape[0]):
        output_data[x][0] = 1 if func(input_data[x]) else 0
    return output_data

#print(input_data[0])
#print(output_data[0])
