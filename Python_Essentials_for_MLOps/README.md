# Introduction

MLOps revolves around the automation and management of the entire Machine Learning lifecycle. Python's adaptability and rich libraries establish it as the optimal selection for MLOps responsibilities, encompassing tasks like data preprocessing, model training, and deployment. This repository serves as a comprehensive guide, leading you through essential Python concepts and libraries essential for excelling in the realm of MLOps.

At the development stage, was needed to study about:
- **Github Codespaces**
- **Command Line Interface Fundamentals**
- **PEP - Python Enhancement Proposals**
- **Pylint**
- **Errors and Exceptions**
- **Pytest**
- **Logging**

## Github Codespaces

<img src="https://github.blog/wp-content/uploads/2021/08/1200x630-codespaces-social.png?resize=1200%2C630" height=400>

GitHub Codespaces is a cloud-based development environment that enables you to perform your entire development workflow in the cloud. It is a fully-featured, cloud-hosted development environment that allows you to develop entirely in the cloud. It empowers you to create a tailored development environment that suits your requirements, encompassing your tools, dependencies, and extensions. Codespaces enables you to engage in cloud-based development, local machine development, or a combination of both.

[![Microsoft Learn](https://img.shields.io/badge/Microsoft_Learn-258ffa?style=for-the-badge&logo=microsoft&logoColor=white)](https://www.youtube.com/watch?v=ozuDPmcC1io&list=PLmsFUfdnGr3wTl-NCblzcrEv2lFSX975-&index=2) **What is Codespaces?**


[![Microsoft Learn](https://img.shields.io/badge/Microsoft_Learn-258ffa?style=for-the-badge&logo=microsoft&logoColor=white)](https://www.youtube.com/watch?v=SVaqUjBUdMA&list=PLmsFUfdnGr3wTl-NCblzcrEv2lFSX975-&index=3) **Run a default Codespace**

[![Microsoft Learn](https://img.shields.io/badge/Microsoft_Learn-258ffa?style=for-the-badge&logo=microsoft&logoColor=white)](https://www.youtube.com/watch?v=4eYS9pAAf4k&list=PLmsFUfdnGr3wTl-NCblzcrEv2lFSX975-&index=4) **Options to run Codespaces**

[![Microsoft Learn](https://img.shields.io/badge/Microsoft_Learn-258ffa?style=for-the-badge&logo=microsoft&logoColor=white)](https://www.youtube.com/watch?v=AQcwa5-FjpE&list=PLmsFUfdnGr3wTl-NCblzcrEv2lFSX975-&index=5) **Local Visual Studio Code with Codespaces**

[![Microsoft Learn](https://img.shields.io/badge/Microsoft_Learn-258ffa?style=for-the-badge&logo=microsoft&logoColor=white)](https://www.youtube.com/watch?v=s2HpjKv84Oo&list=PLmsFUfdnGr3wTl-NCblzcrEv2lFSX975-&index=6) **Codespaces lifecycle, autosave, and timeout**

## Command Line Interface Fundamentals

<img src="https://jeroenjanssens.com/dsatcl/images/cover-small.png" height=400>

[**Data Science at the Command Line**](https://jeroenjanssens.com/dsatcl/) by Jeroen Janssens was published by O’Reilly Media in October 2021. This website is free to use. This thoroughly revised guide demonstrates how the flexibility of the command line can help you become a more efficient and productive data scientist.

Some chapters was readed to understand the command line interface fundamentals. This is so important to the MLOps because the command line is the main tool to interact with the cloud services, for example. The chapters readed was:

- [**Chapter 2 - Getting Started**](https://jeroenjanssens.com/dsatcl/chapter-2-getting-started)
- [**Chapter 3 - Obtaining Data**](https://jeroenjanssens.com/dsatcl/chapter-2-getting-started)
- [**Chapter 4 - Creating Command-line Tools**](https://jeroenjanssens.com/dsatcl/chapter-2-getting-started)
- [**Chapter 5 - Scrubbing Data**](https://jeroenjanssens.com/dsatcl/chapter-2-getting-started)
- [**Chapter 6 - Project Management with Make**](https://jeroenjanssens.com/dsatcl/chapter-2-getting-started)

## PEP - Python Enhancement Proposals

<img src="https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/PEP-8-Tutorial-Python-Code-Formatting-Guide_Watermarked.9103cf7be328.jpg" height=400>

Python Enhancement Proposals (PEPs) improve the readability and consistency of Python code. You can read more about in [**PEP8 - Real Python**](https://realpython.com/python-pep8/#why-we-need-pep-8). But the main PEPs readed was:

- [**PEP-3107: Function Annotations**](https://www.python.org/dev/peps/pep-3107/)
- [**PEP-484: Type Hints**](https://www.python.org/dev/peps/pep-0484/)
- [**PEP-526: Variable Annotations**](https://www.python.org/dev/peps/pep-0526/)
- [**PEP-557: Data Classes**](https://www.python.org/dev/peps/pep-0557/)
- [**PEP-585: Type Hinting Generics In Standard Collections**](https://www.python.org/dev/peps/pep-0585/)

## Pylint

<img src="https://www.pylint.org/css/pylint.svg" height=100>

[**Pylint**](https://github.com/pylint-dev/pylint) is a static code analysis tool that checks Python code for errors and helps enforce a coding standard.

To install Pylint, run the following command:

```bash
pip install pylint
```

## Errors and Exceptions

<img src="https://images.datacamp.com/image/upload/v1677232088/Exception%20and%20error%20handling%20in%20Python.png" height=300>

Errors and exceptions are an integral part of Python programming. They are used to signal the occurrence of an unexpected event or condition in your program that, if not properly handled, will cause your program to crash. 

You can read more about in [**Exception & Error Handling in Python**](https://www.datacamp.com/tutorial/exception-handling-python).

## Pytest

<img src="https://docs.pytest.org/en/7.4.x/_static/pytest_logo_curves.svg" height=300>

Testing is an essential part of software development. It helps you to ensure that your code is working as expected. It also helps you to identify and fix bugs in your codebase. In Python, one of the most popular testing frameworks is [**pytest**](https://docs.pytest.org/en/7.4.x/).

To install pytest, run the following command:

```bash
pip install pytest
```

## Logging

Utilizing Python's logging library offers a multitude of advantages in application development. It enables structured and organized logging of information, warnings, errors, and more. With various severity levels such as DEBUG, INFO, WARNING, ERROR, and CRITICAL, you have control over the level of detail in your log messages.

You can read more about in [**Logging in Python**](https://docs.python.org/3/library/logging.html).

# 🗂️ Projects

[**🎯 Project 01**](./Project_01/) - **Movie Recommendation System in Python**

[**🎯 Project 02**](./Project_02/) - **Airflow Data Pipeline to Download Podcasts**

[**🎯 Project 03**](./Project_03/) - **Optimizing Model Prediction**

# 📚 References

[🎥 **Video**](https://youtu.be/mMltyggT_KQ)

[🏅 **Intermediate Python for Web Development**](https://app.dataquest.io/view_cert/17W0Y3SZ1DA64H7NVTE5)

[🌐 **Errors and Exceptions**](https://docs.python.org/3/tutorial/errors.html)

[🌐 **Pytest**](https://docs.pytest.org/en/latest/)

[🌐 **Logging**](https://realpython.com/python-logging/)

[🌐 **Codespaces**](https://learn.microsoft.com/pt-pt/training/student-hub/github-codespaces-for-students)

[🌐 **PEP - Python Enhancement Proposals**](https://peps.python.org/pep-0000/#introduction)

[🌐 **Pylint**](https://github.com/pylint-dev/pylint)
