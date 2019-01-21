## Course
  - https://www.udemy.com/complete-guide-to-tensorflow-for-deep-learning-with-python/learn
  - download course notes from lecture 2 -> course-notes dir
  - get anaconda distro (https://www.anaconda.com/download/) - python + data science
      * may need to move `conda` setup from .bash_profile to .zshrc
  - run `conda env create -f mac_tfdl_env.yml` from course-notes dir (download mac tfdl from faq section)
  - run `conda activate tfdeeplearning` to activate env
  - run `jupyter notebook` to fire up jupyter (opens browser)

## Machine learning overview

  - supervised learning: (uses labeled data)
    * if continuous (regression), if categorical (classification)
    * given height + weight, predict gender (classification)
    * given house square footage, predict price (regression) (model trained on historical data)
  - unsupervised learning (clustering)
    * features height + weight for dog breeds
    * no labels for unsupervised
    * task: cluster data into groups, then data scientist determines dog breed (label)
  - re-enforcement learning
    * components: agent/decision maker, environment (what it interacts with), actions: what it can do
  - supervised machine learning process overview:
    * get data
    * data cleaning (train/test split)
    * train model
    * adjust model parameters (keep doing these last 2 steps until you are happy with model)
    * deploy model
    * may also want to keep a `holdout` data set in addition to the train/test split, because we are adjusting model parameters against the test set initially, so this will give us a better staging test.
    * regression eval (MAE, MSE, RMSE)

 ## Intro to Neural Networks
  - WiXi + b (weight * input for each input item + bias term (bias term tweaks for 0 input value))
  - input layer (real values from user), hidden layers (in b/t input -> output) 3 or more hidden == deep, output layer - final estimate
  - Activation Functions
    * sigmoid function: f(x) = 1/(1 + e ^(-x)) - output goes from 0 to 1
    * hyperbolic tangent tanh f(x) = tanh(x) = sinh(x) / cosh(x)  goes from -1 to 1
    * rectified linear unit (ReLU) max(0, z)    reminder: (z = wx + b)
  - Cost Functions: (reminder - 'y' is true value, 'a' is predicted value)
    * sum of (y-a)^2 / n   (quadratic)
    * cross entropy: C = (-1/n) * sum (y * ln(a) + ((1 - y) * ln(1-a))
  - Gradient Descent: (finds the minimum of a function - in this case we use it to find minimum of cost function)
    * gradient == derivative of function at a particular point and determining what direction
    * backpropagation - used to update the error rate of each neuron
  - Tensorflow playground (https://playground.tensorflow.org)
  - Manual Neural Network
      * see jupyter notebook
  - Tensorflow
    * constants + sessions + actions (see jupyter notes)
    * graphs (variables / placeholders)
      - placeholders are initially empty but must have shape + type of data
      - graph of wx + b = z w (variable) x (placeholder) -> tf.matmul() -> tf.add(b - variable) -> activation function
      - then add cost function to train network to optimize see `my neural network` jupyter notebook
## Convolusional Neural Networks
- quick review:
  * single neuron: wx + b = z
  * activation functions: perceptrons, sigmoid, tanh, ReLU
  * network has input + output layers, as well as the hidden layers
  * to learn: need measurement of error (quadratic + cross entropy)
  * minimize error with gradient descent
  * backpropagate gradient descent through layers back to input layer
- training techniques: dropout (remove neurons randomly to avoid overfitting), expanding data, l1/l2 regularization (penalty for large weights in model)
- MNIST (0-9 handwritten images of numbers)
  * first flatten it out to 1 dimensional array
  * one hot encoding for labels (1 array for each image)
  * labels end up being a large 2 dimensional array
  * softmax regression: returns list of values from 0-1 that add up to 1 (list of probabilities)
  * Tensors make it convenient to feed in sets of images to our models (IHWC)
  * densley connected layer = every neuron is connected to every other neuron in the next layer
  * convolusional (mirrors biological) - each neuron is connected to a smaller number of nearby neurons in the next layer
  * why use convolusional vs DNN? image processing even with basic images has too many pixels, DNN doesn't scale but convolusional does because it is only the nearby neurons of the next layer.
  * pixels near each other also are more tightly correlated with eachother.
  * when we get to the edge of the image, there may not be any input, so we can add padding for these.
  * each filter detects a different feature, tensor has # of filters by # of units H*W (3D)
  * pooling - create subset of pixels and evaluate the max value, only the max value makes it to the next layer and is representative of the pool.  Even small pooling with a stride of 2 (2x2 pixels) will remove 75% of the input data
  * dropout - randomly drop units along with their connections to prevent overfitting
  * see code along in jupyter notebook for CNN network
