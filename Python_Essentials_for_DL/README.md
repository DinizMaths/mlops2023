# Introduction

## 🤔 What is Deep Learning?

Deep learning is a subfield of machine learning that is inspired by artificial neural networks, which in turn are inspired by biological neural networks.

## 🧠 Perceptron

<p align=center>
    <img src="https://miro.medium.com/v2/resize:fit:828/format:webp/1*OHJhS89QGKVuP1FFRzEw-w.png" height=200>
    <p align=center>
        <a href="https://becominghuman.ai/a-brief-introduction-to-perceptron-f3b9bade8f67">Source</a>
    </p>
</p>

$y = w_0 + \sum_i{x_i \cdot w_i}$

$\sigma(y) = \sigma \left(w_0 + X^t W \right)$

### 📈 Main Activation Functions $\sigma$

- **Linear**:
    $\sigma(x) = x$

    <p align=center>
        <img src="https://assets-global.website-files.com/5d7b77b063a9066d83e1209c/60d244bb0e12c94fb442c01e_pasted%20image%200%20(4).jpg" height=200>
        <p align=center>
            <a href="https://www.v7labs.com/blog/neural-networks-activation-functions">Source</a>
        </p>
    </p>

- **Binary Step**
    $\sigma(x) = \begin{cases} 0 & \text{if } x < 0 \\ 1 & \text{if } x \geq 0 \end{cases}$

    <p align=center>
        <img src="https://assets-global.website-files.com/5d7b77b063a9066d83e1209c/60d2449a8f32de661dfd2c8b_pasted%20image%200%20(3).jpg" height=200>
        <p align=center>
            <a href="https://www.v7labs.com/blog/neural-networks-activation-functions">Source</a>
        </p>
    </p>

- **Sigmoid**
    $\sigma(x) = \frac{1}{1 + e^{-x}}$

    <p align=center>
        <img src="https://assets-global.website-files.com/5d7b77b063a9066d83e1209c/60d24547f85f71e3bd2339f8_pasted%20image%200%20(5).jpg" height=200>
        <p align=center>
            <a href="https://www.v7labs.com/blog/neural-networks-activation-functions">Source</a>
        </p>
    </p>

- **Hyperbolic Tangent**
    $\sigma(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$

    <p align=center>
        <img src="https://assets-global.website-files.com/5d7b77b063a9066d83e1209c/60d246555e0bd43f4bf17b77_Group%2022.jpg" height=200>
        <p align=center>
            <a href="https://www.v7labs.com/blog/neural-networks-activation-functions">Source</a>
        </p>
    </p>

- **Rectified Linear Unit (ReLU)**
    $\sigma(x) = max(0, x)$

    <p align=center>
        <img src="https://assets-global.website-files.com/5d7b77b063a9066d83e1209c/60d24d1ac2cc1ded69730feb_relu.jpg" height=200>
        <p align=center>
            <a href="https://www.v7labs.com/blog/neural-networks-activation-functions">Source</a>
        </p>
    </p>

# 🗂️ Projects

[**🎯 Project 01**](./Project_01/) - **Text Model using Transformers**

<!-- [**🎯 Project 02**](./Project_02/) - **Airflow Data Pipeline to Download Podcasts** -->

# 📚 References

[🏅 **Introduction to Deep Learning in TensorFlow**](https://app.dataquest.io/view_cert/3GW5ERVTQS9GXOAXNIX0)

[🏅 **Sequence Models for Deep Learning**](https://app.dataquest.io/view_cert/7IDVYO692UR4CSKO36ZG)

[🏅 **Natural Language Processing for Deep Learning**](https://app.dataquest.io/view_cert/F8D002085ETY5RPY6GVW)

[🏅 **Building a Data Pipeline**](https://app.dataquest.io/view_cert/NRYMTU8H56I5YVXWASUH)
