# Traffic Sign Recognition using Convolutional Neural Network

In the world of Artificial Intelligence and advancement in technologies, many researchers and big companies like Tesla, Uber, Google, Mercedes-Benz, Audi, etc are working on autonomous vehicles or self-driving cars. For achieving accuracy in this area, it is necessary for vehicles to understand and follow all traffic rules. The vehicles should be able to interpret traffic signs and make decisions accordingly. Under this project, we have built a machine learning model which takes an image of a traffic sign and predicts it's meaning.

## Goal
Detecting and recognizing emerging traffic signs for the smooth functioning of autonomous vehicles

## Abstract
Traffic signs are an integral part of our road infrastructure. They provide critical information for road users, which in turn requires them to adjust their driving behaviour to make sure they adhere with whatever road regulation currently enforced. Autonomous vehicles must also abide by road legislation and therefore recognize and understand traffic signs. There are several different types of traffic signs like speed limits, no entry, turn left or right, children crossing, no passing of heavy vehicles, etc. Traffic signs classification is the process of identifying which class a traffic sign belongs to. Using the most popular image classification strategy Convolutional Neural Network, we have built a machine learning model that classifies traffic sign present in the image into different categories.

In our model, the dataset containing images of different classes are used to train the algorithm. The model is used to test the data for accuracy and is saved. This model is used to predict the class of the image. The user sends the image through a frontend interface through a REST API POST request. The request is directed to the server and processed. The class of the image is predicted and displayed to the user on the dashboard.

## Architecture Diagram:

![Project Architecture Diagram](https://github.com/SJSUSpring2020-CMPE272/Traffic-Sign-Recognition/blob/master/images/Arch.jpeg)

### CNN Model Architecture:

We are using the [GTSRB](http://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset) dataset. The dataset is split into training, test and validation sets, with the following characteristics:
* Images are 32 (width) x 32 (height) x 3 (RGB color channels)
* Training set is composed of 39209 images
* Validation set is composed of 10104 images
* Test set is composed of 2526 images
* There are 43 classes (e.g. Speed Limit 30km/h, No entry, Children Crossing, etc.)

The network is composed of 5 convolutional layers with kernel size for first layer 5x5 and 3x3 for rest, We have used ReLU as the activation function, each followed by a 2x2 max pooling operation. The last 3 layers are fully connected, with the final layer producing 43 results (the total number of possible labels) computed using the SoftMax activation function. The network is trained using mini-batch stochastic gradient descent with the Adam optimizer. We have handled the imbalance in no of images for classes by introducing class weights.

![CNN Architecture Diagram](https://github.com/SJSUSpring2020-CMPE272/Traffic-Sign-Recognition/blob/master/images/arch1.jpeg)

![Architecture Diagram](https://github.com/SJSUSpring2020-CMPE272/Traffic-Sign-Recognition/blob/master/images/arch2.jpeg)
 
## Technology Stack
1. Frontend : React
2. Backend  : Flask, Python
3. Machine Learning Model : Convolutional Neural Networks
4. Libraries : Tensorflow, Keras, Scikit-Learn, Pandas, Numpy, Pillow
5. Editors : IBM Watson Studio, Jupyter Notebook
5. Platforms : AWS-EC2
