  
from rishabh.NN import perceptron
import numpy as np

# Construct the 'OR' dataset
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [1]])

# Train the perceptron
print('[INFO]: Training....')
p = perceptron(X.shape[1], a=0.1)
p.fit(X, y, epochs=20)

# Test the perceptron
print('[INFO]: Testing....')

# Loop over the data points
for (x, target) in zip(X, y):
    # Make a prediction and display the result
    pred = p.predict(x)
    print('[INFO]: Data={}, Ground Truth={}, Prediction={}'.format(x, target[0], pred))