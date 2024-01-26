# QA Genie

[English](README.md) | हिंदी

असंरचित डेटा से प्रश्न और उत्तर बनाने के लिए, QA Genie नामक पायथन पैकेज बनाया गया है। 

यह पैकेज HuggingChat के अनऑफ़िशियल API: [hugchat](https://pypi.org/project/hugchat/) का उपयोग करके बनाया गया है। यह प्रश्न और उत्तर बनाने के लिए HuggingChat की क्षमताओं का लाभ उठाता है।

[![PyPi](https://img.shields.io/pypi/v/qa_genie.svg?logo=pypi&logoColor=white)](https://pypi.python.org/pypi/qa_genie)
[![Support_Platform](https://img.shields.io/badge/3.9+-%234ea94b.svg?logo=python&logoColor=white)](https://pypi.python.org/pypi/qa_genie)
[![स्तिथि](https://img.shields.io/badge/status-operational-%234ea94b.svg?logo=ok&logoColor=white)](https://pypi.python.org/pypi/qa_genie)
[![डाउनलोड्स](https://static.pepy.tech/badge/qa_genie?logo=download&logoColor=white)](https://www.pepy.tech/projects/qa_genie)

> **नोट**
>
> यह पैकेज अपने अल्फा रिलीज़ में है और जल्द ही और अधिक क्षमता जोड़ी जाएगी!


## स्थापना (Installation)
```bash
pip install qa_genie
```
or
```bash
pip3 install qa_genie
```


## उपयोग (Usage)
```python
email = "your_email@example.com" # huggingface अकाउंट की ईमेल 
password = "your_password" # huggingface अकाउंट का पासवर्ड 
model = "meta" # meta-llama/Llama-2-70b-chat-hf का उपयोग करने के लिए "meta" या OpenAssistant/oasst-sft-6-llama-30b का उपयोग करने के लिए "oasst" डाले

# चैटबॉट आरंभ करें
chatbot = get_generator(email, password, model)

# एकल वाक्य का उदाहरण उपयोग
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
result_single = extract_qa(chatbot, text, num_qn=3) # num_qn प्रश्नों और उत्तरों के साथ pandas.DataFrame लौटाता है

# Example usage with multiple texts
texts = ["Text 1", "Text 2", "Text 3"]
result_multiple = extract_qas(chatbot, texts, num_qn_each=3) # प्रत्येक वाक्य के लिए num_qn_each प्रश्नों और उत्तरों के साथ pandas.DataFrame लौटाता ह
```

## ध्यान दे (Important Note)
जैसा कि [Soulter](github.com/Soulter) ने लिखा है, सर्वर संसाधन कीमती हैं, इस API को उच्च आवृत्ति में अनुरोध करने की अनुशंसा नहीं की जाती है।

## योगदान (Contributing)
आपके योगदान की अत्यधिक सराहना की जाती है :)
