import pickle
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import DataClean

def predictedFunction(alist):
    return (alist[0] != alist[1]) == alist[2]

input = DataClean.create_binary_input_data(1000, 3)
output = DataClean.create_binary_output_data(input, predictedFunction)

input_train, input_test, output_train, output_test = train_test_split(input, output)

ANN = MLPClassifier(hidden_layer_sizes=(100), activation='relu')
ANN.fit(input_train, output_train)
if (ANN.score(input_test, output_test) == 1):
    print("Fitting successful. Serializing neural network")
    file = open("ANN", "wb+")
    pickle.dump(ANN, file)
    file.close()
else:
    print("Fitting unsuccessful.")
