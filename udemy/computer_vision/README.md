## Advanced computer vision course
- will use Keras
- run `conda install -n tfdeeplearning keras`
- run `conda install -n tfdeeplearning pillow`
- run `jupyter notebook` within this dir

## MNIST as a sanity check
- just like we used MNIST 0-9 data set to confirm if algorithm worked in the past, we'll use Fashion MNIST to do so now.  This is a bit better as a sanity check than the 0-9 handwritten digits, but still has 10 possible labels, 28x28 pixel images with grayscale coloring.
  * dataset: https://www.kaggle.com/zalando-research/fashionmnist

# VGG (visual geometry group)
- performs better than some of the newer classifiers such as ResNet/Inception for many tasks such as style transfer
- great for transfer learning
# Greedy layer wise pre-training
- transfer learning
- train autoencoder to reproduce original image, then remove second half, and use first half as first layer of final NN
- do this again, but only reproduce the transformation from 1st layer, then append the half from this step to the first half.  Rinse and repeat .. n times then add logistic regression at the end.
# Resnet
- diverges from usual LeNet derivatives
- more layers of convolution is great, but there is a tipping point where perf. starts to degrade
  * they take too long to train
- focus on residual, desired mapping minus identity.  skip intermediate layers and map input to output
- Wx + b -> relu -> W + b + relu   ?
- since we're adding X + F(x) in the same layer, the output must be the same size as the input.
- sometimes if they differ, we will multiply X by Ws which can be trainable or simply pad 0s to X
- ResNet: 16 resnet blocks 16 * 3 = 48 layers
 * Architecture: conv block + batch normalization + max pooling, then conv block, 2 identity blocks, another conv block, 3 identity blocks, a conv block, then 5 identity blocks, a conv block, then 2 identity blocks, then average pooling/flatten density block
 * note: building a ResNet in keras, and then calling `.summary()` on it, will display ^ architecture if you forget
 * conv blocks should be in 'same' mode, except when it is a 1x1 convolution then use 'valid' mode (or just use keras and it will handle that for you)
# Handling images of different sizes
- need operation that gives same output regardless of input size
- global max pooling + global average pooling
- in keras, can just add GlobalMaxPooling2D or GlobalAveragePooling2D layer types to your model to accomplish this.
# Object Localization
- this is finding objects within an image rather than classifying an entire image (where are a person's eyes for example)
- use bounding boxes to find placement
- loss function: if not just classification, then not just cross entropy
  * if image with no objects, then binary cross entropy
  * many classes, then categorical cross entropy or MSE / Huber / Smooth / L1
- sliding windows: slide window over the image to find sub-images
  * problem: this moves slower because each image now becomes many
  * how to solve? sliding window behaves just like convolution (called SSD)
- problems of scale:
  * in a CNN: the image shrinks at each layer
  * SSD architecture: attach mini-neural networks to intermediate layers of pre-trained network
- problems of shape:
  * people vs cars - very different shapes in an image - constrain image search by box sizes
# Neural Style Transfer
- input has 2 images, we apply the style of the first to the second
- 
