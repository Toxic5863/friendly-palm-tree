import pickle
from sklearn.neural_network import MLPClassifier


ann_file = open("ANN", "rb")
trained_network = pickle.load(ann_file)

print(trained_network.predict([[0, 1, 0]]))