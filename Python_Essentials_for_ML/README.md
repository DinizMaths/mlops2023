# Introduction

## 🤔 What is Machine Learning?

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

## ✨ Good Practices

<p align=center>
    <img src="https://i0.wp.com/galaxyinferno.com/wp-content/uploads/2022/06/3.png?resize=768%2C432&ssl=1" height=300>
    <p align=center>
        <a href="https://galaxyinferno.com/what-is-validation-data-used-for-machine-learning-basics/">Source</a>
    </p>
</p>

Make sure that you have a good set of data. For this, you need to split your data into three sets: training set, validation set, and test set. This can make a big difference in the performance of your model.

Previous Machine Learning Era:
Train | Validation | Test
----- | ---------- | ---
70%   | 0%         | 30%
60%   | 20%        | 20%

Big Data Era:
Train | Validation | Test
----- | ---------- | ---
98%   | 1%         | 1%
99.5% | 0.25%      | 0.25%
99.5% | 0.4%       | 0.1%

But, we need to make sure that the validation set and the test set come from same distribution.

## 📏 Bias vs Variance

|                       | Scenario 1 | Scenario 2 | Scenario 3 | Scenario 4 |
| --------------------- | ---------- | ---------- | ---------- | ---------- |
| Train Set Error       | 1%         | 15%        | 15%        | 0.5%       |
| Validation Set Error  | 16%        | 16%        | 30%        | 1%         |
| **Bias**              | Low        | High       | High       | Low        |
| **Variance**          | High       | Low        | High       | Low        |

- **Scenario 1**
    In Scenario 1, we have a low bias and a high variance. In this case, we have a model that can learn the data, but it can't generalize the data. 

- **Scenario 2**
    In Scenario 2, we have a high bias and a low variance. In this case, we have a model that can't learn the data, but it can generalize the data.

- **Scenario 3**
    In Scenario 3, we have a high bias and a high variance. In this case, we have a model that can't learn the data and it can't generalize the data.

- **Scenario 4**
    In Scenario 4, we have a low bias and a low variance. In this case, we have a model that can learn the data and it can generalize the data.

Basic Recipe for Machine Learning:
- If high bias, then:
    - Try a bigger network
    - Try a different model
    - Try a different architecture
    - Try a different hyperparameters
- If high variance, then:
    - Get more data
    - Try regularization
    - Try a different model
    - Try a different architecture
    - Try a different hyperparameters

<p align=center>
    <img src="https://www.researchgate.net/profile/Bo-Fu/publication/331670185/figure/fig1/AS:735471835553794@1552361558681/Model-complexity-vs-Total-Error-The-optimal-models-are-likely-to-belong-to-the-class-of.png" height=300>
    <p align=center>
        <a href="https://www.researchgate.net/figure/Model-complexity-vs-Total-Error-The-optimal-models-are-likely-to-belong-to-the-class-of_fig1_331670185">Source</a>
    </p>
</p>

## 📊 Evaluate Classification Models

- **Threshold Metrics**
    Ratio of correct predictions (positive or negative) among all predictions made.

    - Accuracy
    - Error
    - Sensitivity
    - Specificity
    - G-Mean
    - Precision
    - Recall
    - Fbeta-Measure

- **Ranking Metrics**
    Based on score of class membership and variation of threshold to measure the effectiveness of classifiers.

    - ROC Curve
    - ROC AUC
    - Precision-Recall Curve

- **Probabilistic Metrics**
    Quantify the uncertainty of the prediction.

    - Log Loss
    - Brier Score

<p align=center>
    <img src="https://machinelearningmastery.com/wp-content/uploads/2019/12/How-to-Choose-a-Metric-for-Imbalanced-Classification-latest.png"
    height=500/>
    <p align=center>
        <a href="https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/">Source</a>
    </p>
</p>

## 🧮 Confusion Matrix

<p align=center>
    <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*fxiTNIgOyvAombPJx5KGeA.png"
    height=300/>
    <p align=center>
        <a href="https://towardsdatascience.com/confusion-matrix-for-your-multi-class-machine-learning-model-ff9aa3bf7826">Source</a>
    </p>
</p>

- **True Positive (TP)**
    The model correctly predicts the positive class.

- **True Negative (TN)**
    The model correctly predicts the negative class.

- **False Positive (FP)**    
    The model incorrectly predicts the positive class.

- **False Negative (FN)**
    The model incorrectly predicts the negative class.

We can extract a lot of metrics from the confusion matrix. Some of them are:

$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$

$\text{Error} = 1 - \text{Accuracy}$

$\text{Senstivity or Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$

$\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}$

$\text{G-Mean} = \sqrt{\text{Senstivity} \times \text{Specificity}}$

$\text{Positive Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$

$\text{Negative Precision} = \frac{\text{TN}}{\text{TN} + \text{FN}}$

$\text{Fbeta-Measure} = \frac{(1 + \beta^2)\times \text{Positive Precision} \times \text{Senstivity}}{\beta^2 \times \text{Positive Precision} + \text{Senstivity}}$
- $\beta = 0.5$
        More weight on positive precision
- $\beta = 1.0$
        Same weight on positive precision and senstivity, equal to F1-Measure
- $\beta = 2.0$
        More weight on senstivity

## 📈 ROC Curve

<p align=center>
    <img src="https://machinelearningmastery.com/wp-content/uploads/2018/08/ROC-Curve-Plot-for-a-No-Skill-Classifier-and-a-Logistic-Regression-Model.png"
    height=300/>
    <p align=center>
        <a href="https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/">Source</a>
    </p>
</p>

- **True Positive Rate (TPR)**
    The model correctly predicts the positive class.

- **False Positive Rate (FPR)**
    The model incorrectly predicts the positive class.

Usually, we use the area under the ROC curve to evaluate the model.

## 📉 PR Curve

<p align=center>
    <img src="https://machinelearningmastery.com/wp-content/uploads/2018/08/Precision-Recall-Plot-for-a-No-Skill-Classifier-and-a-Logistic-Regression-Model4.png"
    height=300/>
    <p align=center>
        <a href="https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/">Source</a>
    </p>
</p>

Better than ROC curve when we have an imbalanced dataset.

# 📚 References