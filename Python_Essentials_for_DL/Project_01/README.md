# 📖 Introduction

A Transformer is a deep learning model that adopts the mechanism of attention, which is a mechanism that allows the model to focus on the relevant parts of the input sequence.

Here is a high-level overview of the components of a Transformer model:

<p align=center>
    <img src="https://s3.amazonaws.com/dq-content/796/2.2-m796.png"
    width=700/>
    <p align=center>
        <a href="https://app.dataquest.io/c/148/m/796/building-text-models-with-transformers/2/transformers?path=25&slug=deep-learning-in-tensorflow-skill&version=1">Source</a>
    </p>
</p>

- **Text**: The raw input data
- **Tokenizer**: Transforms the raw text into tokens
- **Input IDs**: The tokenized text converted into numbers
- **Attention Mask**: A binary mask indicating which tokens should be focused on and which should be ignored
- **Encoder**: The model that generates the embeddings
- **Classification**: The encoder output is used to classify the text
- **Output**: The final output of the model, representing the classification

## 🤗 Hugging Face and Transformers

Hugging Face is a community of NLP researchers who have built a large collection of open-source libraries and pretrained models. The Transformers library is one of their most popular libraries, and it contains thousands of pretrained models that can be used for a variety of NLP tasks.

# 📚 References

[🌐 **Building Text Models with Transformers**](https://app.dataquest.io/c/148/m/796/building-text-models-with-transformers/)


