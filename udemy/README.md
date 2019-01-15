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
