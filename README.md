# QA Genie

English | [हिंदी](README_hi.md) 

QA Genie is a Python package designed for generating questions and answers from unstructured data.

This package is built using the unofficial API of HuggingChat: [hugchat](https://pypi.org/project/hugchat/). It leverages HuggingChat's capabilities for question and answer generation.


[![PyPi](https://img.shields.io/pypi/v/qa_genie.svg?logo=pypi&logoColor=white)](https://pypi.python.org/pypi/qa_genie)
[![Support_Platform](https://img.shields.io/badge/3.9+-%234ea94b.svg?logo=python&logoColor=white)](https://pypi.python.org/pypi/qa_genie)
[![Status](https://img.shields.io/badge/status-operational-%234ea94b.svg?logo=ok&logoColor=white)](https://pypi.python.org/pypi/qa_genie)
[![Downloads](https://static.pepy.tech/badge/qa_genie?logo=download&logoColor=white)](https://www.pepy.tech/projects/qa_genie)

> **Note**
>
> This package is in its alpha release and more functionality will be added soon! <br>
> **Update 1.0.0a3:** This update enables the user to adjust iteration time. (Solves #1) 


## Installation
```bash
pip install qa_genie
```
or
```bash
pip3 install qa_genie
```


## Usage
```python
email = "your_email@example.com" # huggingface account email
password = "your_password" # huggingface account password
model = "meta" # use "meta" to use meta-llama/Llama-2-70b-chat-hf or "oasst" to use OpenAssistant/oasst-sft-6-llama-30b

# Initialize chatbot
chatbot = get_generator(email, password, model)

# Example usage with a single text
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
result_single = extract_qa(chatbot, text, num_qn=3) # returns pandas.DataFrame with num_qn questions and answers

# Example usage with multiple texts
texts = ["Text 1", "Text 2", "Text 3"]
result_multiple = extract_qas(chatbot, texts, num_qn_each=3) # return pandas.DataFrame with num_qn_each questions and answers generated for each text
```

## Important Note
As mentioned by [Soulter](github.com/Soulter), Server resources are precious, it is not recommended to request this API in a high frequency.

## Contributing
Feel free to contribute to QA Genie by creating issues, submitting pull requests, or suggesting improvements. Your contributions are highly appreciated :)
