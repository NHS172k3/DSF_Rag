# SC3021 Exercise: Data Science Ecosystems

Discussed in Week 4 Tutorial

## Data Science Problem Setting

In efforts to automatically generate reports for various government agencies, your company is contracted with developing an image recognition system that detects and transcribes handwritten text from scanned documents to digital form. The system shall be deployed in government archives to digitize historical records efficiently and effectively.

1 of 22

---

- Data engineering: list one example for required functionality for each data preparation step (i.e., profiling, structuring, enriching, cleaning)
- Data engineering: What data should be managed by a data management system? Explain how the required system(s) may differ from the relational data management systems introduced in class?
- Which type(s) of data analytics need to be considered for this application? Briefly explain your answer.
- Data understanding: Provide an example of an explanation that can support data understanding. Which users benefiting from it do you have in mind? Why is the proposed explanation useful to them?
- Data understanding: Provide an example of a visualization that can support data understanding. Which users benefiting from it do you have in mind? Why is the proposed visualization useful to them?
- Data protection: Give at least one example of a specific data security issue that you need to take into account during system development.
- Data protection: Give at least one example of a specific privacy issue that you need to take into account during system development.
- Data ethics: Give at least one example of a specific data ethics issue that may arise. Is it related to data, algorithms, or practices?

---

# DATA SCIENCE: A REDUCTIONIST VIEW

```python
import pandas as pd
import sklearn
... # do something
```

3 of 22

---

# DATA SCIENCE: A COMPLETE VIEW (BOSS')

- **Data engineering**
  - Data preparation
  - Data management
- **Data analytics**
  - Data exploration (data mining)
  - Models and algorithms (machine learning)
- **Data understanding**
  - Explanation
  - Visualization
- **Data protection**
  - Security
  - Privacy
- **Data ethics**
  - Impact on individuals, organizations, and society
  - Bias in data
  - Algorithmic bias
  - Regulatory issues

4 of 22

---

# DEFINE THE PROBLEM

In efforts to automatically generate reports for various government agencies, your company is contracted with developing an image recognition system that detects and transcribes handwritten text from scanned documents to digital form. The system shall be deployed in government archives to digitize historical records efficiently and effectively.

> What features do we want the system to have?

> Hint: Be creative, be a boss

5 of 22

---

# FEATURES

- A web interface to upload document scans and get transcripts in PDF, DOCX, etc...
- A search engine to search through the scanned documents
- Password-protection to restrict access to sensitive documents

6 of 22

---

# DATA SCIENCE BOSS

- **Data engineering**
  - Data preparation
  - Data management
- **Data analytics**
  - Data exploration (data mining)
  - Models and algorithms (machine learning)
- **Data understanding**
  - Explanation
  - Visualization
- **Data protection**
  - Security
  - Privacy
- **Data ethics**
  - Impact on individuals, organizations, and society
  - Bias in data
  - Algorithmic bias
  - Regulatory issues

7 of 22

---

# TYPES OF DATA ANALYTICS

> DATAFOREST

- Descriptive
  - What happened?
- Diagnostic
  - Why did it happen?
- Predictive
  - What will happen?
- Prescriptive
  - How can we make it happen?

> VALUE

> COMPLEXITY

> What kind of analytics is this?

In efforts to automatically generate reports for various government agencies, your company is contracted with developing an image recognition system that detects and transcribes handwritten text from scanned documents to digital form. The system shall be deployed in government archives to digitize historical records efficiently and effectively.

8 of 22

---

# KINDS OF ANALYTICS

- Predictive: get the text from the image
- Descriptive: get a description of the handwritten document

---

# WHICH DATA DO WE NEED ??????

> In efforts to automatically generate reports for various government agencies, your company is contracted with developing an image recognition system that detects and transcribes handwritten text from scanned documents to digital form. The system shall be deployed in government archives to digitize historical records efficiently and effectively.

10 of 22

---

# WHICH DATA DO WE NEED?

> The company probably already has an image-to-text model, but might not be trained on administrative languages or notations; or old archives

> The government provides the company with a representative sample of handwritten documents, with (possibly) their transcriptions

> What to do?

---

# Data engineering

- Data preparation
- Data management

# Data analytics

- Data exploration
  - (data mining)
- Models and algorithms
  - (machine learning)

# Data understanding

- Explanation
- Visualization

# Data protection

- Security
- Privacy

# Data ethics

- Impact on individuals, organizations, and society
- Bias in data
- Algorithmic bias
- Regulatory issues

- Data engineering: list one example for required functionality for each data preparation step (i.e., profiling, structuring, enriching, cleaning)

> The government provides the company with a representative sample of handwritten documents, with (possibly) their transcriptions

12 of 22

---

# DATA PREPARATION

- Profiling: investigate document types, languages; identify issues such as faded pages or stained papers
- Enriching: convert images to text with existing tools
- Cleaning: use spell checker on resulting texts; improve images through filters/contrast improvements

13 of 22

---

- Data engineering: What data should be managed by a data management system? Explain how the required system(s) may differ from the relational data management systems introduced in class?

