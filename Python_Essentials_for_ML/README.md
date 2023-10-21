# Introduction

## 🤔 What is ML (Machine Learning)?

Machine Learning is the study of computer algorithms that improve automatically through experience. In a traditional software, we have a set of rules that the computer follows to solve a problem.

```python
if (x > 0):
    print("x is positive")
else:
    print("x is negative")
```

When we need a lot of rules, the software becomes very complex and difficult to maintain. In Machine Learning, we give the computer a set of data and the computer learns the rules by itself. For example, we give the computer a set of images of 🐱 cats and 🐶 dogs and the computer learns how to differentiate between cats and dogs.

<p align=center>
    <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*t6Myx_4eEwaWP9Vms_kYfg.png" height=300>
    <p align=center>
        <a href="https://sravya-tech-usage.medium.com/traditional-programming-vs-machine-learning-e9bbed5e491c">Source</a>
    </p>
</p>

We have a lot of subareas in Machine Learning, some of them are:
- Computer Vision
- Natural Language Processing
- Speech
- Time Series
- Medical
- Graphs

## 🤔 What are the types of Machine Learning?

We have four types of Machine Learning:
- **Supervised Learning**
    In Supervised Learning, we have a set of data with the input and the output. For example, we have a set of images of 🐱 cats and 🐶 dogs and we know which image is a cat and which image is a dog. We use this set of data to train the computer to learn the rules to differentiate between cats and dogs. After the training, we have a model that can predict if an image is a cat or a dog. Or, we have continuous data, like the price of a 🏠 house, and we want to predict the 💵 price of a new house. In this case, we have a set of data with the price of the house and the features of the house, like the number of rooms, the size of the house, the number of bathrooms, etc. We use this set of data to train the computer to learn the rules to predict the price of a new house. After the training, we have a model that can predict the price of a new house.
- **Unsupervised Learning**
    In Unsupervised Learning, we have a set of data with only the input. For example, we have a set of images of 🐱 cats and 🐶 dogs and we don't know which image is a cat and which image is a dog. We use this set of data to train the computer to learn the rules to differentiate between cats and dogs. After the training, we have a model that can predict if an image is a cat or a dog.
- **Semi-supervised Learning**
    In Semi-supervised Learning, we have a set of data with the input and the output, but we have a lot of data without the output. For example, we have a set of images of 🐱 cats and 🐶 dogs and we know which image is a cat and which image is a dog, but we have a lot of images without the label. We use this set of data to train the computer to learn the rules to differentiate between cats and dogs. After the training, we have a model that can predict if an image is a cat or a dog.
- **Reinforcement Learning**
    In Reinforcement Learning, generally, we train the computer to play a game. For example, we train the computer to play 🏓 ping pong. We give a reward to the computer when it does something right and we give a punishment to the computer when it does something wrong. After the training, we have a model that can play ping pong.

## 🧗‍♂️ Main Challenges of Machine Learning


<p align=center>
    <img src="https://cdn-media-1.freecodecamp.org/images/1*bt-E2YcPafjiPbZFDMMmNQ.jpeg" height=300>
    <p align=center>
        <a href="https://www.freecodecamp.org/news/chihuahua-or-muffin-my-search-for-the-best-computer-vision-api-cbda4d6b425d/">Source</a>
    </p>
</p>

- **Insufficient Quantity of Training Data**
    We need a lot of data to train the computer. For example, we need a lot of images of 🐶 chihuahuas and 🧁 cupcakes to train the computer to differentiate between chihuahuas and cupcakes.

- **Nonrepresentative Training Data**
    We need a set of data that represents the real world. For example, we need a set of images of 🐶 chihuahuas and 🧁 cupcakes that represents the real world.

- **Poor-Quality Data**
    We need a set of data with good quality. For this, we need to clean the data.

- **Irrelevant Features**
    We need a set of data with relevant features.

- **Overfitting**
    We need a model that can generalize the data. For example, we have a set of images of 🐶 chihuahuas and 🧁 cupcakes and we train the computer to differentiate between chihuahuas and cupcakes. After the training, we have a model that can differentiate between chihuahuas and cupcakes. But, when we give a new image of a chihuahua or a cupcake, the model can't differentiate between chihuahuas and cupcakes. In this case, we have a model that can't generalize the data.

- **Hyperparameters**
    We need to choose the best hyperparameters to train the computer. We have a lot of hyperparameters to choose, like the number of layers, the number of neurons, the activation function, the optimizer, the learning rate, etc. We need to choose the best hyperparameters to train the computer.