> Relational data management systems = tables;

> Here we need some other systems, such as e.g. a file system

<table>
    <tr>
        <th>Name</th>
        <th>Kind</th>
    </tr>
    <tr>
        <td>civil_code_1992_page_1.jpg</td>
        <td>JPEG image</td>
    </tr>
    <tr>
        <td>civil_code_1992_page_1.txt</td>
        <td>text</td>
    </tr>
    <tr>
        <td>government_report_1995.jpg</td>
        <td>JPEG image</td>
    </tr>
    <tr>
        <td>government_report_1995.txt</td>
        <td>text</td>
    </tr>
</table>14 of 22

---

<table>
    <tr>
        <th>Name</th>
        <th>Kind</th>
    </tr>
    <tr>
        <td>civil_code_1992_page_1.jpg</td>
        <td>JPEG image</td>
    </tr>
    <tr>
        <td>civil_code_1992_page_1.txt</td>
        <td>text</td>
    </tr>
    <tr>
        <td>government_report_1995.jpg</td>
        <td>JPEG image</td>
    </tr>
    <tr>
        <td>government_report_1995.txt</td>
        <td>text</td>
    </tr>
</table># How to visualize?
## Be creative!

- Data understanding: Provide an example of a visualization that can support data understanding. Which users benefiting from it do you have in mind? Why is the proposed visualization useful to them?

15 of 22

---

# CONVERT HANDWRITING TO TEXT

## Before

one is going to love you exactly like
you imagine. No one is is ever going
to read your mind and take every
star from the sky at the perfect time
and hand it to you. No one is going
to show up at your door on a horse,
with a shoe you lost. Do you
understand? That's why you have to
love yourself enough, so that any
other love just adds more candles to
the cake you've already iced.
- Stephanie Bennett - Henry

## After

one is going to love you exactly like you imagine.
No one is ever going to read your mind and take
every story from the sky at the perfect zyme and
hand it to you. No one is going to show up at
one is going to love you exactly like you imagine.
hand it to you. No one is going to show up at
one is going to love you exactly like you imagine.
No one is ever going to read your mind and take
every story from the sky at the perfect zyme and
hand it to you. No one is going to show up at
your door on a horse, with a shoe you lost. Do
you understand That's why you have to love
yourself enough, so that any other love just adds
Stephanie Bennett - Hendy

---

# DIFFERENCE BETWEEN SECURITY AND PRIVACY?

- Security = prevent illegal access to data
- Privacy = prevent illegal use by someone who has legal access to data
- A little bit too simplistic...

---

In efforts to automatically generate reports for various government agencies, your company is contracted with developing an image recognition system that detects and transcribes handwritten text from scanned documents to digital form. The system shall be deployed in government archives to digitize historical records efficiently and effectively.

# SECURITY CONCERNS?

# PRIVACY CONCERNS?

18 of 22

---

# SECURITY AND PRIVACY

- Security: government data can be sensitive, needing appropriate access control
- Privacy: make sure private data doesn't enter into training procedure

---

- Data understanding: Provide an example of an explanation that can support data understanding. Which users benefiting from it do you have in mind? Why is the proposed explanation useful to them?

<table>
    <tr>
        <th>Name</th>
        <th>Kind</th>
    </tr>
    <tr>
        <td>civil_code_1992_page_1.jpg</td>
        <td>JPEG image</td>
    </tr>
    <tr>
        <td>civil_code_1992_page_1.txt</td>
        <td>text</td>
    </tr>
    <tr>
        <td>government_report_1995.jpg</td>
        <td>JPEG image</td>
    </tr>
    <tr>
        <td>government_report_1995.txt</td>
        <td>text</td>
    </tr>
</table># Example:
## How to measure transcription quality?

- Compare text to see the differences
- Test by document types
- Get, e.g. proportion of wrong/missing transcription per doc types

> 20 of 22

---

1 The quick brown fox jumps over the lazy dog.
1 The yellow fox jumps over the smart handsome dog.

> The quick brown fox jumps over the lazy dog.
> The yellow fox jumps over the smart handsome dog.

# Edit Distance Example
enjoyalgorithms.com

String 1
- I
- N
- T
- E
- [Insert C]
- N
- T
- I
- O
- N

String 2
- [Delete I]
- E
- X
- E
- C
- U
- T
- I
- O
- N

- Replace E
- Replace x
- Insert C
- Replace U

<table>
  <thead>
    <tr>
        <th>String 1</th>
        <th>I</th>
        <th>N</th>
        <th>T</th>
        <th>E</th>
        <th></th>
        <th>N</th>
        <th>T</th>
        <th>I</th>
        <th>O</th>
        <th>N</th>
    </tr>
    <tr>
        <th>String 2</th>
        <th></th>
        <th>E</th>
        <th>X</th>
        <th>E</th>
        <th>C</th>
        <th>U</th>
        <th>T</th>
        <th>I</th>
        <th>O</th>
        <th>N</th>
    </tr>
  </thead>
</table>